# 1.数据包分析技术与网络基础

> Tcpdump是一个命令行程序
>
> Wireshark和OmniPeekd拥有图形用户界面（GUI）

### 数据包嗅探工作过程

```
1.收集，数据包嗅探从网络电缆上收集原始的二进制数据
	网卡设置为混杂模式，将抓取一个网段上的所有网络通信流量
2.转换，将捕获的二进制数据转换成可读形式
3.分析，对捕获和转换后的数据作为输入，识别并验证他们的协议，然后开始分析每个协议的特定属性
```

### 协议

> 协议栈是由一组协同工作网络协议的逻辑组合而成

```
常见的网络协议
传输控制协议TCP
互联网协议IP
地址解析协议ARP
动态主机配置协议DHCP
```

### 七层OSI参考模型

> 标准号为ISO7498
>
> 美国国防部（DoD）的网络模型，也被称为TCP/IP模型
>
> >OSI模型中的每层都只能直接与它的上层或下层协议通信

| 数据6page | 应用层（实际程序）           | HTTP SMTP FTP Telnet              |
| :-------- | ---------------------------- | --------------------------------- |
| 数据      | 表示层                       | ASCII MPEG JPEG MIDI              |
| 数据      | 会话层                       | NetBIOS SAP SDP NWlink            |
| 数据段    | 传输层                       | TCP UDP SPX                       |
| 数据包    | 网络层                       | IP IPX                            |
| 帧        | 数据链路层                   | Ethernet TokenRing FDDI AppleTalk |
| 比特      | 物理层（实际的网络数据传播） |                                   |

### 数据封装

> 协议栈中的每层协议都负责在传输数据上增加一个协议头部或尾部，其中包含使协议栈之间能够进行通信的额外信息
>
> 数据封装过程将创建一个协议数据单元（PDU）
>
> 抱文来表示一个完整或部分PDU，该PDU从多个OSI参考层中包含了表头和表尾信息

```
应用层协议发出指令后，数据包中的应用层数据将沿着OSI参考模型的协议栈传递给传输层，HTTP是一个使用TCP（或在TCP协议之上）的应用层协议，因此传输层将使用TCP协议来确保数据包的可靠投递，一个包括序列号和其他数据的TCP协议头部将被创建，并添加到PDU中。
TCP协议将数据包交给IP协议（负责为数据包进行逻辑寻址的协议），IP协议将创建一个包含有逻辑寻址信息的头部，并将数据包传递给数据链路层上的以太网协议，然后以太网物理地址会被添加并存储在以太网帧头中。
数据包以完全组装好并传递给物理层，在这里数据包通过0，1信号完成通过网络的传输。
```

# 2.监听网络线路

### 混杂模式

> 混杂模式驱动网卡：一种允许网卡查看所有流经网络线路数据包的驱动模式

> ARP协议：用来给定IP地址解析MAC地址
>
> > 有些网络流量并非是发送指定目标地址，为了找到对应的MAC地址，ARP协议会发送一个广播包发出到广播域中的每一台设备，然后期望正确的客户端将做出回应

> 广播域：一个网络段，是由几台计算机组成，但广播域中仅仅只有一台客户端应该对传输的ARP感兴趣，而一旦网络上的所有计算机都处理和回应ARP广播包的话，网络性能将变的非常糟糕

### 在交换式网络中进行嗅探

###### 端口镜像

> 为了使用端口镜像，必须能够通过WEB或命令行来访问目标设备所连接的交换机，此外这台交换机还必须支持端口镜像功能，并且有一个空闲端口，可以插入嗅探设备

```
要启用端口镜像，需要发送一个命令，强制交换机将一个端口上的所有通信都镜像到另一端口上
```

| 设备 | CMD                                                          |
| ---- | ------------------------------------------------------------ |
| 思科 | set span <source port> <destination port>                    |
| 凯创 | set port mirroring create <source port> <destination port>   |
| 北电 | port-mirroring mode mirror-port <source port> monitor-port <destination port> |

