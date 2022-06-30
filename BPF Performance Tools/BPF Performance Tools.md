# 1.引言

> https://github.com/iovisor

```
vim /etc/ssh/sshd_config 
vim /etc/ssh/ssh_config 
		PasswordAuthentication yes
		PermitRootLogin prohibit-password yes
service ssh restart
```

### BCC

```
sudo apt-get install arping bison clang-format cmake dh-python \
  dpkg-dev pkg-kde-tools ethtool flex inetutils-ping iperf \
  libbpf-dev libclang-dev libclang-cpp-dev libedit-dev libelf-dev \
  libfl-dev libzip-dev linux-libc-dev llvm-dev libluajit-5.1-dev \
  luajit python3-netaddr python3-pyroute2 python3-distutils python3
git clone https://github.com/iovisor/bcc.git
mkdir bcc/build; cd bcc/build
cmake ..
make
make install
```



```
execsnoop -t
biolatency -m
# 显示失败的open系统调用
opensnoop -x 
```

### bpftrace

```
apt-get install -y \
  bison \
  cmake \
  flex \
  g++ \
  git \
  libelf-dev \
  zlib1g-dev \
  libfl-dev \
  systemtap-sdt-dev \
  binutils-dev \
  libcereal-dev \
  llvm-14-dev \
  llvm-14-runtime \
  libclang-14-dev \
  clang-14 \
  libgtest-dev \
  libgmock-dev \
  asciidoctor
  
git clone https://github.com/iovisor/bpftrace
mkdir bpftrace/build; cd bpftrace/build;
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j8
sudo make install
```



```
bpftrace -l 'tracepoint:syscalls:sys_enter_open*'
bpftrace -e 'tracepoint:syscalls:sys_enter_open* {@[probe]=count();}'
bpftrace -e 'tracepoint:syscalls:sys_enter_open* {printf("%s %s\n",comm,str(args));}'
```

# 2.技术背景

### bpftool: 使用BPF查看指令集

> bpftppl: 查看操作BPF对象

```
└─# bpftool       
Usage: bpftool [OPTIONS] OBJECT { COMMAND | help }
       bpftool batch file FILE
       bpftool version

       OBJECT := { prog | map | link | cgroup | perf | net | feature | btf | gen | struct_ops | iter }
       OPTIONS := { {-j|--json} [{-p|--pretty}] | {-d|--debug} |
                    {-V|--version} }
# perf prog 子命令可以用来查找和打印跟踪程序
```

```
bpftool perf: 显示哪些BPF程序正通过perf_event_open()进行挂载
bpftool prog show
bpftool prog dump xlated id 22 # dump打印 xlated将BPF指令翻译为汇编指令打印出来
bpftool prog dump xlated id 25 linum # 包含了BPF信息,linum修饰符在输出中增加源代码文件和行信息
bpftool prog dump xlated id 25 opcodes # opcodes修饰符可以在输出中包含BPF指令的opcode
bpftool prog dump xlated id 25 visual > bio_.dot # visual修饰符可以以DOT格式输出控制流信息 #GraphViz
	dot -Tpng -Elen=2.5 bio_.dot -o bio.png
	# 生成的PNG图片可以看到指令的流向
	# GraphViz布局工具
			dot
			neato
			fdp
			sfdp
			osage
bpftool prog dump jited id 528 # jited子命令显示了经过JIT编译之后的机器码
```

```
bpftool btf dump id 1 # 显示BTF中类型和结构体信息
```

> BPF系统调用命令
>
> ​	strace -ebpf execsnoop

| Bpf_cmd              | 描述                                                         |
| -------------------- | ------------------------------------------------------------ |
| BPF_MAP_CREATE       | 创建一个BPF映射表: 一个灵活的存储对象,可用作key/value方式的哈希表(关联数组) |
| BPF_MAP_LOOKUP_ELEM  | 使用key查找元素                                              |
| BPF_MAP_UPDATE_ELEM  | 根据key更新相应元素                                          |
| BPF_MAP_DELETE_ELEM  | 根据key删除相应元素                                          |
| BPF_MAP_GET_NEXT_KEY | 遍历映射表中全部key                                          |
| BPF_PROG_LOAD        | 验证并加载BPF程序                                            |
| BPF_PROG_ATTACH      | 将BPF程序挂载到某一事件上                                    |
| BPF_PROG_DETACH      | 将BPF程序从某个事件卸载                                      |
| BPF_OBJ_PIN          | 在/sys/fs/bpf下创建一个BPF对象实例                           |

> BPF程序类型

| Bpf_prog_type                | 描述                                         |
| ---------------------------- | -------------------------------------------- |
| BPF_PROG_TYPE_KPROBE         | 用于内核动态插桩kprobes和用户动态插桩uprobes |
| BPF_PROG_TYPE_TRACEPOINT     | 用于内核静态跟踪点                           |
| BPF_PROG_TYPE_PERF_EVENT     | 用于perf_events,包括PMC                      |
| BPF_PROG_TYPE_RAW_TRACEPOINT | 用于跟踪点,不处理参数                        |
| BPF_PROG_TYPE_SOCKET_FILTER  | 用于挂载到网络套接字上                       |
| BPF_PROG_TYPE_SCHED_CLS      | 用于流量控制分类                             |
| BPF_PROG_TYPE_XDP            | 用于XDP(eXpress Data Path)程序               |
| BPF_PROG_TYPE_CGROUP_SKB     | 用于cgroup包过滤                             |

> BPF映射表类型

| Bpf_map_type                  | 描述                                                       |
| ----------------------------- | ---------------------------------------------------------- |
| BPF_MAP_TYPE_HASH             | 基于哈希表的映射表类型: 保存key/value对                    |
| BPF_MAP_TYPE_ARRAY            | 数组类型                                                   |
| BPF_MAP_TYPE_PERF_EVENT_ARRAY | 到perf_events环形缓冲区的接口,用于将跟踪记录发送到用户空间 |
| BPF_MAP_TYPE_PERCPU_HASH      | 一个基于每个CPU单独维护的更快哈希表                        |
| BPF_MAP_TYPE_PERCPU_ARRAY     | 一个基于每个CPU单独维护的更快数组                          |
| BPF_MAP_TYPE_STACK_TRACE      | 调用栈储存,使用栈ID进行索引                                |
| BPF_MAP_TYPE_STACK            | 调用栈储存                                                 |

