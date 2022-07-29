### 安装

```
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo

wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-8.repo
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo

yum clean all
yum makecache
yum update -y
yum install bcc-tools
cd /usr/share/bcc/tools

vi /etc/profile
source /etc/profile
execsnoop
biolatency -m
opensnoop
funccount 't:syscalls:sys_enter_*'
execsnoop
biolatency -m
 opensnoop
funccount '/alidata/server/imfaker/.venv/bin/python'
funccount '/alidata/server/imfaker/.venv/bin/python:celery'
funccount '/alidata/server/imfaker/.venv/bin:python'
funccount 'python'
funccount 'python3'
funccount -i 1 'tcp_send*'
funccount python
funccount -i 1 t:sched:sched_process_fork
stackcount -P celeryd
stackcount -P /alidata/server/imfaker/.venv/lib64/python3.6/site-packages/certifi/cacert.pem
stackcount -P ktime_get

git clone http://github.com/brendangregg/FlameGraph
argdist -H 'r::__tcp_select_window():int:$retval'
argdist -H 'p::tcp_sendmsg(struct sock *sk, struct msghdr *msg, size_t size):u32:size'
```

```
opensnoop
journalctl --since today
journalctl _COMM=root _COMM=login -n 10
journalctl _COMM=root _COMM=login
journalctl _COMM=login
journalctl _COMM=bash
journalctl _COMM=python
journalctl -p err
git clone https://github.com/iovisor/bpftrace
execsnoop
runqlat
profile
runqlat 10 1
sar -uq 1
runqlat -P
ps -ef | grep 1067
dmesg
free
pmap
oomkill
runqlat -P
ps -ef|grep 67314
memleak -p 67314
trace -U t:syscalls:sys_enter_brk
stackcount -PU t:syscalls:sys_enter_brk
shmsnoop
```

### 