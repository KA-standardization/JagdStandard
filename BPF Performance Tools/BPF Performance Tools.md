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



