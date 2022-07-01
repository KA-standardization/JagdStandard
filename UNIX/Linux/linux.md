### 帐篷陆龟

```
解释器本身是一般的编译型程序
wc -l 算出行数
cat > run_file who | wc -l (cat复制终端输入 )
printf format-string [arguments...]
tr -Ccds source replace
stty -echo (set tty)关闭
stty echo 开启
	stty -echo
	read < /dev/tty
	stty echo
sh -x (开启追踪)
set -x (脚本中开启追踪)
set +x (脚本中关闭追踪)
```

#### 查找与替换

* ```
  grep
  who | grep -F xxx (-F查找固定字符串xxx 默认就等同于-F) 46
  egrep
  fgrep
  方括号表达式[...] POSIX字符集 放在方括号表达式中
  后向引用backreferences
  \(["']\).*\1
  {n,} 至少出现n次
  ^$ 用来匹配空的字符串或者行
  [root@localhost ~]# echo "*hhhhaaa" | grep '.*'
  *hhhhaaa
  [root@localhost ~]# echo "*hhhhaaa" | grep '*'
  *hhhhaaa
  [root@localhost ~]# echo "*hhhhaaa" | grep -E '*'
  *hhhhaaa
  [root@localhost ~]# echo "*hhhhaaa" | egrep '*'
  *hhhhaaa
  判断调用
  ((read|write)[[:space:]]*)+ 此处的*为判断调用 此匹配可以取得在行结尾的单词,也可以匹配中间完全没有空白的单词
  \<chop\> 单词匹配
  
  ```

### 命令行编辑器

#### sed

* ```
  默认情况下,sed编辑器会将指定的命令应用到STDIN输入流上
  [root@localhost ~]# echo "nothing is true" | sed 's/true/True/' 
  nothing is True
  sed 's/old/new/' data.txt
  s命令用斜线指定第二个文本字符串来替换第一个文本字符串 (默认只替换每行出现的第一处)
  sed编辑器并不会修改文本文件的数据,它只是将修改后的数据发送到STDOUT
  ```

* ```
  在sed命令行上执行多个命令 -e 
  sed -e 's/old/new/;s/old2/new2/' data.txt 
  bash shell次提示符来分隔命令
  [root@localhost ~]# echo "nothing is true" | sed -e 's/true/True/
  > s/is/IS/'
  ```

* ```
  从文件中读取命令 -f 
  为了避免搞混.sed用作sed脚本文件的扩展名
  cat script.sed
  s/old/new/
  s/old1/new1/
  
  sed -f script.sed data.txt
  ```

* ```
  替换标记
  's/old/new/flags'
  	数字,表明新文本将替换第几处
  	g,替换所有文本
  	p,表明原先内容要打印出来
  	=,打印行号
  	l,列出行
  	w file,将替换的结果写到文件中
  [root@localhost Documents]# cat data2.txt 
  this is a test of the test script
  this is the test of the test script
  
  [root@localhost Documents]# sed 's/test/hhhh/g' data2.txt 
  this is a hhhh of the hhhh script
  this is the hhhh of the hhhh script
  
  [root@localhost Documents]# sed -n 's/test/hhh/p' data2.txt 
  this is a hhh of the test script
  this is the hhh of the test script
  
  [root@localhost Documents]# sed 's/test/hello/w t.txt' data2.txt 
  this is a hello of the test script
  this is the hello of the test script
  [root@localhost Documents]# cat t.txt 
  this is a hello of the test script
  this is the hello of the test script
  ```
  
* ```
  sed选择其他分割符 
  sed 's!/bin/bash!/bin/csh!' /etc/passwd
  ```
* ```
  sed作用于某些行
  行寻址
  	以数字形式表示行区间
      [root@localhost Documents]# sed '2s!this!THIS!' t.txt 
      this is a hello of the test script
      THIS is the hello of the test script
      区间
      [root@localhost Documents]# sed '1,2s!this!THIS!' t.txt 
      THIS is a hello of the test script
      THIS is the hello of the test script
  	某行开始到结尾
  	[root@localhost Documents]# sed '1,$s!this!THIS!' t.txt 
      THIS is a hello of the test script
      THIS is the hello of the test script
  
  	用文本模式来过滤出行
  	必须用正斜线将要指定的pattern封起来
  	sed '/zhangqin/s/old/new/' /etc/passwd
  ```

* ```
  命令组合 在单行上执行多条命令
  sed '2{s/old/new/;s/old1/new1/}' data.txt
  指定地址区间
  sed '2,${s/old/new/;s/old1/new1/}' data.txt
  ```

