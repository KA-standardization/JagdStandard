# 10.网络

> 潜在的阻塞
>
> 固有的复杂性

> 网络接口: 网络连接的操作系统端点, 它是系统管理员可以配置和管理的抽象层.

> 包的大小通常受限于网络接口的最大传输单元(MTU)的大小,在许多以太网中将它设置为1500字节

### 延时

#### 连接延时

> TCP SYN包在队列已满的情况下会被服务器丢弃, 导致客户机重新发送基于定时器的SYN传输, 由于发生在TCP握手阶段,连接延时包括重传延时,所以会增加1秒或更多.

#### 首字节延时

> 第一字节到达时间(TTFB), 首字节延时是从建立连接到接收到第一个字节数据所需的时间. 这包括远程主机接受连接, 调度提供服务的线程, 并且执行线程以及发送第一个字节所需的时间
>
> 首字节延时包括目标服务器的处理时间, 这可能包括当服务器过载时需要时间处理请求(例如TCP积压队列)及调度服务器(CPU队列处理延时)造成的延时

#### 往返时间

> 往返时间(RTT)描述了一个网络请求在端点之间进行往返所需的时间. 这包括信号传播时间和每一跳网络的处理时间. 每一跳网络的处理时间的目的是为了确定网络的延时,所以在理想情况下,RTT是由请求和回复数据包在网络上花费的时间主导的(而不是远程主机为请求提供服务的时间), ICMP的echo请求的RTT, 因为远程主机的处理时间是最少的.

#### 连接生命周期

> 连接生命周期指一个网络连接从建立到关闭所需的时间, 一些协议支持长连接策略,因而之后的操作可以利用现有的连接, 进而避免这种系统开销以及建立连接(和建立TLS)的延时.

### 缓冲