> 当流经端口的流量远远超出一个单独端口的物理承受能力，将可能会导致数据包丢失，甚至网络速度变慢。在这种情况下，交换机会丢弃所有多余的数据包，或者甚至暂停内部交换电路，从而造成通信中断的情况。

###### ARP缓存污染

```
# 查看本地ARP缓存
arp -n 
cat /proc/net/arp

# http://nmap.org
# 扫描开放端口
nmap -PS 10.0.17.100
nmap -T4 -A -v 10.0.17.100
# 扫描网段存活主机
nmap -sP 10.0.0.0/16
# 查找网段开放的指定端口
nmap -sS 10.0.17.100-200 -p 15672
# 探测端口段
nmap -sV 10.0.17.104 -p 10000-20000
# 对应网段计算机的MAC地址输出到文件 -oM输出到控制台
nmap -sP -PI -PT -oN ipandmaclist.txt 10.0.17.0/24
# 扫描端口
nmap -sC -sV -oA 8-200
```

> ARP查询过程
>
> > 第3层寻址方案称为IP寻址系统，网络上所有设备相互通信时在第3层上均使用IP地址。由于交换机在OSI模型的第2层上工作，它只识别第2层上的MAC地址，因此网络设备必须在他们创建的数据包中包含这些信息。当这些设备不知道对方的MAC地址时，必须要通知已知的第3层IP地址来进行查询，这样才可能通过交换机将流量传递给相应设备。
> >
> > 这些翻译过程就是通过第二层上的ARP协议来实施的，链接到以太网网络上的计算机的ARP查询过程，是从一台计算机想要与另一台进行通信时开始的。发起通信的计算机首先检查自己的ARP缓存，查看它是否已经有对方IP地址对应的MAC地址。如果不存在，它将往数据链路层广播地址FF：FF：FF：FF：FF发送一个ARP广播请求包，作为一个广播数据包，他会被这个特定的以太网广播域上的每台计算机接收。没有匹配到目标IP地址的计算机会简单地选择丢弃这个请求包，而目标计算机选择答复这个请求数据包，通过ARP应答告知它的MAC地址，发起通信的计算机获取到了数据链路层的寻址信息，便可以与远端计算机进行通信，同时将这些信息保存在ARP缓存中，来加速以后的网络访问。

> ARP缓存污染工作过程
>
> > 通过发送包含虚假MAC地址（第2层）的ARP消息，来劫持其他计算机的流量。

# 4.玩转捕获数据包

> Ctrl+F打开find packet, Ctrl+N \ Ctrl+B
>
> > Display filter: 允许通过表达式筛选
> >
> > > Ex: not ip, ip.addr==192.168.0.1, arp
> >
> > Hex Value: 允许通过十六进制，对数据包进行搜索
> >
> > > 00:ff, ff:ff, 00:aa:b1:ff
> >
> > String: 允许通过字符串进行搜索
> >
> > > Workstation, User, Domain

> Ctrl+M标记数据包, Shift+Ctrl+N \ Shift+Ctrl+B
>
> Ctrl+T数据包相对时间参考
>
> Shift+Ctrl+T时间偏移

### 捕获过滤器

> 捕获过滤器应用于libpcap\WinPcap,并使用Berkeley Packet Filter
>
> 使用BPF语法创建的过滤器被称为expression,并且每个表达式包含一个或多个primitive(原语).每个原语包含一个或多个qualifiers(限定词),然后跟着一个ID名字或者数字.
>
> 三种逻辑运算符,对原语进行组合 &&与, ||或, !非
>
> > src host 192.168.0.11 && port 80
> >
> > 对原地址192.168.0.11并且目标端口80的流量进行捕获

