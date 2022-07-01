# RocketMQ-Name Server

## 1 NameServer的功能

1、每个Broker启动的时候会向Namesrv发送注册请求，Namesrv接收Broker的请求注册路由信息，NameServer保存活跃的broker列表，包括Master和Slave；

2、用来保存所有topic和该topic所有队列的列表；

3、NameServer用来保存所有broker的Filter列表

4、接收client（Producer和Consumer）的请求根据某个topic获取所有到broker的路由信息；

## 2 NameServer的初始化及启动过程

1、KVConfigManager类加载NameServer的配置参数，配置参数的路径是 $HOME /namesrv/kvConfig.json;将配置参数加载保存到KVConfigManager.configTable:HashMap<String/*namespace*/,HashMap<String/*key*/,String/*value*/>>变量中。

2、以初始化BrokerHousekeepingService对象为参数初始化NettyRemotingServer对象，BrokerHousekeepingService对象作为该Netty连接中Socket链接的监听器（ChannelEventListener）；监听与Broker建立的渠道的状态（空闲、关闭、异常三个状态），并调用BrokerHousekeepingService的相应onChannel****方法。其中渠道的空闲、关闭、异常状态均调用RouteInfoManager.onChannelDestory方法处理。清理RouteInfoManager类的几个成员变量数据：

| 变量名称          | 变量类型                                                     | 含义                                                         |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| topicQueueTable   | HashMap<String/*topic*/, List<QueueData>>                    | 主题与topic配置的对应关系，topics.json的topicConfigTable数据，在QueueData对象中记录了该topic的BrokerName |
| brokerAddrTable   | HashMap<String/*brokerName*/, BrokerData>                    | Broker名称与broker属性的map                                  |
| clusterAddrTable  | HashMap<String/* clusterName */, Set<String/* brokerName */>> | 集群与broker集合的对应关系                                   |
| brokerLiveTable   | HashMap<String/* brokerAddr */, BrokerLiveInfo>              | Broker的信息集合                                             |
| filterServerTable | HashMap<String/* brokerAddr */, List<String>/* Filter Server */> | Borker地址与过滤器的集合                                     |

3、注册默认的处理类DefaultRequestProcessor,所有的请求均由该处理类的processRequest方法来处理。

4、设置两个定时任务：

第一是每隔10秒检查一遍所有Broker的状态的定时任务，调用scanNotActiveBroker方法；大致逻辑是：遍历brokerLiveTable集合，查看每个broker的最后更新时间（BrokerLiveInfo.lastUpdateTimestamp）是否超过2分钟，若超过则关闭该broker的渠道并调用RouteInfoManager.onChannelDestory方法清理RouteInfoManager类的topicQueueTable、brokerAddrTable、clusterAddrTable、filterServerTable成员变量。

第二是每隔10分钟打印一次NameServer的配置参数。即KVConfigManager.configTable变量的内容。

5、启动NameServer的Netty服务端（NettyRemotingServer），监听渠道的请求信息。当收到客户端的请求信息之后会初始化一个线程，并放入线程池中进行处理,该线程调用DefaultRequestProcessor. processRequest方法来处理请求。

| 请求的KEY值                        | 作用                                                 |
| ---------------------------------- | ---------------------------------------------------- |
| PUT_KV_CONFIG                      | 向Namesrv追加KV配置                                  |
| GET_KV_CONFIG                      | 从Namesrv获取KV配置                                  |
| DELETE_KV_CONFIG                   | 从Namesrv获取KV配置                                  |
| REGISTER_BROKER                    | 注册一个Broker，数据都是持久化的，如果存在则覆盖配置 |
| UNREGISTER_BROKER                  | 卸载一个Broker，数据都是持久化的                     |
| GET_ROUTEINTO_BY_TOPIC             | 根据Topic获取Broker Name、topic配置信息              |
| GET_BROKER_CLUSTER_INFO            | 获取注册到Name Server的所有Broker集群信息            |
| WIPE_WRITE_PERM_OF_BROKER          | 去掉BrokerName的写权限                               |
| GET_ALL_TOPIC_LIST_FROM_NAMESERVER | 从Name Server获取完整Topic列表                       |
| DELETE_TOPIC_IN_NAMESRV            | 从Namesrv删除Topic配置                               |
| GET_KV_CONFIG_BY_VALUE             | 通过 project 获取所有的 server ip 信息               |
| DELETE_KV_CONFIG_BY_VALUE          | 删除指定 project group 下的所有 server ip 信息       |
| GET_KVLIST_BY_NAMESPACE            | 通过NameSpace获取所有的KV List                       |
| GET_KVLIST_BY_NAMESPACE            | 通过NameSpace获取所有的KV List                       |
| GET_TOPICS_BY_CLUSTER              | 获取指定集群下的所有 topic                           |
| GET_SYSTEM_TOPIC_LIST_FROM_NS      | 获取所有系统内置 Topic 列表                          |
| GET_UNIT_TOPIC_LIST                | 单元化相关 topic                                     |
| GET_HAS_UNIT_SUB_TOPIC_LIST        | 获取含有单元化订阅组的 Topic 列表                    |
| GET_HAS_UNIT_SUB_UNUNIT_TOPIC_LIST | 获取含有单元化订阅组的非单元化 Topic 列表            |

## 3 处理Broker注册请求

