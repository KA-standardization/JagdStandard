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

