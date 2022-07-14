# 1.功能描述

> 某些内核函数被调用的频率
>
> 什么代码路径会导致这个函数被调用
>
> 这个内核函数调用了哪些子函数
>
> 禁用抢占的代码路径造成的最高延时是多少

>剖析器
>
>> 提供统计摘要
>
>跟踪器
>
>> 提供每个事件的细节

| 剖析器         | 描述               |
| -------------- | ------------------ |
| function       | 内核函数统计分析   |
| kprobe profile | 启用kprobe计数器   |
| uprobe profile | 启用uprobe计数器   |
| hist trigger   | 事件的自定义直方图 |

| 跟踪器         | 描述                                          |
| -------------- | --------------------------------------------- |
| function       | 内核函数调用跟踪器                            |
| tracepoints    | 内核函数静态检测, 事件跟踪器                  |
| kprobes        | 内核函数动态检测, 事件跟踪器                  |
| uprobes        | 用户级动态检测, 事件跟踪器                    |
| function_graph | 内核函数调用跟踪, 通过子调用的层次图展示      |
| wakeup         | 测量CPU调度器的最大延时                       |
| wakeup_rt      | 测量实时(RT)任务的最大CPU调度器延时           |
| irqsoff        | 用代码位置和延时跟踪IRQ关闭事件(中断禁用延时) |
| preemptoff     | 跟踪有代码路径和延时的事件                    |
| preemptirqsoff | 一个结合了irqsoff和preemptoof的跟踪器         |
| blk            | 块I/O跟踪器(被blktrace使用)                   |
| hwlat          | 硬件延时跟踪器: 可以检测外部扰动导致的延时    |
| mmiotrace      | 跟踪一个模块对硬件的调用                      |
| nop            | 一个特殊的跟踪器, 可以禁用其他跟踪器          |

> 需要启用CONFIG_PREEMPTIRQ_EVENTS

# 2.tracefs

> Ftrace功能的接口是tracefs文件系统,挂载在/sys/kernel/tracing

```
mount -t tracefs tracefs /sys/kernel/tracing
# 列出debugfs和tracefs
mount -t debugfs,tracefs
debugfs on /sys/kernel/debug type debugfs (rw,nosuid,nodev,noexec,relatime)
tracefs on /sys/kernel/tracing type tracefs (rw,nosuid,nodev,noexec,relatime)
```

### tracefs内容

| 文件                       | 权限 | 描述                                                |
| -------------------------- | ---- | --------------------------------------------------- |
| available_tracers          | r    | 列出可用的跟踪器                                    |
| current_tracer             | rw   | 显示当前启用的跟踪器                                |
| enabled_functions          | rw   | 启用函数剖析器                                      |
| available_filter_functions | r    | 列出可跟踪的函数                                    |
| set_ftrace_filter          | rw   | 选择要跟踪的函数                                    |
| tracing_on                 | rw   | 启用/禁用输出环形缓冲区开关                         |
| trace                      | rw   | 环形缓冲区                                          |
| trace_pipe                 | r    | 跟踪器的输出,使用跟踪器和块作为输入                 |
| trace_options              | rw   | 用于定制跟踪缓冲区输出的选项                        |
| kprobe_events              | rw   | 启用kprobe配置                                      |
| uprobe_events              | rw   | 启用uprobe配置                                      |
| events                     | rw   | 事件跟踪器的控制文件: tracepoints, kprobes, uprobes |
| options                    |      |                                                     |
| instances                  | rw   | 并发用户的Ftrace实例                                |

```
# 查看当前是否有Ftrace跟踪器在使用
cat /sys/kernel/debug/tracing/current_tracer
```

# 3.Ftrace函数剖析器

> 函数剖析器提供了关于内核函数调用的统计数据
>
> 研究哪些内核函数正在被调用,并确定哪些是最慢的.
>
> 内核选项: CONFIG_FUNCTION_PROFILER=y