在接收到REGISTER_BROKER请求码之后，由DefaultRequestProcessor.registerBroker(ChannelHandlerContext ctx, RemotingCommand request)方法处理注册请求，在该方法中调用 RouteInfoManager.registerBroker(String clusterName, String brokerAddr, String brokerName, long brokerId, String haServerAddr, TopicConfigSerializeWrapper topicConfigWrapper, List<String> filterServerList, Channel channel)方法完成注册处理逻辑，注册完成后返回给Broker端主用Broker的地址，以及该主用Broker的HA服务地址。

1、维护RouteInfoManager.clusterAddrTable变量；若Broker集群名字不在该Map变量中，则初始化一个Set集合，将brokerName存入该Set集合中，然后以clusterName为key值，该Set集合为values值存入此Map变量中；说明一个集群下面有多个Broker；

2、维护RouteInfoManager.brokerAddrTable变量，该变量是维护Broker的名称、ID、地址等信息的。若该brokername不在该Map变量中，则创建BrokerData对象，该对象包含了brokername，以及brokerId和brokerAddr为K-V的brokerAddrs变量；然后以brokername为key值将BrokerData对象存入该brokerAddrTable变量中；说明同一个BrokerName下面可以有多个不同BrokerId的Broker存在，表示一个BrokerName有多个Broker存在，通过BrokerId来区分主备。

3、若Broker的注册请求消息中topic的配置不为空，并且该Broker是主用（即brokerId=0），则根据NameServer存储的Broker版本信息来判断是否需要更新NameServer端的topic配置信息。若是第一个注册，即表示Name Server端还没有该Broker的topic信息，或者在NameServer中维护的该Broker的dataversion与收到的topic配置（TopicConfigSerializeWrapper）的dataversion不一致；则更新NameServer端的topic配置信息。大致处理思路：

遍历TopicConfigSerializeWrapper对象的topicConfigTable变量，以该变量中的每个TopicConfig对象以及该Broker的名称为参数调用RouteInfoManager.createAndUpdateQueueData(String brokerName, TopicConfig topicConfig) 方法，该方法的逻辑是：

A）用TopicConfig对象中的各变量来初始化QueueData对象，包括的变量有：brokerName、读写队列数、权限等信息；

B）维护RouteInfoManager.topicQueueTable变量，该变量是维护topic配置信息的。以topic的名字从RouteInfoManager.topicQueueTable变量中获取QueueData列表；若没有则初始化该QueueData队列并将上一步初始化的QueueData对象存入；若已经存在QueueData队列，则遍历该队列中的每个QueueData对象，检查是否与该注册的Broker相同的名字的QueueData对象：

若相同则检查该QueueData对象的各个属性值是否与新创建的QueueData对象（在第A步中创建的）一致，若一致则表示是topic的配置没有变化则不更新QueueData队列的该QueueData对象，若不一致，则认为该topic有变化，要将该QueueData对象从QueueData列表中删除，然后将新创建的QueueData对象加入到此队列中；

若不相同则直接将QueueData对象加入到此QueueData队列中；

4、初始化BrokerLiveInfo 对象并以broker地址为key值存入brokerLiveTable:HashMap<String/* brokerAddr */, BrokerLiveInfo>变量中；

5、对于filterServerList不为空的，以broker地址为key值存入RouteInfoManager.filterServerTable :HashMap<String/* brokerAddr */, List<String>/* Filter Server */>变量中；

6、找到该BrokerName下面的主用Broker（BrokerId=0），方法是以该Brokerame从RouteInfoManager.BrokerAddrTable变量中获取BrokerData对象，然后取该对象的brokerAddrs变量，从该变量中找到BrokerId=0的Broker地址，作为该注册Broker对应的主用地址MasterAddr； 以主用Broker地址从brokerLiveTable中获取BrokerLiveInfo 对象，取该对象的HaServerAddr 值，将该地址作为HaServerAddr返回给Broker端，即主用Broker的HaServerAddr为其他备用Broker的HAClient.masterAddress值。

## 4 根据Topic获取Broker信息和topic配置信息（getRouteInfoByTopic）

当NameServer收到GET_ROUTEINTO_BY_TOPIC 请求码之后，间接调用了RouteInfoManager.pickupTopicRouteData(String topic)方法获取Broker信息和topic配置信息。

1、获取topic配置信息，根据topic从RouteInfoManager.topicQueueTable变量中获取List<QueueData>队列，赋值给返回对象TopicRouteData的QueueDatas变量。表示该topic对应的所有topic配置信息以及每个配置所属的BrokerName。

2、从上一步获取到的List<QueueData>队列中获取BrokerName集合，该集合是去重之后的BrokerName集合，然后以该BrokerName集合的每个BrokerName从RouteInfoManager.brokerAddrTable变量中获取BrokerData对象，将所有获取到的BrokerData对象集合赋值给返回对象TopicRouteData的BrokerDatas集合变量。表示该topic是由哪些Broker提供的服务，以及每个Broker的名字、BrokerId、IP地址。

然后以"ORDER_TOPIC_CONFIG"和请求消息中的topic值为参数从NamesrvController.kvConfigManager.configTable: HashMap<String/* Namespace */, HashMap<String/* Key */, String/* Value */>>变量中获取orderTopiconf值（即broker的顺序），并赋值给TopicRouteData.orderTopicConf变量；该orderTopiconf的参数格式为：以";"解析成数组，数组的每个成员是以":"分隔的，构成数据"brokerName:queueNum"；

最后将TopicRouteData对象返回给调用者；