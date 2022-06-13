# 1.Make

```
vi /etc/hosts
10.0.22.100	hadoopMaster0
10.0.17.103	hadoopMaster1
10.0.17.100	hadoopSlave0
10.0.17.101	hadoopSlave1
10.0.17.102	hadoopSlave2
10.0.24.100	hadoopSlave3

hostname hadoopMaster0

BCC_HOME=/usr/share/bcc/tools/
HADOOP_HOME=/partita/astronaut/share/hadoop3/
JAVA_HOME=/kaiser/jdk1.8.0_291
JRE_HOME=/kaiser/jdk1.8.0_291/jre
CLASS_PATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin:$BCC_HOME:$HADOOP_HOME/bin
export JAVA_HOME JRE_HOME CLASS_PATH HADOOP_HOME PATH
```

# 2.Config

```
ERROR: Attempting to operate on hdfs namenode as root
vi /partita/astronaut/share/hadoop3/sbin/start-dfs.sh
vi /partita/astronaut/share/hadoop3/sbin/stop-dfs.sh
	HDFS_DATANODE_USER=root
	HADOOP_SECURE_DN_USER=root
	HDFS_NAMENODE_USER=root
	HDFS_SECONDARYNAMENODE_USER=root
vi /partita/astronaut/share/hadoop3/sbin/start-yarn.sh
vi /partita/astronaut/share/hadoop3/sbin/stop-yarn.sh
    YARN_RESOURCEMANAGER_USER=root
    HADOOP_SECURE_DN_USER=yarn
    YARN_NODEMANAGER_USER=root
scp /partita/astronaut/share/hadoop3/sbin/start-yarn.sh /partita/astronaut/share/hadoop3/sbin/stop-yarn.sh /partita/astronaut/share/hadoop3/sbin/start-dfs.sh /partita/astronaut/share/hadoop3/sbin/stop-dfs.sh root@10.0.17.101:/partita/astronaut/share/hadoop3/sbin/
```

```
./bin/hdfs namenode -format
ERROR conf.Configuration: error parsing conf hdfs-site.xml
<!--hdfs-site.xml-->
<configuration> 
	<property> 
		<name>dfs.namenode.secondary.http-address</name> 
		<value>hadoopMaster1:9001</value> 
	</property> 
	<property> 
		<name>dfs.namenode.name.dir</name> 
		<value>file:/var/log/hadoop/tmp/dfs/name</value> 
	</property> 
	<property> 
		<name>dfs.datanode.data.dir</name> 
		<value>file:/var/log/hadoop/tmp/dfs/data</value> 
	</property> 
	<property> 
		<name>dfs.replication</name> 
		<value>4</value> 
	</property> 
	<property> 
		<name>dfs.webhdfs.enabled</name> 
		<value>true</value> 
	</property> 
</configuration>
<!--core-site.xml-->
<configuration> 
	<property> 
		<name>fs.defaultFS</name> 
		<value>hdfs://hadoopMaster0:9000</value> 
	</property> 
	<property> 
		<name>io.file.buffer.size</name> 
		<value>131072</value> 
	</property> 
	<property> 
		<name>hadoop.tmp.dir</name> 
		<value>file:/var/log/hadoop/tmp</value> 
		<description>A base for other temporary directories.</description> 
	</property> 
</configuration>
<!--mapred-site.xml-->
<configuration> 
	<property> 
		<name>mapreduce.framework.name</name> 
		<value>yarn</value> 
	</property> 
	<property> 
		<name>mapreduce.jobhistory.address</name> 
		<value>hadoopMaster0:10020</value> 
	</property> 
	<property> 
		<name>mapreduce.jobhistory.webapp.address</name> 
		<value>hadoopMaster0:19888</value> 
	</property> 
</configuration>
<!--yarn-site.xml-->
<configuration> 
	<property> 
		<name>yarn.nodemanager.aux-services</name> 
		<value>mapreduce_shuffle</value> 
	</property> 
	<property> 
		<name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name> 
		<value>org.apache.hadoop.mapred.ShuffleHandler</value> 
	</property> 
	<property> 
		<name>yarn.resourcemanager.hostname</name> 
		<value>hadoopMaster1</value> 
	</property> 
	<property> 
		<name>yarn.resourcemanager.scheduler.address</name> 
		<value>hadoopMaster1:8030</value> 
	</property> 
	<property> 
		<name>yarn.resourcemanager.resource-tracker.address</name> 
		<value>hadoopMaster1:8031</value> 
	</property> 
	<property> 
		<name>yarn.resourcemanager.address</name> 
		<value>hadoopMaster1:8032</value> 
	</property> 
	<property> 
		<name>yarn.resourcemanager.admin.address</name> 
		<value>hadoopMaster1:8033</value> 
	</property> 
	<property> 
		<name>yarn.resourcemanager.webapp.address</name> 
		<value>hadoopMaster1:8088</value> 
	</property> 
</configuration>
```

```
bash v3.2+ is required. Sorry.
系统使用了zsh或者其他非bash的shell，而hadoop的脚本都是使用bash编写的
chsh -s /bin/bash

```



# 3.RUN

> MapReduce框架
>
> ​	PYTHON
>
> ​	mrjob https://bitly.com/1NqmsvA https://github.com/Yelp/mrjob
>
> ​	*dumbo https://bitly.com/1UQx8G3 https://github.com/klbostee/dumbo/wiki
>
> ​	C++
>
> ​	pydoop  https://bitly.com/1LizcVD
>
> ​	Cython 
>
> ​	hadoopy  https://bitly.com/1TQugX1

```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
	-input corpus \
	-output bigrams \
	-mapper mapper.py \
	-reducer reducer.py \ # -reducer 0 只执行mapzuo
	-file mapper.py \
	-file reducer.py \
	-file framework.py
```

