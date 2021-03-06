# RocketMQ——Consumer篇：PUSH模式下的消息拉取（DefaultMQPushConsumer）

DefaultMQPushConsumerImpl中各个对象的主要功能如下：

RebalancePushImpl：主要负责决定，当前的consumer应该从哪些Queue中消费消息；

1）PullAPIWrapper：长连接，负责从broker处拉取消息，然后利用ConsumeMessageService回调用户的Listener执行消息消费逻辑；

2）ConsumeMessageService：实现所谓的"Push-被动"消费机制；从Broker拉取的消息后，封装成ConsumeRequest提交给ConsumeMessageSerivce，此service负责回调用户的Listener消费消息；

3）OffsetStore：维护当前consumer的消费记录（offset）；有两种实现，Local和Rmote，Local存储在本地磁盘上，适用于BROADCASTING广播消费模式；而Remote则将消费进度存储在Broker上，适用于CLUSTERING集群消费模式；

4）MQClientFactory：大杂烩，负责管理client（consumer、producer），并提供多中功能接口供各个Service（Rebalance、PullMessage等）调用；大部分逻辑均在这个类中完成；

### 1 消息拉取入口

调用DefaultMQPushConsumerImpl.pullMessage(PullRequest pullRequest)方法进行消息的拉取。该方法的大致逻辑如下：

1、检查PullRequest对象中的ProcessQueue对象的dropped是否为true（在RebalanceService线程中为topic下的MessageQueue创建拉取消息请求时要维护对应的ProcessQueue对象，若Consumer不再订阅该topic则会将该对象的dropped置为true）；若是则认为该请求是已经取消的，则直接跳出该方法；

2、更新PullRequest对象中的ProcessQueue对象的时间戳（ProcessQueue.lastPullTimestamp）为当前时间戳；

3、检查该Consumer是否运行中，即DefaultMQPushConsumerImpl.serviceState是否为RUNNING;若不是运行状态或者是暂停状态（DefaultMQPushConsumerImpl.pause=true），则调用PullMessageService.executePullRequestLater(PullRequest pullRequest, long timeDelay)方法延迟再拉取消息，其中timeDelay=3000；该方法的目的是在3秒之后再次将该PullRequest对象放入PullMessageService. pullRequestQueue队列中；并跳出该方法；

4、进行流控。若ProcessQueue对象的msgCount大于了消费端的流控阈值（DefaultMQPushConsumer.pullThresholdForQueue，默认值为1000），则调用PullMessageService.executePullRequestLater方法，在50毫秒之后重新该PullRequest请求放入PullMessageService.pullRequestQueue队列中；并跳出该方法；

5、若不是顺序消费（即DefaultMQPushConsumerImpl.consumeOrderly等于false），则检查ProcessQueue对象的msgTreeMap:TreeMap<Long,MessageExt>变量的第一个key值与最后一个key值之间的差额，该key值表示查询的队列偏移量queueoffset；若差额大于阈值（由DefaultMQPushConsumer. consumeConcurrentlyMaxSpan指定，默认是2000），则调用PullMessageService.executePullRequestLater方法，在50毫秒之后重新将该PullRequest请求放入PullMessageService.pullRequestQueue队列中；并跳出该方法；

6、以PullRequest.messageQueue对象的topic值为参数从RebalanceImpl.subscriptionInner: ConcurrentHashMap<String /* topic */, SubscriptionData>中获取对应的SubscriptionData对象，若该对象为null，考虑到并发的关系，调用executePullRequestLater方法，稍后重试；并跳出该方法；

7、若消息模型为集群模式（RebalanceImpl.messageModel等于CLUSTERING），则以PullRequest对象的MessageQueue变量值、type =READ_FROM_MEMORY（从内存中获取消费进度offset值）为参数调用DefaultMQPushConsumerImpl. offsetStore对象（初始化为RemoteBrokerOffsetStore对象）的readOffset(MessageQueue mq, ReadOffsetType type)方法从本地内存中获取消费进度offset值。若该offset值大于0 则置临时变量commitOffsetEnable等于true否则为false；该offset值作为pullKernelImpl方法中的commitOffset参数，在Broker端拉取消息之后根据commitOffsetEnable参数值决定是否用该offset更新消息进度。该readOffset方法的逻辑是：以入参MessageQueue对象从RemoteBrokerOffsetStore.offsetTable:ConcurrentHashMap <MessageQueue,AtomicLong>变量中获取消费进度偏移量；若该偏移量不为null则返回该值，否则返回-1；

