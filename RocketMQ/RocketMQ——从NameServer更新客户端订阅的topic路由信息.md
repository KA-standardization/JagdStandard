#RocketMQ——从NameServer更新客户端订阅的topic路由信息



由Producer或Consumer端调用MQClientInstance. updateTopicRouteInfoFromNameServer()方法的目的主要有：

1）从NameServer获取该客户端订阅的每个topic的相关信息（包括每个topic对应的Broker信息和topic配置信息），用TopicRouteData对象表示；并将该对象信息存入MQClientInstance.topicRouteTable变量中；

2）根据返回的信息更新topic对应的BrokerName和BrokerId，保存在变量 **MQClientInstance.brokerAddrTable中；**

3）对于Prodcuer，根据每个topic以及配置的写队列个数创建MessageQueue消费队列，并存入变量DefaultMQProducerImpl.topicPublishInfoTable中；

4）对于已经订阅了该topic的Consumer，根据每个topic以及配置的读队列个数创建MessageQueue消费队列，并存入变量RebalanceImpl. topicSubscribeInfoTable中；

大致逻辑如下：

1、获取Producer或Consumer端的所有topic列表，步骤如下：

1.1）对于PushConsumer端：遍历MQClientInstance.consumerTable:

ConcurrentHashMap<String/* group */, MQConsumerInner>变量，对于每个DefaultMQPushConsumerImpl（MQConsumerInner的子类），获取DefaultMQPushConsumerImpl.rebalanceImpl:RebalanceImpl变量中的RebalanceImpl.subscriptionInner:ConcurrentHashMap<String, SubscriptionData>变量的values值，即SubscriptionData的集合；然后遍历SubscriptionData集合，取出每个SubscriptionData对象的topic变量值，即构成了该PushConsumer端的所有topic列表；

1.2）对于PullConsumer端：遍历MQClientInstance.consumerTable:

ConcurrentHashMap<String/* group */, MQConsumerInner>变量，对于每个DefaultMQPullConsumerImpl（MQConsumerInner的子类），对应的DefaultMQPullConsumer.registerTopics的变量值集合构成了该PullConsumer端的所有topic列表；

1.3）对于Producer端：遍历MQClientInstance.producerTable: ConcurrentHashMap<String/* group */, MQProducerInner>变量，DefaultMQProducerImpl为MQProducerInner的子类，获取每个DefaultMQProducerImpl.topicPublishInfoTable:ConcurrentHashMap<String/* topic */, TopicPublishInfo>变量的key值集合，即构成了Producer端的topic列表；对于刚启动的Producer，该topic列表只有默认值"TBW102"；

2、遍历上一步获取的topic列表，以每个topic为参数调用MQClientInstance.updateTopicRouteInfoFromNameServer(String topic)方法，在该方法中调用updateTopicRouteInfoFromNameServer(String topic, boolean isDefault, DefaultMQProducer defaultMQProducer)方法，其中isDefault=false，defaultMQProducer=null，大致步骤如下：

2.1）在此调用中请求参数isDefault=false，defaultMQProducer=null，则以参数topic向NameServer发送GET_ROUTEINTO_BY_TOPIC 请求码的请求从NameServer获取对应的Broker信息和topic配置信息，即返回TopicRouteData对象。但是若isDefault=true并且defaultMQProducer不等于null，则以主题名"TBW102"为topic向NameServer发送GET_ROUTEINTO_BY_TOPIC 请求码的请求从NameServer获取对应的Broker信息和topic配置信息，即返回TopicRouteData对象。

2.2）若第2.1步获取的TopicRouteData对象为空则直接返回，否则继续下面的操作；根据topic参数值从MQClientInstance.topicRouteTable本地列表中获取TopicRouteData对象；

2.3）比较从本地列表获取的TopicRouteData对象与从NameServer获取获取的TopicRouteData对象是否相等，若不相等则表示要更新topic信息，继续执行第2.4步操作；若相等则再检查MQClientInstance.consumerTable或者producerTable变量中每个Producer或Consumer端是否都包含该topic的订阅信息或者订阅信息中的MessageQueue队列是否为空，若没有订阅信息或者订阅信息中的队列为空则返回true并继续执行2.4步的操作；

A）对于Producer端：遍历MQClientInstance.producerTable: ConcurrentHashMap<String/* group */, MQProducerInner>变量中的每个DefaultMQProducerImpl对象，调用DefaultMQProducerImpl对象的isPublishTopicNeedUpdate(String topic)方法，在该方法中，以topic值获取DefaultMQProducerImpl.topicPublishInfoTable:ConcurrentHashMap<String/* topic */, TopicPublishInfo>变量的TopicPublishInfo对象，若遇到获取的该对象为null或者该对象的messageQueueList:List<MessageQueue>列表变量为空则跳出该遍历过程，并返回true，表示需要更新topic信息；

B）对于PushConsumer端：遍历MQClientInstance.consumerTable:

ConcurrentHashMap<String/* group */, MQConsumerInner>变量中的每个DefaultMQPushConsumerImpl对象，首先调用DefaultMQPushConsumerImpl对象的isSubscribeTopicNeedUpdate(String topic)方法，在该方法中获取DefaultMQPushConsumerImpl.rebalanceImpl: RebalanceImpl变量中的RebalanceImpl.subscriptionInner:ConcurrentHashMap<String/*topic*/, SubscriptionData>变量，检查该Consumer是否订阅了此topic（在Consumer启动时设置该变量的值），即该topic是否再该subscriptionInner变量中，若不在则继续遍历其他的DefaultMQPushConsumerImpl对象直到遍历完为止；若在subscriptionInner变量中则再检查该topic是否在RebalanceImpl.topicSubscribeInfoTable: ConcurrentHashMap<String/*topic*/, Set<MessageQueue>>变量中；若不在则表示该topic有订阅关系但是没有生成MessageQueue列表，则返回true（表示需要更新topic信息）并且跳出此遍历过程。

C）对于PullConsumer端的判断逻辑与PushConsumer端是一样的；

2.4）遍历从NameServer获取的TopicRouteData对象的BrokerDatas变量，将每个BrokerData对象的BrokerName和BrokerAddr:HashMap<Long/*brokerId */, String/* broker address*/>为key、values值存入 **MQClientInstance.brokerAddrTable: ConcurrentHashMap<String/\*BrokerName*/,HashMap<Long/*brokerId*/, String/*address*/>>变量中** ；

2.5）更新Producer端的topic信息：

A）调用MQClientInstance.topicRouteData2TopicPublishInfo(String topic, TopicRouteData route)方法创建TopicPublishInfo对象： 
A.1）若TopicRouteData对象的orderTopicConf不为空并且长度大于零，则以";"解析成数组，数组的每个成员是以":"分隔的，结构是"brokerName:queueNum"；遍历数组的每个成员变量，为每个成员变量创建queueNum个MessageQueue对象，存入TopicPublishInfo.messageQueueList: List<MessageQueue>变量中；遍历结束之后将TopicPublishInfo.orderTopic设置为true； 
A.2）若TopicRouteData对象的orderTopicConf为空，则取TopicRouteData对象的QueueData列表；然后遍历该QueueData列表的每个QueueData对象：

- A.2.1）检查该QueueData对象是否具有写权限；若没有则继续遍历下一个QueueData对象；

- A.2.2）对于QueueData对象的BrokerName值，若该值等于TopicRouteData对象的BrokerData列表中某一BrokerData对象的BrokerName值，再检查BrokerData对象的BrokerAddr:HashMap<Long/* brokerId */, String/* broker address */>列表中是否包含了主用Broker（ID=0）,即检查BrokerName名下是否有主用Broker; 若存在主用Broker，则取该QueueData对象的writeQueueNums值，以该Broker的name、入参topic、从0开始的序号（小于writeQueueNums）为参数初始化writeQueueNums个MessageQueue对象， **存入TopicPublishInfo.messageQueueList:List<MessageQueue>变量中** ；若该BrokerName集群下面没有主用Broker，则不创建写入队列MessageQueue对象；

- A.2.3）继续遍历下一个QueueData对象,直到遍历完该QueueData列表为止，最后将TopicPublishInfo.orderTopic设置为false；

  A.3）返回TopicPublishInfo对象；

  B）设置TopicPublishInfo.haveTopicRouterInfo等于true，表示已经有最新topic信息，即TopicPublishInfo对象；

  C）遍历MQClientInstance.producerTable: ConcurrentHashMap<String/* group */, MQProducerInner>变量，调用每个DefaultMQProducerImpl对象的updateTopicPublishInfo(String topic, TopicPublishInfo info)方法，以该topic为key值、上一步返回的TopicPublishInfo对象为values值 **存入该DefaultMQProducerImpl.topicPublishInfoTable变量中；**

  2.6）更新Consumer端的topic信息：

  A）构建MessageQueue列表。遍历TopicRouteData对象的QueueData列表中每个QueueData对象，首先判断该QueueData对象是否具有读权限，若有则根据该QueueData对象的readQueueNums值，创建readQueueNums个MessageQueue对象，并构成MessageQueue集合；最后返回该MessageQueue集合；

  B）对于PushConsumer端和PullConsumer端，处理逻辑是一样的，以DefaultMQPushConsumerImpl为例：遍历MQClientInstance.consumerTable:ConcurrentHashMap<String/* group */, MQConsumerInner>中的MQConsumerInner对象；获取DefaultMQPushConsumerImpl.rebalanceImpl:RebalanceImpl变量中的RebalanceImpl.subscriptionInner：ConcurrentHashMap<String, SubscriptionData>变量值；若topic在该subscriptionInner变量值的列表中，则用topic和MessageQueue集合更新RebalanceImpl. topicSubscribeInfoTable:ConcurrentHashMap<String/* topic */, Set<MessageQueue>>变量；

  2.7）将该topic以及TopicRouteData对象存入MQClientInstance.topicRouteTable:ConcurrentHashMap<String/* Topic */,TopicRouteData>变量中；