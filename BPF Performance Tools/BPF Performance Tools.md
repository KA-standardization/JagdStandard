# 1.引言

> https://github.com/iovisor

```
vim /etc/ssh/sshd_config 
vim /etc/ssh/ssh_config 
		PasswordAuthentication yes
		PermitRootLogin prohibit-password yes
service ssh restar
```

### BCC

```
execsnoop -t
biolatency -m
# 显示失败的open系统调用
opensnoop -x 
```

### bpftrace

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