| qualifiers | 说明                                 | EX.                            |
| ---------- | ------------------------------------ | ------------------------------ |
| Type       | 指出名字或数字所代表的意义           | host, net, port                |
| Dir        | 指明传输方向是前往还是来自名字或数字 | src, dst                       |
| Proto      | 限定所要匹配的协议                   | Ether, ip, tcp, udp, http, ftp |

| Ex.                              | 说明                                                         |
| -------------------------------- | ------------------------------------------------------------ |
| host 192.168.0.11                | IPv4地址相关流量                                             |
| host 2022:db8:886e:8abc:322:7777 | IPv6地址相关流量                                             |
| host master_1                    | 设备主机名                                                   |
| ether host 00-11-22-33-44-55     | MAC地址相关流量                                              |
| src host 192.168.0.11            | 原                                                           |
| dst host 192.168.0.11            | 目标                                                         |
| dst 192.168.0.11                 | 如果在原语中没有指定一种类型限定符(host, net, port), host限定词将作为默认选择 |
| port 8888                        | 捕获端口8888的流量                                           |
| !port 8888                       | 除端口8888的流量                                             |
| dst port 80                      | 捕获访问标准HTTP80端口的WEB服务器                            |
| icmp                             | ICMP流量                                                     |
| !ip6                             | 除IPv6外的流量                                               |

#### 协议过滤器

> BPF语法允许通过检查协议头中的每一个字节来创建基于那些数据的特殊过滤器
>
> > EX.: 基于ICMP过滤器的类型域进行过滤,而类型域位于数据包的最开头也就是偏移量为0的位置,可以通过在协议限定符后输入由方括号括起的字节偏移量. icmp[0]==3
> >
> > EX.: 仅检查代表echo请求(类型8)或echo回复(类型0)的ICMP数据包. icmp[0]==8||icmp[0]=0
>
> 可以在方括号中偏移值得后面以冒号分隔加上一个字节长度，来指定返回给过滤器表达式的数据长度
>
> > EX.: 创建一个过滤器捕获所有ICMP目标---不可访问, 主机不可达的数据包(类型3,代码1).这些是1字节的字段,他们与偏移量为0的数据包头部相邻.检查从数据包头部的偏移量0处开始的2字节数据,并与十六进制值0x0301(类型3,代码1)进行比较. Icmp[0:2]==0x0301
>
> 只捕获带有RST标志的TCP数据包,TCP数据包标志位在偏移为13字节的地方,虽然整个标志位加在一起是1字节,但是这个字节中每一比特位都是一个标志.在一个TCP数据包中,多个标志可被同时设置,因此多个值可能都代表RST位被设置,不能通过一个tcp[13]的值来进行有效过滤,我们必须通过当前原语中加人一个单一的&符号,来指定这个字节中检查的比特位置
>
> > EX.: 在这个字节中RST标志额比特位代表数字4. tcp[13]&4==4
> >
> > 所有都被设置PSH标志(比特位代表数字8)的数据包. tcp[13]&8==8

| 过滤器                                  | 说明                      |
| --------------------------------------- | ------------------------- |
| tcp[13]&32==32                          | 设置URG位的TCP数据包      |
| tcp[13]&                                | 设置了ACK位的TCP数据包    |
| tcp[13]&8==8                            | 设置了PSH位的TCP数据包    |
| tcp[13]&4==4                            | 设置了RST位的TCP数据包    |
| tcp[13]&2==2                            | 设置了SYN位的TCP数据包    |
| tcp[13]&1==1                            | 设置了FIN位的TCP数据包    |
| tcp[13]==18                             | TCP-SYN-ACK数据包         |
| tcp[((tcp[12:1]&0xf0)>>2):4]=0x504f5354 | POST                      |
| tcp[((tcp[12:1]&0xf0)>>2):4]=0x47455420 | GET                       |
| ether host 00:00:00:00:00:00            | 流入流出MAC地址的流量     |
| !ether host 00:00:00:00:00:00           | 不流入流出MAC地址的流量   |
| broadcast                               | 广播流量                  |
| icmp                                    | ICMP流量                  |
| icmp[0:2]                               | ICMP目标不可达,主机不可达 |
| ip                                      | IPv4流量                  |
| ip6                                     | IPv6流量                  |
| udp                                     | UDP流量                   |

