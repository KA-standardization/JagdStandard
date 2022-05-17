# 传统工具
"""
df -h
显示文件系统磁盘用量
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs         32G     0   32G   0% /dev
tmpfs            32G  4.2M   32G   1% /dev/shm
tmpfs            32G  3.3G   29G  11% /run
tmpfs            32G     0   32G   0% /sys/fs/cgroup
/dev/sda2       108G   26G   77G  26% /
/dev/sda1       976M  176M  733M  20% /boot
tmpfs           6.3G     0  6.3G   0% /run/user/0

Use%
文件系统使用率超过90%，它的性能可能下降
因为，可用空间的下降，空余块越来越少，越来越分散，导致顺序写负载变为随机写负载
"""
"""
mount
列出文件系统的类型和挂载参数
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
devtmpfs on /dev type devtmpfs (rw,nosuid,size=32946696k,nr_inodes=8236674,mode=755)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,nodev,mode=755)
tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,mode=755)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,xattr,release_agent=/usr/lib/systemd/systemd-cgroups-agent,name=systemd)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,perf_event)
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,cpuset)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,net_prio,net_cls)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,devices)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,blkio)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,freezer)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpuacct,cpu)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,hugetlb)
configfs on /sys/kernel/config type configfs (rw,relatime)
/dev/sda2 on / type ext4 (rw,relatime,data=ordered)
mqueue on /dev/mqueue type mqueue (rw,relatime)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=33,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=15199)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
/dev/sda1 on /boot type ext4 (rw,relatime,data=ordered)
sunrpc on /var/lib/nfs/rpc_pipefs type rpc_pipefs (rw,relatime)
/dev/sda2 on /var/lib/docker/containers type ext4 (rw,relatime,data=ordered)
/dev/sda2 on /var/lib/docker/overlay2 type ext4 (rw,relatime,data=ordered)
tmpfs on /run/user/0 type tmpfs (rw,nosuid,nodev,relatime,size=6592408k,mode=700)

/relatime 可优化为noatime 通过避免记录访问时间戳来提高性能 
"""
"""
strace cksum -tttT /usr/bin/cksum
跟踪系统中的系统调用 -ttt 将系统时钟时间戳以微妙单位作为第一列输出，-T记录系统调用所花费的时间（秒）
execve("/usr/bin/cksum", ["cksum", "-tttT", "/usr/bin/cksum"], 0x7ffdb4f5e690 /* 30 vars */) = 0
brk(NULL)                               = 0x119c000
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f9387340000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=91669, ...}) = 0
mmap(NULL, 91669, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f9387329000
close(3)                                = 0
open("/lib64/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0`&\2\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=2156240, ...}) = 0
mmap(NULL, 3985920, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9386d52000
mprotect(0x7f9386f15000, 2097152, PROT_NONE) = 0
mmap(0x7f9387115000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1c3000) = 0x7f9387115000
mmap(0x7f938711b000, 16896, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f938711b000
close(3)                                = 0
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f9387328000
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f9387326000
arch_prctl(ARCH_SET_FS, 0x7f9387326740) = 0
mprotect(0x7f9387115000, 16384, PROT_READ) = 0
mprotect(0x606000, 4096, PROT_READ)     = 0
mprotect(0x7f9387341000, 4096, PROT_READ) = 0
munmap(0x7f9387329000, 91669)           = 0
brk(NULL)                               = 0x119c000
brk(0x11bd000)                          = 0x11bd000
brk(NULL)                               = 0x11bd000
open("/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=106172832, ...}) = 0
mmap(NULL, 106172832, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f9380810000
close(3)                                = 0
open("/usr/share/locale/locale.alias", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=2502, ...}) = 0
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f938733f000
read(3, "# Locale name alias data base.\n#"..., 4096) = 2502
read(3, "", 4096)                       = 0
close(3)                                = 0
munmap(0x7f938733f000, 4096)            = 0
open("/usr/share/locale/en_US.UTF-8/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en_US.utf8/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en_US/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en.UTF-8/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en.utf8/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
write(2, "cksum: invalid option -- 't'\n", 29cksum: invalid option -- 't'
) = 29
open("/usr/share/locale/en_US.UTF-8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en_US.utf8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en_US/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en.UTF-8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en.utf8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
write(2, "Try 'cksum --help' for more info"..., 41Try 'cksum --help' for more information.
) = 41
close(1)                                = 0
close(2)                                = 0
exit_group(1)                           = ?
+++ exited with 1 +++

由于strace用ptrace实现，
ptrace内部实现方式是在系统调用的开始处和结束处添加一个断点来记录相关信息，大幅降低目标软件的运行速度
perf是替代品
"""
"""
perf trace cksum /usr/bin/cksum

"""
"""
opensnoop -T
-T 输出时间戳信息
-x 只显示打开失败的操作
-p PID 仅监控给定的进程
-n NAME 仅显示进程名字包含NAME的事件
跟踪文件打开事件，发现系统中使用的数据文件，日志文件，配置文件
该工具可以揭示由于快速打开大量文件导致的性能问题，帮助调试找不到文件导致的问题
17.415835000  93055  [celeryd: zvide   139   0 /alidata/server/imfaker/.venv/lib/python3.6/site-packages/certifi/cacert.pem
17.418271000  92936  [celeryd: zvide   137   0 /etc/passwd
17.418399000  92936  [celeryd: zvide   137   0 /etc/passwd
17.422936000  93026  [celeryd: zvide   148   0 /etc/passwd
17.423035000  93026  [celeryd: zvide   148   0 /etc/passwd
17.431055000  93026  [celeryd: zvide   148   0 /etc/passwd
17.431148000  93026  [celeryd: zvide   148   0 /etc/passwd
17.435811000  93041  [celeryd: zvide   162   0 /alidata/server/imfaker/.venv/lib/python3.6/site-packages/certifi/cacert.pem

stackcount -p 92908 't:syscalls:sys_enter_openat'
对该PID记录打开跟踪点调用信息
"""