8、当每次拉取消息之后需要更新订阅关系（由DefaultMQPushConsumer. postSubscriptionWhenPull参数表示，默认为false）并且以topic值参数从RebalanceImpl.subscriptionInner获取的SubscriptionData对象的classFilterMode等于false（默认为false），则将sysFlag标记的第3个字节置为1，否则该字节置为0；

9、该sysFlag标记的第1个字节置为commitOffsetEnable的值；第2个字节（suspend标记）置为1；第4个字节置为classFilterMode的值；

10、 **初始化匿名内部类PullCallback，实现了onSucess/onException方法；** 该方法只有在异步请求的情况下才会回调；

11、调用底层的拉取消息API接口：PullAPIWrapper.pullKernelImpl(MessageQueue mq, String subExpression, long subVersion,long offset, int maxNums, int sysFlag,long commitOffset,long brokerSuspendMaxTimeMillis, long timeoutMillis, CommunicationMode communicationMode, PullCallback pullCallback)方法进行消息拉取操作（详见5.9小节）。将回调类PullCallback传入该方法中，当采用异步方式拉取消息（详见5.10.2小节）时，在收到响应之后会回调该回调类的方法。

### 2 拉取消息的底层API接口（PullAPIWrapper.pullKernelImpl）

PUSH模式和PULL模式下的拉取消息的操作均调用PullAPIWrapper.pullKernelImpl(MessageQueue mq, String subExpression, long subVersion,long offset, int maxNums, int sysFlag,long commitOffset,long brokerSuspendMaxTimeMillis, long timeoutMillis, CommunicationMode communicationMode, PullCallback pullCallback)方法完成。该方法的大致逻辑如下：

1、获取Broker的ID。以入参MessageQueue对象为参数调用PullAPIWrapper.recalculatePullFromWhichNode(MessageQueue mq)方法，在该方法中，先判断PullAPIWrapper.connectBrokerByUser变量是否为true（在FiltersrvController中启动时会设置为true，默认为false），若是则直接返回0（主用Broker的brokerId）；否则以MessageQueue对象为参数从PullAPIWrapper.pullFromWhichNodeTable:ConcurrentHashMap<MessageQueue, AtomicLong/* brokerId */>获取brokerId，若该值不为null则返回该值，否则返回0（主用Broker的brokerId）；

2、调用MQClientInstance.findBrokerAddressInSubscribe(String brokerName ,long brokerId,boolean onlyThisBroker) 方法查找Broker地址，其中onlyThisBroker=false，表示若指定的brokerId未获取到地址则获取其他BrokerId的地址也行。在该方法中根据brokerName和brokerId参数从MQClientInstance.brokerAddrTable: ConcurrentHashMap<String/* Broker Name */, HashMap<Long/* brokerId */, String/* address */>>变量中获取对应的Broker地址，若获取不到则从brokerName下面的Map列表中找其他地址返回即可；

3、若在上一步未获取到Broker地址，则以topic参数调用MQClientInstance.updateTopicRouteInfoFromNameServer(String topic)方法，然后在执行第2步的操作，直到获取到Broker地址为止；

4、若获取的Broker地址是备用Broker，则将标记位sysFlag的第1个字节置为0，即在消费完之后不提交消费进度；

5、检查标记位sysFlag的第4个字节（即SubscriptionData. classFilterMode）是否为1；若等于1，则调用PullAPIWrapper.computPullFromWhichFilterServer(String topic, String brokerAddr)方法获取Filter服务器地址。大致逻辑如下：

5.1)根据topic参数值从MQClientInstance.topicRouteTable: ConcurrentHashMap<String/*Topic*/,TopicRouteData>变量中获取TopicRouteData对象，

5.2)以Broker地址为参数从该TopicRouteData对象的filterServerTable:HashMap<String/* brokerAddr*/,List<String>/* FilterServer*/>变量中获取该Broker下面的所有Filter服务器地址列表；

5.3)若该地址列表不为空，则随机选择一个Filter服务器地址返回；否则向调用层抛出异常，该pullKernelImpl方法结束；

6、构建PullMessageRequestHeader对象，其中queueOffset变量值等于入参offset；

7、若执行了第5步则向获取的Filter服务器发送PULL_MESSAGE请求信息，否则向Broker发送PULL_MESSAGE请求信息。初始化PullMessageRequestHeader对象，然后调用MQClientAPIImpl.pullMessage(String addr, PullMessageRequestHeader requestHeader, long timeoutMillis, CommunicationMode communicationMode, PullCallback pullCallback)方法向Broker地址或者Filter地址发送PULL_MESSAGE请求信息（详见5.10小节）；

### 3 发送远程请求拉取消息的逻辑（PULL_MESSAGE）