### 显示过滤器

> 语法模式以具体协议为中心并且遵从protocol.feature.subfeature的格式
>
> 保存过滤器规则Capture->Capture Filters->+

| 过滤器                                         | 说明                         |
| ---------------------------------------------- | ---------------------------- |
| frame.len<=128                                 | 长度小于128字节的数据包      |
| ip.addr==192.168.0.11 or ip.addr==192.168.0.12 | 只显示这两个IP地址的数据包   |
| !tcp.port==3389                                | 排除RDP流量                  |
| tcp.flags.syn==1                               | 具有SYN标志位的TCP数据包     |
| tcp.flags.rst==1                               | 具有RST标志位的TCP数据包     |
| !arp                                           | 排除ARP流量                  |
| http                                           | 所有HTTP流量                 |
| tcp.port==23\|\|tcp.port==21                   | 文本管理流量(Telent或FTP)    |
| smtp\|\|pop\|\|imap                            | 文本email流量(SMTP,POP,IMAP) |

# 5.Wireshark高级特性

### WHOIS

> ARIN: https://www.arin.net 美国互联网号码注册中心
>
> AfriNIC: https://afrinic.net 非洲互联网络信息中心
>
> RIPE: https://www.ripe.net 世界互联网组织(负责欧洲)
>
> APNIC: https://www.apnic.net 亚太互联网信息中心

### 解析器源代码

> https://gitlab.com/wireshark/wireshark/-/tree/master/epan/dissectors

### 流

> Follow TLS Stream

#### Chrome

> chrome://flags
>
> chrome://settings/security?search=%E8%AF%81%E4%B9%A6

# 6.用命令行分析数据包

### tshark&tcpdump

```
# 打印网卡信息
tshark -D
ifconfig
# 选择网卡
tshark -i 1
tcpdump -i eth0
# 保存为文件并限制抓取条数
tshark -i 1 -w packet.pcap -c100
tcpdump -i eth0 -w packet.pcap -c100
# 回读数据包限制条数
tshark -r packet.pcap -c100
tcpdump -r packet.pcap -c100
# 增加冗余
tshark -r packet.pcap -V -c100
tcpdump -r packet.pcap -vvv
# 以ASCII或16进制的形式查看数据包
tshark -r -x packet.pcap
tcpdump -Xr packet.pcap
tcpdump -xr packet.pcap # 只查看16进制输出
tcpdump -Ar packet.pcap # 只输出ASCII形式
# 禁用名称解析
tshark -ni 1
tshark -i 1 -Ntm
	m: MAC地址解析
	n: 网络地址解析
	t: 传输层(端口服务名称)解析
	N: 使用外网解析服务
	C: 使用当前DNS解析
tcpdump -nni eth0 #-n会禁用IP名称解析 -nn会禁用端口服务解析
```

```
应用过滤器
# -f参数来应用捕获过滤器 ""内遵从BPF语法
tshark -ni 1 -w packet.pcap -f "tcp port 80"
tshark -i 7 -w Jagd-24-7-T.pcap -f "tcp dst port 5601 and dst 10.0.24.100 and (tcp[((tcp[12:1]&0xf0)>>2):4])=0x504f5354"
tcpdump -nni eth0 -w packet.pcap 'tcp port 80' # ''里构造过滤表达式
tcpdump -nni eth0 -F dns_filter.bpf # BPF过滤文件
# -Y参数来应用显示过滤器 ""内使用Wireshark语法
tshark -ni 1 -w packet.pcap -Y "tcp.dstport==80"
# 显示符合过滤表达式的包
tshark -r packet.pcap -Y "tcp.dstport==80"
tcpdump -r packet.pcap 'tcp dst port 80'
# 分包
tcpdump -r packet.pcap 'tcp dst port 80' -w packet2.pcap
# 打印出使用过滤表达式的BPF指令
tcpdump  -d -r t1.pcap 'host 10.0.17.200'
```