* ```
  删除行
  sed 'd' data.txt
  指定删除
  sed '3d' data.txt
  区间删除
  sed '2,3d' data.txt
  sed '2,$d' data.txt
  sed编辑器的模式匹配
  sed '/this is/d' data.txt
  使用两个文本模式删除某个区间内的行
  sed '/1/,/3/d' data.txt (第一个模式会打开删除功能 第二个模式会关闭删除功能)
  
  ```

* ```
  插入
  	插入 会在指定前增加一个新行 i insert
      [root@localhost Documents]# echo "this is 1" | sed 'i\this is 2'
      this is 2
      this is 1
  	附加 会在指定行后增加一个新行 a append
      [root@localhost Documents]# echo "this is 1" | sed 'a\this is 2'
      this is 1
      this is 2
  	插入到第三行前
  	sed '3i\haha' data.txt
  	插入到第三行后
  	sed '3a\haha' data.txt
  	插入到最后一行前 后
  	sed '$i\haha' data.txt
  	sed '$a\haha' data.txt
  ```

* ```
  修改 change
  	修改某行
  	sed '3c\haha' data.txt
  	匹配数据流中的任意文本
  	sed '/this/c\haha' data.txt 
  	使用地址区间会把整个闭区间替换成这一行
  	sed '2,3c\haha' data.txt
  ```

* ```
  处理单个字符 y transform 
  [root@localhost Documents]# cat data8.txt 
  this is a 1
  this is a 2
  this is a 3
  this is a 4
  如果inchars和outchars值长度不同,则sed编辑器会产生一条错误
  [root@localhost Documents]# sed 'y/123/789/' data8.txt
  this is a 7
  this is a 8
  this is a 9
  this is a 4
  ```

* ```
  打印行号
  [root@localhost Documents]# sed '=' data8.txt 
  1
  this is a 1
  2
  this is a 2
  3
  this is a 3
  4
  this is a 4
  ```

* ```
  从文件读取数据 r read 允许将一个独立的文件中的数据插入到数据流中 
  [root@localhost Documents]# sed '3r data12.txt' data8.txt 
  this is a 1
  this is a 2
  this is a 3
  11111111111111
  22222222222222
  this is a 4
  模式匹配
  [root@localhost Documents]# sed '/a 2/r data12.txt' data8.txt
  this is a 1
  this is a 2
  11111111111111
  22222222222222
  this is a 3
  this is a 4
  插入到末尾
  [root@localhost Documents]# sed '$r data12.txt' data8.txt 
  this is a 1
  this is a 2
  this is a 3
  this is a 4
  11111111111111
  22222222222222
  读取和删除 change 替换命令
  sed '/list/{r data11.txt;d}' data.txt (先插入文件到list这行后,在删除list这一行)
  ```

* ```
  匹配数字
  [root@localhost Documents]# echo "123" | sed -n '/[[:digit:]]/p'
  123
  [root@localhost Documents]# echo "123" | sed -n 's/[[:digit:]]/456/p'
  45623
  [root@localhost Documents]# echo "123" | sed -n 's/[[:digit:]]/456/pg'
  456456456
  匹配字母不区分大小写
  [root@localhost Documents]# echo "abc" | sed 's![[:alpha:]]!ABC!p'
  ABCbc
  ABCbc
  [root@localhost Documents]# echo "abc" | sed -n 's![[:alpha:]]!ABC!p'
  ABCbc
  [root@localhost Documents]# echo "abc" | sed -n 's![[:alpha:]]!ABC!pg'
  ABCABCABC
  匹配数字字母
  [root@localhost Documents]# echo "as123" | sed -n 's/[[:alnum:]]/QWE/p2'
  aQWE123
  匹配空格或制表符
  [root@localhost Documents]# echo "a a" | sed -n 's/[[:blank:]]/AAA/p'
  aAAAa
  匹配小写字母
  [root@localhost Documents]# echo "aAAA" | sed -n 's/[[:lower:]]/QQ/p'
  QQAAA
  匹配大写字母
  [root@localhost Documents]# echo "aAAA" | sed -n 's/[[:upper:]]/QQ/p'
  aQQAA
  匹配任意空白符
  [root@localhost Documents]# echo " a " | sed -n 's/[[:space:]]/XX/pg'
  XXaXX
  匹配标点符号
  [root@localhost Documents]# echo "a,.? a" | sed -n 's/[[:punct:]]/A/pg'
  aAAA a
  匹配任意可打印字符
  [root@localhost Documents]# echo "nothing is true, . ?" | sed -n 's@[[:print:]]@A@pg'
  AAAAAAAAAAAAAAAAAAAA
  ```

  

#### gawk

