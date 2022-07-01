# RocketMQ——Consumer篇：PULL模式下的消息消费（DefaultMQPullConsumer）

### 1 应用层的使用方式

在应用层初始化DefaultMQPullConsumer类，然后调用该类的start方法启动Consumer；接下来的消费步骤如下：

1、调用DefaultMQPullConsumer.fetchSubscribeMessageQueues(String topic)方法，根据topic获取对应的MessageQueue（即可被订阅的队列），在该方法中最终通过调用MQAdminImpl.fetchSubscribeMessageQueues(String topic)方法从NameServer获取该topic的MessageQueue，大致逻辑如下：

1.1）调用MQClientAPIImpl.getTopicRouteInfoFromNameServer(String topic, long timeoutMillis)方法，其中timeoutMillis=3000，该方法向NameServer发送GET_ROUTEINTO_BY_TOPIC请求码获取topic参数对应的Broker信息和topic配置信息，即TopicRouteData对象；

1.2）遍历TopicRouteData对象的QueueData列表中每个QueueData对象，首先判断该QueueData对象是否具有读权限，若有则根据该QueueData对象的readQueueNums值，创建readQueueNums个MessageQueue对象，并构成MessageQueue集合；最后返回给MessageQueue集合；

1.3)若上一步构建的MessageQueue集合不为空，则返回给该集合，否则抛MQClientException异常；

2、调用 DefaultMQPullConsumer.pullBlockIfNotFound( MessageQueue mq, String subExpression, long offset, int maxNums)方法获取该 MessageQueue队列下面从offset位置开始的消息内容，其中maxNums=32即表示获取的最大消息个数，offset为该MessageQueue对象的开始消费位置，可以调用DefaultMQPullConsumer.fetchConsumeOffset(MessageQueue mq, boolean fromStore)方法获取该MessageQueue队列的消费进度来设定参数offset值（详见5.6.2小节）；该方法最终调用DefaultMQPullConsumerImpl.pullSyncImpl(MessageQueue mq, String subExpression, long offset, int maxNums, boolean block)方法，该方法的大致逻辑如下：

2.1）检查MessageQueue对象的topic是否在RebalanceImpl.subscriptionInner:ConcurrentHashMap<String,SubscriptionData>变量中，若不在则以consumerGroup、topic、subExpression为参数调用**FilterAPI.buildSubscriptionData(String consumerGroup, String topic, String subExpression)**方法构造SubscriptionData对象保存到RebalanceImpl.subscriptionInner变量中，其中 **subExpression="\*"** ；

2.2）构建消息的标志位sysFlag，其中suspend和subscription为true（即该标记位的第2/3位为1），其他commit和classFilter两位为false（第1/4位为0）；

2.3）以请求参数subExpression以及consumerGroup、topic为参数调用**FilterAPI.buildSubscriptionData(String consumerGroup,Stringtopic, String subExpression)**方法构造SubscriptionData对象并返回；

2.4）调用PullAPIWrapper.pullKernelImpl(MessageQueue mq, String subExpression, long subVersion, long offset, int maxNums, int sysFlag, long commitOffset, long brokerSuspendMaxTimeMillis, long timeoutMillis, CommunicationMode communicationMode, PullCallback pullCallback)方法从Broker拉取消息内容；

2.5）调用PullAPIWrapper.processPullResult(MessageQueue mq, PullResult pullResult, SubscriptionData subscriptionData)方法对拉取消息的响应结果进行处理，主要是消息反序列化；（详细逻辑见 5.5.2小节—内部匿名类PullCallback的onSuccess方法部分）

3、在本地创建offseTable:Map<MessageQueue, Long>变量，根据上一步返回的结果，将该MessageQueue的下一次消费开始位置记录下来；

### 2 获取队列的消费进度（fetchConsumeOffset）

调用DefaultMQPullConsumer.fetchConsumeOffset(MessageQueue mq, boolean fromStore)方法获取MessageQueue队列的消费进度，其中fromStore为true表示从存储端（即Broker端）获取消费进度；若fromStore为false表示从本地内存获取消费进度；

1、对于从存储端获取消费进度（即fromStore=true）的情况：

1.1)对于LocalFileOffsetStore对象，从本地加载offsets.json文件，然后获取该MessageQueue对象的offset值；

1.2)对于RemoteBrokerOffsetStore对象,获取逻辑如下：

A）以MessageQueue对象的brokername从MQClientInstance. brokerAddrTable中获取Broker的地址；若没有获取到则立即调用updateTopicRouteInfoFromNameServer方法然后再次获取；

B）构造QueryConsumerOffsetRequestHeader对象，其中包括topic、consumerGroup、queueId；然后调用MQClientAPIImpl.queryConsumerOffset (String addr, QueryConsumerOffsetRequestHeader requestHeader, long timeoutMillis)方法向Broker发送QUERY_CONSUMER_OFFSET请求码，获取消费进度Offset；

C）用上一步从Broker获取的offset更新本地内存的消费进度列表数据RemoteBrokerOffsetStore.offsetTable:ConcurrentHashMap<MessageQueue, AtomicLong>变量值；

D）返回该offset值；

2、对于从本地内存获取消费进度（即fromStore=false）的情况：

对于LocalFileOffsetStore或者RemoteBrokerOffsetStore对象，均是以MessageQueue对象作为key值从各自对象的offsetTable变量中获取相应的消费进度。