在MQClientAPIImpl.pullMessage方法中，根据入参communicationMode的值分为异步拉取和同步拉取方式两种。

无论是异步方式拉取还是同步方式拉取，在发送拉取请求之前都会构造一个ResponseFuture对象，以请求消息的序列号为key值，存入NettyRemotingAbstract.responseTable:ConcurrentHashMap<Integer /* opaque */, ResponseFuture>变量中，对该变量有几种情况会处理：

1、发送失败后直接删掉responseTable变量中的相应记录；

2、收到响应消息之后，会以响应消息中的序列号（由服务端根据请求消息的序列号原样返回）从responseTable中查找ResponseFuture对象，并设置该对象的responseCommand变量。若是同步发送会唤醒等待响应的ResponseFuture.waitResponse方法；若是异步发送会调用ResponseFuture.executeInvokeCallback()方法完成回调逻辑处理；

3、在NettyRemotingClient.start()启动时，也会初始化定时任务，该定时任务每隔1秒定期扫描responseTable列表，遍历该列表中的ResponseFuture对象，检查等待响应是否超时，若超时，则调用ResponseFuture. executeInvokeCallback()方法，并将该对象从responseTable列表中删除；

### 3.1 同步方式拉取消息

对于同步发送方式，调用MQClientAPIImpl.pullMessageSync(String addr, RemotingCommand request, long timeoutMillis)方法。大致步骤如下：

1、调用RemotingClient.invokeSync(String addr, RemotingCommand request, long timeoutMillis)方法：

1.1）获取Broker地址的Channel信息。根据broker地址从RemotingClient.channelTables:ConcurrentHashMap<String /* addr */, ChannelWrapper>变量中获取ChannelWrapper对象并返回该对象的Channel变量；若没有ChannelWrapper对象则与broker地址建立新的连接并将连接信息存入channelTables变量中，便于下次使用；

1.2）若NettyRemotingClient.rpcHook:RPCHook变量不为空（该变量在应用层初始化DefaultMQPushConsumer或者DefaultMQPullConsumer对象传入该值），则调用RPCHook.doBeforeRequest(String remoteAddr, RemotingCommand request)方法；

1.3)调用NettyRemotingAbstract.invokeSyncImpl(Channel channel, RemotingCommand request, long timeoutMillis)方法，该方法的逻辑如下：

A）使用请求的序列号（opaue）、超时时间初始化ResponseFuture对象；并将该ResponseFuture对象存入NettyRemotingAbstract.responseTable: ConcurrentHashMap<Integer /* opaque */, ResponseFuture>变量中；

B）调用Channel.writeAndFlush(Object msg)方法将请求对象RemotingCommand发送给Broker；然后调用addListener(GenericFutureListener<? extends Future<? super Void>> listener)方法添加内部匿名类：该内部匿名类实现了ChannelFutureListener接口的operationComplete方法，在发送完成之后回调该监听类的operationComplete方法，在该方法中，首先调用ChannelFuture. isSuccess()方法检查是否发送成功，若成功则置ResponseFuture对象的sendRequestOK等于true并退出此回调方法等待响应结果；若不成功则置ResponseFuture对象的sendRequestOK等于false，然后从NettyRemotingAbstract.responseTable中删除此请求序列号（opaue）的记录，置ResponseFuture对象的responseCommand等于null，并唤醒ResponseFuture.waitResponse(long timeoutMillis)方法的等待；

C）调用ResponseFuture.waitResponse(long timeoutMillis)方法等待响应结果；在发送失败或者收到响应消息（详见5.10.3小节）或者超时的情况下会唤醒该方法返回ResponseFuture.responseCommand变量值；

D）若上一步返回的responseCommand值为null，则抛出异常:若ResponseFuture.sendRequestOK为true，则抛出RemotingTimeoutException异常，否则抛出RemotingSendRequestException异常；

E）若上一步返回的responseCommand值不为null，则返回responseCommand变量值；

1.4）若NettyRemotingClient.rpcHook: RPCHook变量不为空，则调用RPCHook.doAfterResponse(String remoteAddr, RemotingCommand request)方法；

2、以上一步的返回值RemotingCommand对象为参数调用MQClientAPIImpl. **processPullResponse** (RemotingCommand response)方法将返回对象解析并封装成PullResultExt对象然后返回给调用者，响应消息的结果状态转换如下：

2.1）若RemotingCommand对象的Code等于SUCCESS，则PullResultExt.pullStatus=FOUND；

2.2）若RemotingCommand对象的Code等于PULL_NOT_FOUND，则PullResultExt.pullStatus= NO_NEW_MSG；