* ```
  gawk程序脚本用一对花括号来定义,必须将脚本命令放到花括号中
  每个数据字段都是通过字段分隔符划分的
      $0代表整个文本行
      $1代表文本行的第一个字段
      $2代表文本行的第二个字段
      $n代表文本行的第N个字段
  [root@localhost Documents]# gawk '{print $0}' data.txt 
  one 1 yi
  two 2 er
  three 3 san
  ```

* ```
  使用其他分隔符 -F
  [root@localhost Documents]# gawk -F: '{print $1}' /etc/passwd
  root
  bin
  daemon
  ```

* ```
  使用多条命令 (在命令之间放分号即可)
  [root@localhost Documents]# echo "I am Rich" | gawk '{$3="Super";print $0}'
  I am Super
  bash shell 次提示符
  [root@localhost Documents]# gawk '{
  > $3="super"
  > print $0'}
  my is rich     (STDIN)
  my is super	   (STDOUT)
  ```

* ```
  从文件中读取 -f
  [root@localhost Documents]# cat script.gawk 
  {print $1 "'s home dir is " $6}
  
  {
  text="'s home dir is "
  print $1 text $6
  }
  
  [root@localhost Documents]# gawk -F: -f script.gawk /etc/passwd
  root's home dir is /root
  bin's home dir is /bin
  ```

* ```
  在处理数据前运行脚本 BEGIN
  [root@localhost Documents]# gawk 'BEGIN {print "CNM"}'
  CNM
  [root@localhost Documents]# gawk 'BEGIN {print "hello"};{print $0}' data.txt 
  hello
  one 1 yi
  two 2 er
  three 3 san
  ```

* ```
  在处理数据后运行脚本 END
  [root@localhost Documents]# gawk 'BEGIN {print "hello"};{print $0};END {print "word"}' data.txt 
  hello
  one 1 yi
  two 2 er
  three 3 san
  word
  ```

### 文件夹中查找指定字符串

```shell
grep -r -e string directory
```

### 批量删除进程

```
ps -ef |grep tasks/daily_task.py |gawk '{print $2}'|xargs kill -9
```

### 时区

```shell
tzselect
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

ntpdate -dv ntp.api.bz
```

### python

```
wget https://www.python.org/ftp/python/3.8.11/Python-3.8.11.tgz

yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel

cd Python-3.7.0
./configure --prefix=/partita/python38
make && make install

ln -s /partita/python38/bin/python3.8 /usr/bin/python3
ln -s /partita/python38/bin/pip3.8 /usr/bin/pip3
```

### htop

```
yum -y install epel-release
yum -y install htop
```

### sshd

```
sed -i -e 's#\#UseDNS yes#UseDNS no#g' -e 's#UseDNS yes#UseDNS no#g' -e 's#\#GSSAPIAuthentication yes#GSSAPIAuthentication no#g' -e 's#GSSAPIAuthentication yes#GSSAPIAuthentication no#g' /etc/ssh/sshd_config
systemctl restart sshd
```

### cmd

```
du -sh /* | sort –nr  ：找出系统中占容量最大的文件夹

isof -i:8080
```

### curl

```
-F 提交表单数据
curl -v http://xxxx -F name=aa -F age=2
```

### IPC

```


ipc.h
#ifndef _LINUX_IPC_H
#define _LINUX_IPC_H

#include <linux/types.h>

#define IPC_PRIVATE ((__kernel_key_t) 0)  

/* Obsolete, used only for backwards compatibility and libc5 compiles */
struct ipc_perm
{
		// 键 系统支持两种键(公有,私有)
        __kernel_key_t  key; 
        // 对象拥有者对应进程的有效用户识别号和有效组织识别号
        __kernel_uid_t  uid;
        __kernel_gid_t  gid;
        //对象创建者对应进程的有效用户识别号和有效组识别号
        __kernel_uid_t  cuid;
        __kernel_gid_t  cgid;
        // 存取模式
        __kernel_mode_t mode;
        // 序列号
        unsigned short  seq;
};

/* Include the definition of ipc64_perm */
#include <asm/ipcbuf.h>

/* resource get request flags */
#define IPC_CREAT  00001000   /* create if key is nonexistent */
#define IPC_EXCL   00002000   /* fail if key exists */
#define IPC_NOWAIT 00004000   /* return error on wait */

/* these fields are used by the DIPC package so the kernel as standard
   should avoid using them if possible */
   
#define IPC_DIPC 00010000  /* make it distributed */
#define IPC_OWN  00020000  /* this machine is the DIPC owner */

/* 
 * Control commands used with semctl, msgctl and shmctl 
 * see also specific commands in sem.h, msg.h and shm.h
 */
#define IPC_RMID 0     /* remove resource */
#define IPC_SET  1     /* set ipc_perm options */
#define IPC_STAT 2     /* get ipc_perm options */
#define IPC_INFO 3     /* see ipcs */

/*
 * Version flags for semctl, msgctl, and shmctl commands
 * These are passed as bitflags or-ed with the actual command
 */
#define IPC_OLD 0       /* Old version (no 32-bit UID support on many
                           architectures) */
#define IPC_64  0x0100  /* New version (support 32-bit UIDs, bigger
                           message sizes, etc. */

/*
 * These are used to wrap system calls.
 *
 * See architecture code for ugly details..
 */
struct ipc_kludge {
        struct msgbuf *msgp;
        long msgtyp;
};

#define SEMOP            1
#define SEMGET           2
#define SEMCTL           3
#define SEMTIMEDOP       4
#define MSGSND          11
#define MSGRCV          12
#define MSGGET          13
#define MSGCTL          14
#define SHMAT           21
#define SHMDT           22
#define SHMGET          23
#define SHMCTL          24

/* Used by the DIPC package, try and avoid reusing it */
#define DIPC            25

#define IPCCALL(version,op)     ((version)<<16 | (op))


#endif /* _LINUX_IPC_H */

```