```
cat /boot/config-5.16.0-kali7-arm64 |grep "CONFIG_FUNCTION_TRACER\|CONFIG_FUNCTION_GRAPH_TRACER\|CONFIG_STACK_TRACER\|CONFIG_DYNAMIC_FTRACE"
# (hdx,y) x表示硬盘号，y表示分区号
# 使用函数剖析器来统计所有以tcp开头的内核函数
echo 'tcp*' > set_ftrace_filter 
echo 1 > function_profile_enabled 
sleep 5 # 设置剖析器粗略时间
echo 0 > function_profile_enabled 
head 100 trace_stat/function*
echo > set_ftrace_filter
```

```
#!/bin/bash
debugfs=/sys/kernel/debug
echo 1 > $debugfs/tracing/tracing_on
# 如果未设置任何值, 所有的内核函数都会被剖析
echo 'tcp*' > $debugfs/tracing/set_ftrace_filter
echo 1 > $debugfs/tracing/function_profile_enabled
sleep 10
echo 0 > $debugfs/tracing/function_profile_enabled
echo > $debugfs/tracing/set_ftrace_filter
echo 0 > $debugfs/tracing/tracing_on

head 100 /sys/kernel/debug/tracing/trace_stat/function*
Function函数名称                               Hit调用次数    Time函数总时间            Avg平均时间             s^2标准差
  --------                               ---    ----            ---             ---
  tcp_poll                            657807    87747.48 us     0.133 us        12.801 us   
  tcp_stream_memory_free              631866    24538.54 us     0.038 us        0.059 us    
  tcp_v4_rcv                            2207    21914.69 us     9.929 us        142.893 us  
  tcp_v4_do_rcv                         2070    19161.19 us     9.256 us        126.754 us  
  tcp_rcv_established                   1975    16519.24 us     8.364 us        99.751 us   
  tcp_recvmsg                          45377    14630.49 us     0.322 us        0.609 us    
  tcp_send_ack                          1205    11527.30 us     9.566 us        78.634 us   
  tcp_recvmsg_locked                   45377    6891.807 us     0.151 us        0.406 us 
```

# 4.Ftrace函数跟踪

```
#!/bin/bash
debugfs=/sys/kernel/debug
echo 1 > $debugfs/tracing/tracing_on
echo '*sleep' > $debugfs/tracing/set_ftrace_filter
echo function > $debugfs/tracing/current_tracer
sleep 10
# trace文件是跟踪事件缓冲区的一个接口, 读取它会显示缓冲区内容
cat $debugfs/tracing/trace > ~/sleep.log
echo 0 > $debugfs/tracing/tracing_on
# 清除跟踪区缓存, 当current_tracer 设为nop时,跟踪区缓存也会被清除
# > $debugfs/tracing/trace
echo nop > $debugfs/tracing/current_tracer
echo > $debugfs/tracing/set_ftrace_filter

# 名为prlshprint,PID为1152的进程在调用sleep函数
# 最后字段显示当前函数和调用它的父函数, __arm64_sys_clock_nanosleep()被invoke_syscall()调用
#
#                                _-----=> irqs-off
#                               / _----=> need-resched
#                              | / _---=> hardirq/softirq
#                              || / _--=> preempt-depth
#                              ||| /     delay
#           TASK-PID     CPU#  ||||   TIMESTAMP  FUNCTION
#              | |         |   ||||      |         |
      prlshprint-1152    [001] ....  1697.625979: __arm64_sys_clock_nanosleep <-invoke_syscall
      prlshprint-1152    [001] ....  1697.625981: common_nsleep <-__arm64_sys_clock_nanosleep
      prlshprint-1152    [001] ....  1697.625981: hrtimer_nanosleep <-common_nsleep
      prlshprint-1152    [001] ....  1697.625982: do_nanosleep <-hrtimer_nanosleep
     sga.hostcmd-2281    [001] ....  1697.645655: __arm64_sys_clock_nanosleep <-invoke_syscall
     sga.hostcmd-2281    [001] ....  1697.645655: common_nsleep <-__arm64_sys_clock_nanosleep
     sga.hostcmd-2281    [001] ....  1697.645655: hrtimer_nanosleep <-common_nsleep
     sga.hostcmd-2281    [001] ....  1697.645655: do_nanosleep <-hrtimer_nanosleep
           sleep-7310    [001] ....  1697.648985: __arm64_sys_clock_nanosleep <-invoke_syscall
           sleep-7310    [001] ....  1697.648986: common_nsleep <-__arm64_sys_clock_nanosleep
           sleep-7310    [001] ....  1697.648986: hrtimer_nanosleep <-common_nsleep
           sleep-7310    [001] ....  1697.648986: do_nanosleep <-hrtimer_nanosleep
```

