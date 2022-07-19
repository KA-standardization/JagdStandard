# Azkaban

```
Azkaban:轻量级
Oozie:重量级 xml
Zeus:阿里调度框架
```

### 工作流

```
工作流主要解决的主要问题是：为了实现某个业务目标，利用计算机在多个参与者之间按某种预定规则自动传递文档、信息或者任务。
```

#### jBPM

<img src="J:\笔记\imgs\jbpm.png" style="zoom:550%;" />

#### Activiti

![](J:\笔记\imgs\activiti.jpg)

### ETL

```
step1-->step2-->step3
```

#### 1.数据抽取

```
Sqoop:把RDBMS(关系型数据库)中的数据抽取到Hadoop
Flume:把日志,文本数据的采集到Hadoop
```

#### 2.数据处理

```
Hive
MapReduce
Spark
```

#### 3.统计结果入库

```
数据存放到HDFS(Hive,SparkSQL,file)
	启动Server:HiveServer2,ThriftServer
使用Sqoop把结果导入RDBMSZ中
```

### crontab

```
crontab -l
crontab -e
	* * * * * 脚本
```

### 模式

```
the stand alone “solo-server” mode
distributed multiple-executor mode
```

### 安装

```
git clone https://github.com/azkaban/azkaban.git
cd azkaban
./gradlew build installDist
vi /root/app/azkaban/gradle/wrapper/gradle-wrapper.properties
	distributionUrl=./gradle-4.6-all.zip


zip -r dependencies.zip foo.job bar.job

keytool -keystore keystore -alias zhangqin -genkey -keyalg RSA

```

### Hive&Azkaban

```
create table emp(
empno int,ename string,job string,mgr int,hiredate string,sal double,comm double,deptno int
)row format delimited fields terminated by '\t';

load data local inpath '' overwrite into table emp

```

### 创建MySQL

```
CREATE DATABASE azkaban;
CREATE USER 'azkaban'@'%' IDENTIFIED BY 'azkaban';
GRANT SELECT,INSERT,UPDATE,DELETE ON azkaban.* to 'azkaban'@'%' WITH GRANT OPTION;
flush privileges;
```

### azkaban-conf

> `azkaban.properties`文件是主要的配置文件

```shell
root@83c1759c7008:/usr/local/azkaban/azkaban-exec-server/conf# cat azkaban.properties 
# Azkaban Personalization Settings
azkaban.name=Test
azkaban.label=My Local Azkaban
azkaban.color=#FF3601
azkaban.default.servlet.path=/index
web.resource.dir=web/
default.timezone.id=America/Los_Angeles

# Azkaban UserManager class
user.manager.class=azkaban.user.XmlUserManager
user.manager.xml.file=conf/azkaban-users.xml

# Loader for projects
executor.global.properties=conf/global.properties
azkaban.project.dir=projects

database.type=h2
h2.path=./h2
h2.create.tables=true

# Velocity dev mode
velocity.dev.mode=false

# Azkaban Jetty server properties.
jetty.use.ssl=false
jetty.maxThreads=25
jetty.port=8081

# Azkaban Executor settings
executor.port=12321

# mail settings
mail.sender=
mail.host=
job.failure.email=
job.success.email=

lockdown.create.projects=false

cache.directory=cache

# JMX stats
jetty.connector.stats=true
executor.connector.stats=true

# Azkaban plugin settings
azkaban.jobtype.plugin.dir=plugins/jobtypes
```

```shell
root @ 8-200 in /kaiser/azkaban/azkaban/azkaban-solo-server/build/install/azkaban-solo-server on git:master o [18:15:23] 
$ ls
bin  conf  lib  plugins  sql  web
```

```
JAVA_HOME=/partita/kaiser/jdk1.8.0_291
JRE_HOME=/partita/kaiser/jdk1.8.0_291/jre
CLASS_PATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
export JAVA_HOME JRE_HOME CLASS_PATH PATH
```