```
# 显示绝对时间
tshark -r packet.pcap -t ad
	a:绝对时间
	ad:带日期的绝对时间
	d:自前捕获数据包的增量
	dd:
	e:亿元时间
	r:第一个数据包和当前数据包之间时间差
	u:UTC时间
	ud:带日期的UTC时间
```

```
统计
# 查看所有可用统计
tshark -z help
# 显示每个IP地址并统计每个IP地址在所占流量的比率
tshark -r packet.pcap -z ip_hosts,tree
# 分层级统计在捕获文件中找到的所有协议
tshark -r packet.pcap -z io,phs
# 显示关于HTTP请求和回应的统计
tshark -r packet.pcap -z http,tree
# 显示每个HTTP请求的统计
tshark -r packet.pcap -z http_req,tree
# 显示关于Windows会话的SMB命令的统计
tshark -r packet.pcap -z smb,srt
# 显示无线端点
tshark -r packet.pcap -z endpoints,wlan
# 从捕获中显示专家信息(对话,错误)
tshark -r packet.pcap -z expert
# 有关IP会话的信息的统计图表
tshark -r packet.pcap -z conv,ip
# 跟随TCP流 指明流的类型,输出模式,想要显示的流
tshark -r packet.pcap -z follow,tcp,ascii,0
```

# 7.网络层协议

### ARP(Address Resolution Protocol地址解析协议)

> 在已知远程主机的IP地址创建通信应用,也就意味着系统已经拥有了所有其需要的信息,用来构建它想要在第3层到第7层中传递的数据包.
>
> 这时它所需的唯一信息就是第2层包含有目标主机MAC地址的数据链路层数据,之所以需要MAC地址,是因为网络中用于连接各个设备的交换机使用了内容寻址寄存器(CAM),这个表列出它在每一个端口的所有连接设备的MAC地址.当交换机收到了一个指向特定MAC地址的流量时,它会使用这个表来确定应该使用哪一个端口发送流量.如果MAC地址是未知的,则这个传输设备会首先在它的缓存中查找这个地址.如果没有找到,那这个地址就需要在网络上进行额外的通信来进行解析了.
>
> TCP/IP网络(IPv4)中用来将IP地址解析为MAC地址的过程称为地址解析协议,它的解析过程只使用两种数据包: ARP请求,ARP响应. 
>
> 122

### 互联网协议第4版(IPv4)

> IPv4地址是一个32位的地址,用来唯一标识连接到网络中的设备.
>
> 每个IP地址都包含两部分: 网络地址,主机地址

> 网络掩码(network mask)/子网掩码(subnet mask): 用来决定IP地址哪部分属于网络,哪部分属于主机

```
IP: 10.10.1.22
network mask: 255.255.0.0
	10      .10      .1       .22      
	00001010 00001010 00000001 00010110
	255     .255     .0       .0
	11111111 11111111 00000000 00000000
	网络地址network    主机地址host
CIDR: 无类型域间选路(Classless Inter-Domain Routing)
	10.0.1.22/16
```

> IP分片
>
> 一个数据包的分片主要基于第2层数据链路协议所使用的最大传输单元(maximum transmission unit,MTU)的大小.(MTU可以手工设定)
>
> 在多数情况下,第2层所使用的数据链路协议是以太网,以太网的默认MTU是1500字节,最大报文大小是1500字节(并不包括14字节的以太网头本身)

```
数据包分片
1. 设备将数据分为若干个将要接下来进行传输的数据包
2. 每个IP头的总长度字段会被设置为每个分片的片段长度
3. 除了最后一个分片数据包外,之前所有分片数据包的标志位都被设为1
4. IP头中分片部分的分片偏移将会被设置
5. 数据包被发送出去
132
```