> trace_pipe文件是读取跟踪缓冲区的一个不同接口, 从这个文件读取会返回一个无尽事件流, 它使用事件, 所以在读取一次后, 事件就不再位于跟踪缓冲区中了

```
echo 1 > tracing_on
echo '*sleep' > set_ftrace_filter 
echo function > current_tracer 
cat trace_pipe
echo 0 > tracing_on
```

#### Option

> 选项
>
> > 提供定制输出的选项, 可以从trace_options文件或options目录中控制输出

```
# Ex. 禁用flags列
echo 0 > options/irq-info
#           TASK-PID     CPU#     TIMESTAMP  FUNCTION
#              | |         |         |         |
      prlshprint-1152    [001]   2931.727815: __arm64_sys_clock_nanosleep <-invoke_syscall

echo 1 > options/irq-info
#                                _-----=> irqs-off
#                               / _----=> need-resched
#                              | / _---=> hardirq/softirq
#                              || / _--=> preempt-depth
#                              ||| /     delay
#           TASK-PID     CPU#  ||||   TIMESTAMP  FUNCTION
#              | |         |   ||||      |         |
      prlshprint-1152    [001] ....  2931.727815: __arm64_sys_clock_nanosleep <-invoke_syscall
```

> echo print-parent > trace_options

| option             | desc                                                         |                                                              |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| annotate           | It is sometimes confusing when the CPU buffers are full and one CPU buffer had a lot of events recently, thus a shorter time frame, were another CPU may have only had a few events, which lets it have older events. When the trace is reported, it shows the oldest events first,and it may look like only one CPU ran (the one with the oldest events). When the annotate option is set, it will display when a new CPU buffer started | 当CPU缓冲区满了，一个CPU缓冲区最近有很多事件，因此时间更短，而另一个CPU可能只有几个事件，这让它有更早的事件时，有时会令人困惑。当报告跟踪时，它首先显示最老的事件，看起来可能只运行了一个CPU(具有最老事件的CPU)。当设置了annotate选项时，它将在新的CPU缓冲区启动时显示 |
| bin                | This will print out the formats in raw binary.               | 这将打印出原始二进制格式。                                   |
| blk_cgname         |                                                              |                                                              |
| blk_cgroup         |                                                              |                                                              |
| blk_classic        | Shows a more minimalistic output.                            | 显示更简约的输出。                                           |
| block              | When set, reading trace_pipe will not block when polled.     | 当设置该参数时，读取trace_pipe将不会在轮询时阻塞。           |
| context-info       | Show only the event data. Hides the comm, PID, timestamp, CPU, and other useful data. | 只显示事件数据。隐藏通信、PID、时间戳、CPU等有用数据。       |
| disable_on_free    | When the free_buffer is closed, tracing will stop (tracing_on set to 0). | 当free_buffer关闭时，跟踪将停止(tracing_on设置为0)。         |
| display-graph      | When set, the latency tracers (irqsoff, wakeup, etc) will use function graph tracing instead of function tracing. | 当设置延迟跟踪器(irqsoff, wakeup等)时，将使用函数图跟踪而不是函数跟踪。 |
| event-fork         | When set, tasks with PIDs listed in set_event_pid will have the PIDs of their children added to set_event_pid when those tasks fork. Also, when tasks with PIDs in set_event_pid exit, their PIDs will be removed from the file. | 当设置该参数时，在set_event_pid中列出pid的任务将在其子任务分叉时将其pid添加到set_event_pid中。此外，当pid在set_event_pid中的任务退出时，它们的pid将从文件中删除。 |
| funcgraph-abstime  | When set, the timestamp is displayed at each line.           | 设置后，时间戳将显示在每一行。                               |
| funcgraph-cpu      | When set, the CPU number of the CPU where the trace occurred is displayed. | 设置后，将显示跟踪发生的CPU的CPU号。                         |
| funcgraph-duration | At the end of each function (the return) the duration of the amount of time in the function is displayed in microseconds. | 在每个函数(返回)的末尾，函数中时间的持续时间以微秒为单位显示。 |
| funcgraph-irqs     | When disabled, functions that happen inside an interrupt will not be traced. | 当被禁用时，发生在中断内部的函数将不会被跟踪。               |
| funcgraph-overhead | When set, if the function takes longer than A certain amount, then a delay marker is displayed. See "delay" above, under the header description. | 当设置时，如果函数花费的时间超过一定的数量，那么将显示一个延迟标记。参见上面的“延迟”，标题描述下面。 |
| funcgraph-overrun  | When set, the "overrun" of the graph stack is displayed after each function traced. The overrun, is when the stack depth of the calls is greater than what is reserved for each task. Each task has a fixed array of functions to trace in the call graph. If the depth of the calls exceeds that, the function is not traced. The overrun is the number of functions missed due to exceeding this array. | 设置后，图形堆栈的“溢出”显示在每个函数跟踪后。溢出是指调用的堆栈深度大于为每个任务保留的堆栈深度。在调用图中，每个任务都有一个要跟踪的固定函数数组。如果调用的深度超过该值，则不跟踪该函数。溢出是由于超出这个数组而错过的函数的数量。 |
| funcgraph-proc     | Unlike other tracers, the process' command line is not displayed by default, but instead only when a task is traced in and out during a context switch. Enabling this options has the command of each process displayed at every line. | 与其他跟踪程序不同，进程的命令行在默认情况下不会显示，而是只在上下文切换期间进进出出跟踪任务时才会显示。启用此选项将在每行显示每个进程的命令。 |
| funcgraph-tail     | When set, the return event will include the function that it represents. By default this is off, and only a closing curly bracket "}" is displayed for the return of a function. | 设置后，返回事件将包括它所表示的函数。默认情况下，这是关闭的，并且只在函数返回时显示右花括号“}”。 |
| func-no-repeats    |                                                              |                                                              |
| func_stack_trace   | When set, a stack trace is recorded after every function that is recorded. NOTE! Limit the functions that are recorded before enabling this, with "set_ftrace_filter" otherwise the system performance will be critically degraded. Remember to disable this option before clearing the function filter. | 设置后，在记录的每个函数之后记录堆栈跟踪。注意!使用“set_ftrace_filter”限制在启用此功能之前记录的功能，否则系统性能将严重下降。记得在清除函数过滤器之前禁用此选项。 |
| function-fork      | When set, tasks with PIDs listed in set_ftrace_pid will have the PIDs of their children added to set_ftrace_pid when those tasks fork. Also, when tasks with PIDs in set_ftrace_pid exit, their PIDs will be removed from the file. | 当设置该参数时，在set_ftrace_pid中列出pid的任务在其子任务分叉时，其子任务的pid将被添加到set_ftrace_pid中。此外，当pid在set_ftrace_pid中的任务退出时，它们的pid将从文件中删除。 |
| function-trace     | The latency tracers will enable function tracing if this option is enabled (default it is). When it is disabled, the latency tracers do not trace functions. This keeps the overhead of the tracer down 	    when performing latency tests. | 如果这个选项被启用(默认是)，延迟跟踪器将启用函数跟踪。当它被禁用时，延迟跟踪器不会跟踪函数。这将在执行延迟测试时降低跟踪程序的开销。 |
| graph-time         | When running function profiler with function graph tracer, to include the time to call nested functions. When this is not set, the time reported for the function will only include the time the function itself executed for, not the time for functions that it called. | 当使用函数图跟踪器运行函数分析器时，要包括调用嵌套函数的时间。如果不设置此参数，则报告的函数时间将只包括函数本身的执行时间，而不包括它所调用的函数的时间。 |
| hash-ptr           |                                                              |                                                              |
| hex                | Similar to raw, but the numbers will be in a hexadecimal format. | 类似于raw，但数字将采用十六进制格式。                        |
| irq-info           | Shows the interrupt, preempt count, need resched data. When disabled. | 显示中断，抢占计数，需要重新扫描的数据。当禁用。             |
| latency-format     | This option changes the trace output. When it is enabled,the trace displays additional information about the latency, as described in "Latency trace format". | 此选项更改跟踪输出。当它被启用时，跟踪将显示关于延迟的附加信息，如“延迟跟踪格式”中所述。 |
| markers            | When set, the trace_marker is writable (only by root). When disabled, the trace_marker will error with EINVAL on write. | 设置trace_marker时，trace_marker是可写的(仅对root可写)。当禁用时，trace_marker将在写入时发生EINVAL错误。 |
| overwrite          | This controls what happens when the trace buffer is full. If "1" (default), the oldest events are discarded and overwritten. If "0", then the newest events are discarded. | 这将控制跟踪缓冲区满时发生的情况。如果是"1"(默认)，最早的事件将被丢弃并覆盖。如果是“0”，则丢弃最新的事件。 |
| pause-on-trace     |                                                              |                                                              |
| printk-msg-only    | When set, trace_printk()s will only show the format and not their parameters (if trace_bprintk() or trace_bputs() was used to save the trace_printk()). | 设置后，trace_printk()将只显示格式而不显示它们的参数(如果使用trace_bprintk()或trace_bputs()来保存trace_printk())。 |
| print-parent       | On function traces, display the calling (parent) function as well as the function being traced. | 在函数跟踪中，显示调用(父)函数以及被跟踪的函数。             |
| raw                | This will display raw numbers. This option is best for use with user applications that can translate the raw numbers better than having it done in the kernel. | 这将显示原始数字。这个选项最适合用于能够更好地转换原始数字的用户应用程序，而不是在内核中完成。 |
| record-cmd         | When any event or tracer is enabled, a hook is enabled in the sched_switch trace point to fill comm cache with mapped pids and comms. But this may cause some overhead, and if you only care about pids, and not the name of the task, disabling this option can lower the impact of tracing. See "saved_cmdlines". | 当启用任何事件或跟踪程序时，将在sched_switch跟踪点中启用一个钩子，以使用映射的pid和comm填充通信缓存。但这可能会导致一些开销，如果您只关心pid，而不关心任务的名称，禁用此选项可以降低跟踪的影响。看到“saved_cmdlines”。 |
| record-tgid        | When any event or tracer is enabled, a hook is enabled in the sched_switch trace point to fill the cache of mapped Thread Group IDs (TGID) mapping to pids. See "saved_tgids". | 当启用任何事件或跟踪程序时，将在sched_switch跟踪点中启用一个钩子，以填充映射到pid的映射线程组id (TGID)的缓存。看到“saved_tgids”。 |
| sleep-time         | When running function graph tracer, to include the time a task schedules out in its function. When enabled, it will account time the task has been scheduled out as part of the function call. | 在运行函数图跟踪程序时，在其函数中包含任务调度的时间。启用时，它将记录任务已被调度出的时间，作为函数调用的一部分。 |
| stacktrace         | When set, a stack trace is recorded after any trace event is recorded. | 设置后，将在记录任何跟踪事件之后记录堆栈跟踪。               |
| sym-addr           | this will also display the function address as well as the function name | 这还将显示函数地址和函数名                                   |
| sym-offset         | Display not only the function name, but also the offset in the function. For example, instead of 	  seeing just "ktime_get", you will see "ktime_get+0xb/0x20". | 不仅显示函数名，还显示函数中的偏移量。例如，您将看到"ktime_get+0xb/0x20"，而不是只看到"ktime_get"。 |
| sym-userobj        | when user stacktrace are enabled, look up which object the address belongs to, and print a relative address. This is especially useful when ASLR is on, otherwise you don't get a chance to resolve the address to object/file/line after the app is no longer running | 当启用用户堆栈跟踪时，查找该地址属于哪个对象，并打印相对地址。当ASLR打开时，这尤其有用，否则在应用程序不再运行后，你就没有机会将地址解析到object/file/line |
| test_nop_accept    |                                                              |                                                              |
| test_nop_refuse    |                                                              |                                                              |
| trace_printk       | Can disable trace_printk() from writing into the buffer.     | 可以禁用trace_printk()写入缓冲区。                           |
| userstacktrace     | This option changes the trace. It records a stacktrace of the current user space thread after each trace event. | 此选项更改跟踪。它在每个跟踪事件之后记录当前用户空间线程的堆栈跟踪。 |
| verbose            | This deals with the trace file when the latency-format option is enabled. | 这将在启用延迟格式选项时处理跟踪文件。                       |

