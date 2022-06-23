![](L:\Developer\JagdStandard\UNIX\Linux Kernel\imgs\nets\Linux Tracing Tech-Stack.PNG)

```
静态探针(埋点): 是指事先在代码中定义好,并编译到应用程序或者内核中的探针 
	跟踪点(tracepoints)
		 printk
		 kernel function
		 kernel trace event
		 	# 数据链路层(网卡)到达TCP/IP处理的第一个函数
		 	int netif_receive_skb(struct sk_buff *skb)
		 	{
		 		int ret;
		 		trace_netif_receive_skb_entry(skb);
		 		ret = netif_receive_skb_internal(skb);
		 		trace_netif_receive_skb_exit(ret);
		 		return ret;
		 	}
	USDT探针(User Statically-Defined Tracing)
```

```
Tracing Frameworks
	ftrace 
		可消费的事件源: tracepoints, kprobes, uprobes
		依赖debugfd
	perf_event
		可消费的事件源: tracepoints, kprobes, uprobes
		可以完成ftrace的大部分功能,但是不能做函数遍历,比ftrace更安全,支持采样,支持自定义动态事件
	eBPF
		BPF是一个内核虚拟机,可在events上高效运行programs,支持事件追踪
		前端工具
			bcc: 编写代码
			bpftrace: 配置
	SystemTap
		自己写脚本,由stap编译为驱动并插入内核,不太安全
	sysdig
		使用类似tcpdump的语法和lua后处理操作系统调用事件,
		还可以通过eBPF来进行扩展,所以,也可以用来追踪内核中
```

```
ftrace
cd /sys/kernel/debug/tracing
	mount -t debugfs nodev /sys/kernel/debug
cat available_tracers
	function #表示跟踪函数的执行
	function_graph #跟踪函数的调用关系
cat available_filter_functions # 查看内核函数

cat available_events # 查看事件

echo netif_receive_skb > set_graph_function # 设置追踪函数

echo function_graph > current_tracer #设置追踪器
echo funcgraph-proc > trace_options

echo 1 > tracing_on # 开启追踪

echo 0 > tracing_on # 停止追踪

cat trace # 结果
```



```
tar -Jxf linux-3.12.tar.xz
drivers/net/tun.c netif_receive_skb
```

