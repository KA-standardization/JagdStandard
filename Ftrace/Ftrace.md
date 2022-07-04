# 1.Tracers List

> **设置追踪器**
>
> echo tracers >  current_tracer

| tracers        |                                                              |                                                              |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| function       | Function call tracer to trace all kernel functions.          | 跟踪所有内核函数的函数调用跟踪器。                           |
| function_graph | Similar to the function tracer except that the function tracer probes the functions on their entry  whereas the function graph tracer traces on both entry  and exit of the functions. It then provides the ability 	to draw a graph of function calls similar to C code source. | 类似于函数跟踪器，除了函数跟踪器探测函数的入口而函数图跟踪器跟踪两个入口然后退出函数。然后它提供能力绘制类似于C代码的函数调用图源 |
| blk            | The block tracer. The tracer used by the blktrace user application. | 块跟踪。blktrace用户应用程序使用的跟踪程序。                 |
| hwlat          | The Hardware Latency tracer is used to detect if the hardware produces any latency. See "Hardware Latency Detector" section below. | 硬件延迟跟踪程序用于检测硬件是否产生任何延迟。请参阅下面的“硬件延迟检测器”一节。 |
| irqsoff        | Traces the areas that disable interrupts and saves the trace with the longest max latency.  See tracing_max_latency.  When a new max is recorded, it replaces the old trace.  It is best to view this trace with the latency-format option enabled, which happens automatically when the tracer is selected. | 跟踪禁用中断的区域，并保存最大延迟最长的跟踪。看到tracing_max_latency。当记录一个新的最大值时，它会替换旧的跟踪。最好在启用延迟格式选项的情况下查看此跟踪，该选项在选择跟踪程序时自动发生。 |
| preemptoff     | Similar to irqsoff but traces and records the amount of time for which preemption is disabled. | 类似于irqsoff，但是跟踪和记录禁用抢占的时间。                |
| preemptirqsoff | Similar to irqsoff and preemptoff, but traces and records the largest time for which irqs and/or preemption is disabled. | 类似于irqsoff和preemptoff，但是跟踪和记录禁用irqs和/或抢占的最长时间。 |
| wakeup         | Traces and records the max latency that it takes for the highest priority task to get scheduled after it has been woken up. Traces all tasks as an average developer would expect. | 跟踪并记录在唤醒最高优先级任务后调度该任务所需的最大延迟时间。像一般开发人员所期望的那样跟踪所有任务。 |
| wakeup_rt      | Traces and records the max latency that it takes for just RT tasks (as the current "wakeup" does). This is useful for those interested in wake up timings of RT tasks. | 跟踪并记录仅RT任务所需的最大延迟时间(正如当前的“唤醒”所做的那样)。这对于那些对RT任务的唤醒时间感兴趣的人很有用。 |
| wakeup_dl      | Traces and records the max latency that it takes for a SCHED_DEADLINE task to be woken (as the "wakeup" and "wakeup_rt" does). | 跟踪并记录唤醒SCHED_DEADLINE任务所需的最大延迟时间(就像“wakeup”和“wakeup_rt”所做的那样)。 |
| mmiotrace      | A special tracer that is used to trace binary module. It will trace all the calls that a module makes to the hardware. Everything it writes and reads from the I/O as well. | 用于跟踪二进制模块的特殊跟踪器。它将跟踪模块对硬件的所有调用。它从I/O写入和读取的所有内容。 |
| branch         | This tracer can be configured when tracing likely/unlikely calls within the kernel. It will trace when a likely and unlikely branch is hit and if it was correct in its prediction of being correct. | 可以在跟踪内核中可能/不可能的调用时配置此跟踪程序。它将跟踪一个可能的和不可能的分支何时被击中，以及它的预测是否正确。 |
| nop            | This is the "trace nothing" tracer. To remove all tracers from tracing simply echo "nop" into current_tracer. | 这就是“无迹”追踪器。要从跟踪中移除所有跟踪器，只需将"nop"回显到current_tracer中。 |

# 2.Graph Function

> **设置追踪函数** : 产生函数调用堆栈
>
> echo netif_receive_skb > set_graph_function  
>
> echo do_sys_call > set_graph_notrace 禁用函数调用堆栈

# 3.Event Tracing

> ```
> echo sched_wakeup > set_event
> echo '!sched_wakeup' > set_event
> ```





# Ex.

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

```
https://www.kernel.org/doc/Documentation/trace/events.txt
https://www.kernel.org/doc/Documentation/trace/ftrace.txt
```

```
# 临时设置
sysctl -w xxxx=1
# cha'kan
sysctl -n xxxx
```