#### Tracepoint

> 跟踪点
>
> > tracepoint: 是内核的静态检测工具
> >
> > 跟踪点只是内核源代码中的跟踪函数, 它们是从定义和格式化其参数的跟踪事件接口中被使用
>
> 跟踪事件在tracefs中可见, 并与Ftrace共享输出和控制文件

```
alarmtimer    error_report    interconnect  napi            regulator   tegra_apb_dma
avc           ext4            iocost        neigh           rpm         thermal
block         fib             iomap         net             rpmh        thermal_power_allocator
bpf_test_run  fib6            iommu         netlink         rseq        timer
bpf_trace     filelock        io_uring      oom             rtc         udp
bridge        filemap         ipi           page_isolation  sched       v4l2
cgroup        fs_dax          irq           pagemap         scmi        vb2
clk           ftrace          jbd2          page_pool       scsi        virtio_gpu
cma           gpio            kmem          percpu          signal      vmscan
compaction    hda             kvm           power           skb         wbt
cpuhp         hda_controller  libata        printk          smbus       workqueue
cros_ec       hda_intel       mdio          pwm             sock        writeback
devfreq       header_event    migrate       qdisc           spi         xdp
devlink       header_page     mmap          random          swiotlb     xhci-hcd
dma_fence     huge_memory     mmap_lock     ras             sync_trace
drm           hwmon           mmc           raw_syscalls    syscalls
emulation     i2c             module        rcu             task
enable        initcall        mptcp         regmap          tcp

```

