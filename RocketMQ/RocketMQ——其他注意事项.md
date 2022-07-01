# RocketMQ——其他注意事项

### 1 消息过滤的方式

1、简单消息过滤。订阅时指定topic下面tags；

2、高级消息过滤。

2.1）Broker所在的机器会启动多个FilterServer过滤进程；

2.2）Consumer启动后，会向FilterServer上传一个过滤的Java类；

2.3）Consumer从FilterServer拉消息，FilterServer将请求转发给Broker，FilterServer从Broker收到消息后，按照Consumer上传的java过滤程序做过滤，过滤完成后返回给Consumer。

这两种方式的总结：

1）使用CPU资源来换取网卡流量资源；

2）FilterServer与Broker部署在同一台机器，数据通过本地回环通信，不走网卡；

3）一台Broker部署多个FilterServer，充分利用CPU资源，因为单个JVM难以全面利用高配的物理机CPU资源；

4）因为过滤代码使用Java编写，应用几乎可以做任意形式的服务器端消息过滤，例如通过Messgae Header进行过滤，甚至可以按照Message Body进行过滤；

5）使用Java语言进行作为过滤表达式是一个双刃剑，方便了应用的过滤操作，但是带来了服务器端的安全风险。需要应用来保证过滤代码安全，例如在过滤程序中尽可能不做申请大内存，创建线程等操作，避免Broker服务器发生资源泄露。

### 2 客户端寻找NameServer地址的方式

1、代码中指定NameServer地址；

2、java启动参数中指定NameServer地址:-Drocketmq.nameerv.addr

3、环境变量指定NameServer地址：NAMESRV_ADDR

4、HTTP静态服务器寻址。客户端启动后，会定时访问一个静态HTTP服务器,该URL返回NameServer地址列表。推荐使用HTTP静态服务器寻址方式，对于客户端部署简单，而且NameServer集群可以热升级。

### 3 发送消息注意事项

1、一个应用尽可能用一个Topic,消息子类型用tags来标识，tags可以由应用只有设置。只有发送消息设置了tags，消费方在订阅消息时，才可以利用tags在broker做消息过滤；

2、每个消息在业务层面的唯一标识码，要设置到keys字段，方便将来定位消息丢失问题。服务器会为每个消息创建索引，应该可以通过topic、key来查询这条消息内容以及消息被谁消费，由于哈希索引，请务必保证key尽可能唯一。

3、消息发送成功或者失败，要打印消息日志，务必大于sendResult和key字段；

4、send消息方法，只要不抛异常，就代表发送成功，但是发送成功会有多个状态，在sendResult里定义。

SEND_OK:消息发送成功；

FLUSH_DISK_TIMEOUT:消息发送成功，但是服务器刷盘超时，消息已经进入服务器队列，只有此时服务器宕机，消息才会丢失；

FLUSH_SLAVE_TIMEOUT：消息发送成功，但是服务器同步到slave时超时，消息已经进入服务器队列，只有此次服务器宕机，消息才会丢失；

SLAVE_NOT_AVAILABLE:消息发送成功，但是此时slave不可用，消息已经进入服务器队列，只有此时服务器宕机，消息才会丢失；

### 4 Oneway方式发送消息

一个RPC调用，通常是这样的一个过程：

1、客户端发送请求到服务器；

2、服务器处理请求；

3、服务器向客户端返回应答；

所以一个RPC的耗时时间是上述三个步骤的总和，而某些场景要求耗时非常短，但是对可靠性要求并不高，例如日志收集类应用，此类应用可以采用oneway形式调用，oneway形式只发送请求不等待应答，而发送请求在客户端实现层面仅仅一个OS系统调用的开销，即将数据写入客户端的socket缓冲区，此过程耗时通常在微秒级。