2.3）若RemotingCommand对象的Code等于PULL_RETRY_IMMEDIATELY，则PullResultExt.pullStatus= NO_MATCHED_MSG；

2.3）若RemotingCommand对象的Code等于PULL_OFFSET_MOVED，则PullResultExt.pullStatus= OFFSET_ILLEGAL；

### 3.2 异步方式拉取消息

对于异步方式拉取消息，调用MQClientAPIImpl.pullMessageAsync(String addr, RemotingCommand request, long timeoutMillis, PullCallback pullCallback)方法。大致逻辑如下：

1、定义了一个内部匿名**InvokeCallback类并实现operationComplete (ResponseFuture responseFuture)方法**；该方法的大致逻辑如下：

1.1）从入参ResponseFuture对象中获取传输的响应对象RemotingCommand；

1.2）若该响应对象RemotingCommand不为空；则首先调用MQClientAPIImpl. **processPullResponse** (RemotingCommand response)方法对返回对象解析并封装成PullResultExt对象，其中PullResultExt.messageBinary等于响应消息的body；然后以PullResultExt对象为参数调用回调类PullCallback对象的onSuccess方法（调用应用层定义的回调方法，详见5.5.2小节），若在此过程中出现异常则调用PullCallback对象的onException方法（调用应用层定义的回调方法）；

1.3）若该返回对象RemotingCommand为空；则检查ResponseFuture.sendRequestOK是否为true，若不是则发送请求失败；若发生成功再检查是否等待超时；对于每种异常情况均调用PullCallback对象的onException方法由应用层来处理异常情况；

2、以匿名类InvokeCallback为参数调用NettyRemotingClient.invokeAsync(String addr, RemotingCommand request, long timeoutMillis, InvokeCallback invokeCallback)方法，大致逻辑如下：

2.1）获取Broker地址的Channel信息。根据broker地址从RemotingClient.channelTables: ConcurrentHashMap<String /* addr */, ChannelWrapper>变量中获取ChannelWrapper对象并返回该对象的Channel变量；若没有ChannelWrapper对象则与broker地址建立新的连接并将连接信息存入channelTables变量中，便于下次使用；

2.2）若NettyRemotingClient.rpcHook: RPCHook变量不为空（该变量在应用层初始化DefaultMQPushConsumer或者DefaultMQPullConsumer对象传入该值），则调用RPCHook.doBeforeRequest(String remoteAddr, RemotingCommand request)方法；

2.3）调用NettyRemotingAbstract.invokeAsyncImpl(Channel channel, RemotingCommand request,long timeoutMillis,InvokeCallback invokeCallback)方法，该方法的大致逻辑如下：

A）利用java.util.concurrent.Semaphore.tryAcquire(long timeout,TimeUnitunit)获取信号量，保证该方法的业务逻辑同时执行的线程个数；

B）使用请求的序列号（opaue）、超时时间、InvokeCallback对象、 用Semaphore初始化的SemaphoreReleaseOnlyOnce对象（该对象是确保在释放信号量是只释放一次）初始化ResponseFuture对象，并根据请求的序列号（opaue）作为key值，将该ResponseFuture对象存入NettyRemotingAbstract. responseTable对象中；

C）调用Channel.writeAndFlush(Object msg)方法将请求对象发送给Broker，并且添加监听器，再消息发送完成之后回调该监听器，该监听器是内部匿名类，该类实现了ChannelFutureListener接口的operationComplete(ChannelFuture f)方法，该方法的逻辑如下：

C.1）首先调用ChannelFuture.isSuccess()方法检查是否发送成功，若成功则置ResponseFuture对象的sendRequestOK等于true并退出此回调方法等待对方的响应消息；若不成功则置ResponseFuture对象的sendRequestOK等于false，然后继续执行下面的逻辑，主要目的是立即向应用层返回发送失败的响应消息，无需再等待对方的响应结果；

C.2）根据请求的序列号（opaue）从responseTable中删除相应的ResponseFuture对象记录；

C.3）将ResponseFuture.responseCommand变量置为null；

C.4）调用ResponseFuture.executeInvokeCallback()方法，在该方法中执行InvokeCallback.OperationComplete(ResponseFuture)方法完成回调工作，在executeInvokeCallback方法之前，确保ResponseFuture. executeCallbackOnlyOnce的值为false并且成功更新为true，由于executeCallbackOnlyOnce在初始化时为false，若更新失败说明该回调方法已经执行过了，故不在执行；

C.5）最后调用SemaphoreReleaseOnlyOnce对象的realse，释放信号量；