#### Filter

> field operator value
>
> > 数字运算符: == != < <= > >= &
> >
> > 字符串运算符: == != ~
> >
> > 通配符: * ? []
> >
> > 布尔表达式使用 && || 进行组合

```
# bytes字段大于64KB事件, 输出结果中包含较大的I/O统计
echo 'bytes > 65536' > events/block/block_rq_insert/filter
cat trace_pipe
echo 0 > events/block/block_rq_insert/filter
```

#### Trigger

> 触发器可在事件被触发时运行额外的跟踪命令
>
> 该命令可以启用或禁用其他跟踪器, 打印栈跟踪, 保存跟踪缓冲区的快照

```
# 当一个大于64KB的块I/O排队时, 禁用跟踪traceoff
echo 'traceoff if bytes > 65535' > events/block/block_rq_insert/trigger
```

# Kprobes







# Tracers List

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

# Graph Function

> **设置追踪函数** : 产生函数调用堆栈
>
> echo netif_receive_skb > set_graph_function  
>
> echo do_sys_call > set_graph_notrace 禁用函数调用堆栈

# Event Tracing

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

```
#!/bin/bash
debugfs=/sys/kernel/debug
echo nop > $debugfs/tracing/current_tracer
echo 0 > $debugfs/tracing/tracing_on
echo $$ > $debugfs/tracing/set_ftrace_pid
echo function > $debugfs/tracing/current_tracer
echo 'sched:sched_kthread_stop_ret' > $debugfs/tracing/set_event
echo 1 > $debugfs/tracing/events/sched/sched_kthread_stop_ret/enable
echo 1 > $debugfs/tracing/tracing_on
exec "$@"
```