### 互联网控制消息协议(Internet Control Message Protocol, ICMP)

> 互联网控制消息协议是TCP/IP协议族中的一个功能协议,负责提供在TCP/IP网络上的设备,服务,路由器可用性的信息

```
ping 10.0.17.100
数据包的类型8,代码0: echo请求
数据包的类型0,代码0: echo响应
数据包的类型11,代码0: 数据包的TTL在传输过程中超时,目的不可达
```

> 路由跟踪

```
tracert 10.0.17.100
```

# 8.传输层协议

### 传输控制协议(Transmission Control Protocol, TCP)

> TCP报头 152
>
> ​	序号(sequence number): 这个数字用来表示一个TCP片段,这个域用来保证数据流中的部分没有缺失
>
> ​	确认号(acknowledgment number): 这个数字是通信中希望从另一个设备中得到的下一个数据包的序号
>
> ​	标志(flags): 
>
> ​	窗口大小(window size): TCP接收者缓冲的字节大小

> TCP端口 使用TCP通信时,我们有65535个端口可供使用
>
> 1-1023: 标准端口组
>
> 1024-65535: 临时端口组

### 用户数据报协议(User Datagram Protocol, UDP)

> 161

# 9.常见高层网络协议

### 动态主机配置协议(Dynamic Host Configuration Protocol)

> 164

| 类型号 | 消息类型 | 描述                                             |
| ------ | -------- | ------------------------------------------------ |
| 1      | 发现     | 客户端用来定位可用的DHCP服务器                   |
| 2      | 提供     | 服务器用来给客户端发送发现数据包的响应           |
| 3      | 请求     | 客户端用来请求服务器所提供的参数                 |
| 4      | 拒绝     | 客户端向服务器指明数据包的无效参数               |
| 5      | ACK      | 服务器向客户端发送所请求的配置参数               |
| 6      | NAK      | 客户端向服务器拒绝其配置参数的请求               |
| 7      | 释放     | 客户端向服务器通过取消配置参数来取消租约         |
| 8      | 通知     | 当客户端已经有IP地址时客户端向服务器请求配置参数 |

### 域名系统(Domain Name System, DNS)

#### DNS数据包结构 174

> QR(query/response): 用来指明这个数据包是DNS查询还是响应
>
> OpCode: 用来定义消息中请求的类型
>
> AA(Authoritative Answer): 如果响应数据包中设定了这个值,则说明这个响应是由域内权威域名服务器发出的
>
> TC(Truncation): 用来指明这个响应由于太长,无法装入数据包而被截断
>
> RD(Recursion Desired): DNS客户端在目标域名服务器不含有所请求的信息的情况下,要求进行递归查询
>
> RA(Recursion Available): 域名服务器支持递归查询
>
> ResponseCode: 在DNS响应中用来指明错误

#### DNS问题类型

> DNS查询和响应中所使用的类型域,指明了这个查询或者响应的资源记录类型

| 值   | type  | description    |
| ---- | ----- | -------------- |
| 1    | A     | IPv4主机地址   |
| 2    | NS    | 权威域名服务器 |
| 5    | CNAME | 规范别名       |
| 15   | MX    | 邮件交换       |
| 16   | TXT   | 文本字符串     |
| 28   | AAAA  | IPv6主机地址   |
| 251  | IXFR  | 增量区域传送   |
| 252  | AXFR  | 完整区域传送   |

```
yum -y install bind-utils
dig zhihu.com
```

### 超文本传输协议(Hypertext Transfer Protocol, HTTP)

# 10.基础场景

```
http.request.method=="GET" Statics>HTTP>Requests
每一个会话初始SYN包
tcp.flags.syn==1 && tcp.flags.ack==0
```

# 13.无线网络

```
309
```