```
信号量:
	解决同步和赋值方法
	系统中每个信号量的数据结构 sem
	系统中表示信号量集合(set)的数据结构 semid_ds
	系统中每一信号量集合的队列结构 sem_queue
	
	
#ifndef _LINUX_SEM_H
#define _LINUX_SEM_H

#include <linux/ipc.h>

/* semop flags */
#define SEM_UNDO        0x1000  /* undo the operation on exit */

/* semctl Command Definitions. */
#define GETPID  11       /* get sempid */
#define GETVAL  12       /* get semval */
#define GETALL  13       /* get all semval's */
#define GETNCNT 14       /* get semncnt */
#define GETZCNT 15       /* get semzcnt */
#define SETVAL  16       /* set semval */
#define SETALL  17       /* set all semval's */

/* ipcs ctl cmds */
#define SEM_STAT 18
#define SEM_INFO 19
#define SEM_STAT_ANY 20

/* Obsolete, used only for backwards compatibility and libc5 compiles */
struct semid_ds {
        struct ipc_perm sem_perm;               /* IPC权限permissions .. see ipc.h */
        __kernel_time_t sem_otime;              /* 最后一次对信号量操作的时间last semop time */
        __kernel_time_t sem_ctime;              /* 对这个结构最后一次修改的时间last change time */
        struct sem      *sem_base;              /* 对信号量数组中指向第一个信号量的指针ptr to first semaphore in array */
        struct sem_queue *sem_pending;          /* 待处理的挂起操作pending operations to be processed */
        struct sem_queue **sem_pending_last;    /* last pending operation */
        struct sem_undo *undo;                  /* 在这个数组上的undo请求undo requests on this array */
        unsigned short  sem_nsems;              /* 在信号量数组上的信号量号no. of semaphores in array */
};

/* Include the definition of semid64_ds */
#include <asm/sembuf.h>

/* semop system calls takes an array of these. */
struct sembuf {
        unsigned short  sem_num;        /* semaphore index in array */
        short           sem_op;         /* semaphore operation */
        short           sem_flg;        /* operation flags */
};

/* arg for semctl system calls. */
union semun {
        int val;                        /* value for SETVAL */
        struct semid_ds *buf;   /* buffer for IPC_STAT & IPC_SET */
        unsigned short *array;  /* array for GETALL & SETALL */
        struct seminfo *__buf;  /* buffer for IPC_INFO */
        void *__pad;
};

struct  seminfo {
        int semmap;
        int semmni;
        int semmns;
        int semmnu;
        int semmsl;
        int semopm;
        int semume;
        int semusz;
        int semvmx;
        int semaem;
};

#define SEMMNI  128             /* <= IPCMNI  max # of semaphore identifiers */
#define SEMMSL  250             /* <= 8 000 max num of semaphores per id */
#define SEMMNS  (SEMMNI*SEMMSL) /* <= INT_MAX max # of semaphores in system */
#define SEMOPM  32              /* <= 1 000 max num of ops per semop call */
#define SEMVMX  32767           /* <= 32767 semaphore maximum value */
#define SEMAEM  SEMVMX          /* adjust on exit max value */

/* unused */
#define SEMUME  SEMOPM          /* max num of undo entries per process */
#define SEMMNU  SEMMNS          /* num of undo structures system wide */
#define SEMMAP  SEMMNS          /* # of entries in semaphore map */
#define SEMUSZ  20              /* sizeof struct sem_undo */


#endif /* _LINUX_SEM_H */
```



