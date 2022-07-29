#### Ubuntu卸载MySQL

* ```bush
  sudo apt-get remove mysql-common
  sudo apt-get autoremove --purge mysql-server-5.7
  dpkg -l|grep ^rc|awk '{print$2}'|sudo xargs dpkg -P
  dpkg --list|grep mysql
  ```

#### Ubuntu安装MySQL

* ```
  sudo dpkg -i *.deb
  sudo apt-get -f --fix-missing install #如果报依赖错误
  ```

#### SSH

* ```
  sudo apt-get purge openssh-client 
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install openssh-server
  ps -e|grep ssh # ssh-agent  sshd
  sudo service ssh restart 
  #win10命令行
  ssh -p 端口号 用户名@ip地址
  ```

#### 外部访问

* ```
  USE mysql
  SELECT user,host FROM user;	#查看账户host
  UPDATE user SET host = '%' WHERE user = 'root';
  FLUSH PRIVILEGES;
  ```

* ```
  lsof -i:3306		#端口号 查看端口
  netstat -aptn		#查看所有开放端口
  sudo netstat -tlpn
  netstat -an|grep 3306
  sudo gedit /etc/mysql/mysql.conf.d/mysqld.cnf
  	关闭 #bind-address
  	打开 pid-file	socket daradir log-error port=3306
  service mysql stop
  service mysql start
  ```
  
* ```
  sudo apt-get install iptables
  # sudo iptables -I INPUT -p tcp --dport [端口号] -j ACCEPT
  sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT
  # 临时保存配置，重启后失效
  sudo iptables-save
  sudo apt-get install iptables-persistent
  sudo netfilter-persistent save
  sudo netfilter-persistent reload
  ```

* ```
  #防火墙
  sudo ufw status		#防火墙状态
  
  sudo ufw enable		#开启防火墙
  
  sudo ufw disable	#关闭防火墙
  
  sudo ufw default allow		#允许外部访问
  
  sudo ufw default deny		#拒绝外部访问
  
  sudo ufw allow 22			#开放22端口
  
  sudo ufw deny 22			#关闭22端口
  
  sudo ufw allow from 192.168.101.5	#允许192.168.101.5访问本机
  ```

#### apt-get

* ```
  # http://ppa.launchpad.net/fcitx-team/nightly/ubuntu/dists/xenial/main/binary-amd64/Packages  404 Not Found
  cd /etc/apt/sources.list.d
  mv fcitx-team-ubuntu-nightly-xenial.list fcitx-team-ubuntu-nightly-xenial.list.bak
  ```

#### MySQL

* ```
  mysqladmin --version
  service mysql restart
  ```

* mysql:清屏    

  * ctrl+L    , system clear

* ```
  create table tb(
  				id int(4) auto_increment,
  				name varchar(5),
  				addr varchar(5),
  				primary key(id)
  				)
  				engine=myisam auto_increment=1 default charset=utf8;
  ```

##### Index索引

* ```mysql
  create index addr_index on tb(addr); #单值索引
  alter table tb add index addr_index(addr);
  create unique index name_index on tb(name); #唯一索引
  alter table tb add unique index name_index(name);
  create index addr_name_index on tb(addr,name); #复合索引
  alter table tb add index addr_name_index(addr,name);
  show index from tb;
  drop index name_index on tb;
  ```

* ```
  show variables like '%char%'; #查看字符集
  show variables like '%storage_engine%'; #查看数据库引擎
  ```

##### Explain

* ```
  explain select * from tb;
      id |编号
      select_type |查询类型
      table |表
      partitions |
      type |类型
      possible_keys |预测用到的索引
      key  |实际用到的索引
      key_len |实际用到的索引长度
      ref  |表之间的引用
      rows |通过索引查询到的数据量
      filtered |
      Extra  |额外的信息
  CREATE TABLE course(
  					cid INT(3),
  					cname VARCHAR(20),
  					tid INT(3)
  					);
  
  CREATE TABLE teacher(
  					tid INT(3),
  					tname VARCHAR(20),
  					tcid INT(3)
  					);
  					
  CREATE TABLE teacerCard(
  						tcid INT(3),
  						tcdesc VARCHAR(200)
  					    );
  INSERT INTO course VALUES(1,'java',1);
  INSERT INTO course VALUES(2,'html',1);
  INSERT INTO course VALUES(3,'sql',2);
  INSERT INTO course VALUES(4,'web',3);
  
  INSERT INTO teacher VALUES(1,'tz',1);
  INSERT INTO teacher VALUES(2,'tw',2);
  INSERT INTO teacher VALUES(3,'tl',3);
  
  INSERT INTO teacerCard VALUES(1,'tzdesc');
  INSERT INTO teacerCard VALUES(2,'twdesc');
  INSERT INTO teacerCard VALUES(3,'tldesc');
  ```

###### id |编号

* ```
  #查询课程编号为2  或 教师证编号为3  的老师信息
  SELECT DISTINCT * FROM teacher t,course c,teacerCard tc WHERE t.tid=c.tid AND t.tcid=tc.tcid AND (c.cid=2 OR tc.tcid=3);
  EXPLAIN SELECT DISTINCT * FROM teacher t,course c,teacerCard tc WHERE t.tid=c.tid AND t.tcid=tc.tcid AND (c.cid=2 OR tc.tcid=3);
  # tc3 t6 c8
  #表的执行顺序  因数量的个数改变而改变的原因： 笛卡儿积
  #数据小的表优先查询
  DELETE FROM teacher WHERE tid>1;
  SELECT COUNT(*) FROM teacher;
  EXPLAIN SELECT DISTINCT * FROM teacher t,course c,teacerCard tc WHERE t.tid=c.tid AND t.tcid=tc.tcid AND (c.cid=2 OR tc.tcid=3);
  #查询教授SQL课程的老师的描述
  #id值越大越优先查询 (本质：在嵌套子查询时，先查内层 再查外层)
  EXPLAIN SELECT tc.tcdesc FROM teacerCard tc,course c,teacher t WHERE tc.tcid=t.tcid AND t.tid=c.tid AND c.cname='sql';
  EXPLAIN SELECT tc.tcdesc FROM teacerCard tc WHERE tc.tcid=(SELECT t.tcid FROM teacher t WHERE t.tid=(SELECT c.tid FROM course c WHERE c.cname='sql'));
  EXPLAIN SELECT tc.tcdesc FROM teacerCard tc,teacher t WHERE tc.tcid=t.tcid AND t.tid=(SELECT c.tid FROM course c WHERE c.cname='sql');
  ```

###### select_type |查询类型

* ```
  #PRIMARY: 包含子查询SQL中的 主查询 （最外层）
  #SUBQUERY：包含子查询SQL中的 子查询 （非最外层）
  #simple: 简单查询（不包含子查询、union）
  #derived: 衍生查询(使用到了临时表)
  	a.在from子查询中只有一张表
  		EXPLAIN SELECT cr.cname FROM (SELECT * FROM course WHERE tid IN(1,2)) cr;
  	b.在from子查询中， 如果有table1 union table2 ，则table1 就是derived,table2就是union
  		EXPLAIN SELECT cr.cname FROM (SELECT * FROM course WHERE tid=1 UNION SELECT * FROM course WHERE tid=2) cr;
  #union result :告知开发人员，那些表之间存在union查询
  ```

###### type |类型 索引类型

* system > const > eq_ref > ref > fulltext > ref_or_null > index_merge > unique_subquery > index_subquery > range > index > ALL
* **要对type进行优化的前提：有索引**

* ```
  #system>const>eq_ref>ref>range>index>all
  #system（忽略）: 只有一条数据的系统表 ；或衍生表只有一条数据的主查询
  	CREATE TABLE test01(
  						tid INT(3),
  						tname VARCHAR(20)
  						);
  	INSERT INTO test01 VALUES(1,'a');
  	ALTER TABLE test01 ADD CONSTRAINT tid_pk PRIMARY KEY(tid);
  	EXPLAIN SELECT * FROM (SELECT * FROM test01) t WHERE tid=1;
  ```

* ```
  #const: 仅仅能查到一条数据的SQL ,用于Primary key 或unique索引
  	EXPLAIN SELECT * FROM test01 where tid=1;
  	#删除主键创建一般索引
  	ALTER TABLE test01 DROP PRIMARY KEY;
  	CREATE INDEX test_index ON test01(tid);
  	ALTER TABLE test01 ADD index test_index(tid);
  ```

* ```
  #eq_ref: 唯一性索引：对于每个索引键的查询，返回匹配唯一行数据（每条数据有且只有1个，不能多 、不能0）
  	ALTER TABLE teacerCard ADD CONSTRAINT tcid_pk PRIMARY KEY(tcid);
  	ALTER TABLE teacher ADD CONSTRAINT tcid_uk UNIQUE INDEX(tcid);
  	EXPLAIN SELECT * FROM teacher t,teacerCard tc WHERE t.tcid=tc.tcid;
  ```

* ```
  #ref：非唯一性索引，对于每个索引键的查询，返回匹配的所有行（0，多）
  	INSERT INTO teacher VALUES(2,'tt',2);
  	ALTER TABLE teacher ADD INDEX t_index(tname);
  	EXPLAIN SELECT * FROM teacher WHERE tname='tt';
  ```

* ```
  #range：检索指定范围的行 ,where后面是一个范围查询(between and, >, <, >=, <=, <>)
  #特殊: in有时候会失效,从而转为无索引ALL
  	CREATE INDEX tid_index ON teacher(tid);
  		ALTER TABLE teacher ADD INDEX tid_index(tid);
  	EXPLAIN SELECT * FROM teacher WHERE tid BETWEEN 1 AND 2;
  		EXPLAIN SELECT * FROM teacher WHERE tid<3;
  		EXPLAIN SELECT * FROM teacher WHERE tid IN (1,2);
  ```

* ```
  #index：查询全部索引中数据
  	EXPLAIN SELECT tid FROM teacher;
  	#tid 是索引，只需要扫描索引表，不需要所有表中的所有数据
  ```

* ```
  #all：查询全部表中的数据
  	EXPLAIN SELECT cid FROM course;
  	#cid不是索引，需要全表所有，即需要所有表中的所有数据
  ```

###### possible_keys |预测用到的索引  是一种预测,不准

* ```
  
  ```

###### key  |实际用到的索引

* ```
  
  ```

###### key_len |实际用到的索引长度

* ```
  #用于判断复合索引是否被完全使用
  CREATE TABLE test_kl(
  					name CHAR(20) NOT NULL DEFAULT ' '
  					);
  ALTER TABLE test_kl ADD INDEX name_index(name);
  	CREATE INDEX name_index ON test_kl(name);
  EXPLAIN SELECT * FROM test_kl WHERE name=' ';	#80
  #在utf8：1个字符站3个字节  UTF8最多是一个字符占用4个字节 GBK是2个字节
  #如果索引字段可以为Null,则会使用1个字节用于标识
  ALTER TABLE test_kl ADD COLUMN name1 CHAR(20);
  CREATE INDEX name1_index ON test_kl(name1);
  EXPLAIN SELECT * FROM test_kl WHERE name1=' ';	#81 1个字节用于标识null
  #复合索引
  DROP INDEX name_index ON test_kl;
  DROP INDEX name1_index ON test_kl;
  ALTER TABLE test_kl ADD INDEX name_name1_index(name,name1);
  EXPLAIN SELECT * FROM test_kl WHERE name1='';	#161
  EXPLAIN SELECT * FROM test_kl WHERE name='';	#80
  #VARCHAR
  ALTER TABLE test_kl ADD COLUMN name2 VARCHAR(20);
  ALTER TABLE test_kl ADD INDEX name2_index(name2);
  EXPLAIN SELECT * FROM test_kl WHERE name2='';	#83 1个字节用于标识null 2个字节用于标识可变长度
  ```

###### ref  |表之间的引用

* ```
  CREATE INDEX tid_index ON teacher(tid);
  ALTER TABLE teacher ADD INDEX tname_index(tname);
  CREATE INDEX tid_index ON course(tid);
  EXPLAIN SELECT * FROM course c,teacher t WHERE c.tid=t.tid AND t.tname='tw';	#常量 const
  ```

###### rows |通过索引查询到的数据量

* ```
  EXPLAIN SELECT * FROM course c,teacher t WHERE c.tid=t.tid AND t.tname='tw';
  ```

###### Extra  |额外的信息

* ```
  #using filesort: 性能消耗大；需要“额外”的一次排序（查询）。常见于 order by 语句中。排序：先查询
  CREATE TABLE test02(
  					a CHAR(3),
  					b CHAR(3),
  					c CHAR(3),
  					INDEX a_index(a),
  					INDEX b_index(b),
  					INDEX c_index(c)
  					);
  #单值索引
  #如果查找和排序是同一个字段,则不会出现using filesort
  EXPLAIN SELECT * FROM test02 WHERE a='' ORDER BY a;
  EXPLAIN SELECT * FROM test02 WHERE a='' ORDER BY b;	#using filesort
  #where哪些字段，就order by那些字段
  #复合索引：不能跨列（最佳左前缀）
  DROP INDEX a_index ON test02;
  DROP INDEX b_index ON test02;
  DROP INDEX c_index ON test02;
  ALTER TABLE test02 ADD INDEX a_b_c(a,b,c);
  EXPLAIN SELECT * FROM test02 WHERE a='' ORDER BY c;	#using filesort不能跨列
  EXPLAIN SELECT * FROM test02 WHERE b='' ORDER BY C;	#using filesort不能跨列
  EXPLAIN SELECT * FROM test02 WHERE a='' ORDER BY b;
  EXPLAIN SELECT * FROM test02 WHERE b='' ORDER BY a;
  #where和order by 按照复合索引的顺序使用，不要跨列或无序使用
  ```

* ```
  #using temporary: 性能损耗大 ，用到了临时表。一般出现在group by 语句中
  EXPLAIN SELECT a FROM test02 WHERE a IN ('1','2') GROUP BY a;
  EXPLAIN SELECT a FROM test02 WHERE a IN ('2','3') GROUP BY b;
  	# ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'mydb.test02.a' which is not functionally dependent on columns in GROUP BY clause
  EXPLAIN SELECT b FROM test02 WHERE a IN ('1','2') GROUP BY b;	##using temporary
  ```

* ```
  #using index: 性能提升; 索引覆盖（覆盖索引）。
  #原因：不读取原文件，只从索引文件中获取数据 （不需要回表查询）只要使用到的列 全部都在索引中，就是索引覆盖using index
  EXPLAIN SELECT a,b FROM test02 WHERE a='' OR b='';	#using index
  DROP INDEX a_b_c ON test02;
  ALTER TABLE test02 ADD INDEX a_b(a,b);
  EXPLAIN SELECT a,b FROM test02 WHERE a='' OR c='';	#回表查询
  #如果没有where，则索引只出现在key中；
  EXPLAIN SELECT a,b FROM test02;
  #如果有where，则索引 出现在key和possible_keys中
  EXPLAIN SELECT a,b FROM test02 WHERE a='' OR b='';
  ```

* ```
  #using where:（需要回表查询）
  EXPLAIN SELECT a,c FROM test02 WHERE c='';
  ```

* ```
  #impossible where: where子句永远为false
  EXPLAIN SELECT a FROM test02 WHERE a='1' and a='2';	#impossible where
  ```

##### 优化案例

###### 单表优化

* ```
  CREATE TABLE book(
  				  bid INT(4),
				  name VARCHAR(20) NOT NULL,
  				  aid INT(4) NOT NULL,
  				  pid INT(4) NOT NULL,
  				  tid INT(4) NOT NULL,
  				  PRIMARY KEY(bid)
  				  );
  INSERT INTO book VALUES(1,'java',1,1,2);
  INSERT INTO book VALUES(2,'c',2,1,2);
  INSERT INTO book VALUES(3,'python',3,2,1);
  INSERT INTO book VALUES(4,'go',4,2,3);
  #查询aid=1且 tid为2或3的	bid
  EXPLAIN SELECT bid FROM book WHERE tid IN(2,3) AND aid=1 ORDER BY tid DESC;		# tid aid bid
  #优化 
  #from .. on.. join ..where ..group by ....having ...select dinstinct ..order by limit ...
  ALTER TABLE book ADD INDEX tid_aid_bid(tid,aid,bid);
  #优化
  DROP INDEX tid_aid_bid ON book;
  CREATE INDEX aid_tid_bid ON book(aid,tid,bid);
  EXPLAIN SELECT bid FROM book WHERE aid=1 AND tid IN(2,3) ORDER BY tid DESC;
  ```

###### 两表优化

* ```
  #小表驱动大表 数据量小的表放左边 数据量大的表放右边 t.cid=c.cid 10 300
  CREATE TABLE teacher2(
  					  tid INT(4) PRIMARY KEY,
  					  cid INT(4) NOT NULL
  					  );
  CREATE TABLE course2(
  					cid INT(4),
  					cname VARCHAR(20)
  					);
  INSERT INTO teacher2 VALUES(1,2);
  INSERT INTO teacher2 VALUES(2,1);
  INSERT INTO teacher2 VALUES(3,3);
  
  INSERT INTO course2 VALUES(1,'java');
  INSERT INTO course2 VALUES(2,'python');
  INSERT INTO course2 VALUES(3,'c');
  
  EXPLAIN SELECT * FROM teacher2 t LEFT OUTER JOIN course2 c ON t.cid=c.cid WHERE c.cname='c';
  #Using join buffer: Mysql引擎使用了 连接缓存
  #优化
  ALTER TABLE teacher2 ADD INDEX cid_index(cid);
  ALTER TABLE course2 ADD INDEX cname_index(cname);
  ```

###### 多表优化

* ```
  小表驱动大表 
  索引建立在经常查询的字段上
  ```

###### 避免索引失效的原则

* ```
  a.复合索引，不要跨列或无序使用（最佳左前缀）
  	对于复合索引，如果左边失效，右侧全部失效。(a,b,c)，例如如果 b失效，则b c同时失效。
  b.复合索引，尽量使用全索引匹配(建立的索引全都用上)
  ```

* ```
  #不要在索引上进行任何操作（计算、函数、类型转换），否则索引失效
  EXPLAIN SELECT * FROM book WHERE aid=1 AND tid=2;
  EXPLAIN SELECT * FROM book WHERE aid=1 AND tid*2=2; 
  EXPLAIN SELECT * FROM book WHERE aid*2=1 AND tid=2;	#复合索引atb aid失效 所以tid失效
  EXPLAIN SELECT * FROM book WHERE aid*2=1 AND tid*2=2;
  ```

* ```
  #复合索引不能使用不等于（!=  <>）或is null (is not null)，否则自身以及右侧所有全部失效
  DROP INDEX aid_tid_bid ON book;
  ALTER TABLE book ADD INDEX aid_index(aid);
  ALTER TABLE book ADD INDEX tid_index(tid);
  EXPLAIN SELECT * FROM book WHERE aid=1;	#type ref
  #原因是服务层中有SQL优化器，可能会影响我们的优化
  EXPLAIN SELECT * FROM book WHERE aid!=1;	#type range
  #概率情况
  DROP INDEX aid_index ON book;
  DROP INDEX tid_index ON book;
  CREATE INDEX aid_tid ON book(aid,tid);
  EXPLAIN SELECT * FROM book WHERE aid=1 and tid=2;
  #一般而言， 范围查询（> <  in），之后的索引失效
  EXPLAIN SELECT * FROM book WHERE aid>1 and tid=2;
  #补救
  #尽量使用索引覆盖: using index 提高系统性能
  EXPLAIN SELECT tname FROM teacher WHERE tname LIKE '%w%';
  #like尽量以“常量”开头，不要以'%'开头，否则索引失效
  EXPLAIN SELECT * FROM teacher WHERE tname LIKE '%w%';
  EXPLAIN SELECT * FROM teacher WHERE tname LIKE 't%';
  ```

* ```
  #尽量不要使用类型转换（显示、隐式），否则索引失效
  EXPLAIN SELECT * FROM teacher WHERE tname='123';
  EXPLAIN SELECT * FROM teacher WHERE tname=123;	#程序底层将 123 -> '123'
  #尽量不要使用or，否则索引失效
  EXPLAIN SELECT * FROM teacher WHERE tname='' AND tid >1;
  #OR将左侧,右侧的索引置为失效
  EXPLAIN SELECT * FROM teacher WHERE tname='' OR tid >1;
  ```

###### 其他优化方法

* exist语法： **将主查询的结果，放到子查需结果中进行条件校验**（看子查询是否有数据，如果有数据 则校验成功，如果 符合校验，则保留数据)

* ```
  #exist和in
  #select ..from table where exist (子查询) ;
  #select ..from table where 字段 in (子查询) ;
  #如果主查询的数据集大，则使用In   ,效率高。
  #如果子查询的数据集大，则使用exist,效率高。	
  
  #exists
  SELECT tname FROM teacher WHERE EXISTS (SELECT * FROM teacher);
  SELECT tname FROM teacher WHERE EXISTS (SELECT * FROM teacher WHERE tid=999); #EXISTE (null)
  #in
  SELECT tname FROM teacher WHERE tid IN (SELECT tid FROM teacher WHERE tid<3);
  ```

* ```
  #order by 优化
  #using filesort 有两种算法: 双路排序、单路排序 (根据IO的次数)
  #调大buffer的容量大小
  #set max_length_for_sort_data = 1024  单位byte
  ```

###### SQL排查 - 慢查询日志

* ```
  #MySQL提供的一种日志记录，用于记录MySQL种响应时间超过阀值的SQL语句 （long_query_time，默认10秒）
  #检查是否开启了 慢查询日志:   
  SHOW VARIABLES LIKE '%slow_query_log%';
  #临时开启：
  SET GLOBAL slow_query_log = 1 ;  --在内存种开启
  #永久开启：
  /etc/my.cnf 中追加配置：
  $vi /etc/my.cnf 
  [mysqld]
  slow_query_log=1
  slow_query_log_file=/var/lib/mysql/my_slow.log
  #阀值
  SHOW VARIABLES LIKE '%long_query_time%';
  #临时阀值：
  SET GLOBAL long_query_time = 5 ; --设置完毕后，重新登陆后起效 （不需要重启服务）
  #永久阀值：		
  /etc/my.cnf 中追加配置：
  $vi /etc/my.cnf 
  [mysqld]
  long_query_time=3
  #查询超过阀值的SQL
  SELECT SLEEP(4);
  SHOW GLOBAL STATUS LIKE '%slow_queries%';
  #查看慢SQL
  $cat /var/lib/mysql/my_slow.log
  ```

* ```
  #mysqldumpslow
      #s：排序方式
      #r:逆序
      #l:锁定时间
      #g:正则匹配模式	
  $mysqldumpslow -s r -t 3 /var/lib/mysql/my_slow.log
  $mysqldumpslow -s t -t 10 -g "left join" /var/lib/mysql/localhost-slow.log
  ```

###### 存储函数

* ```
  CREATE DATABASE testdata;
  USE testdata;
  CREATE TABLE dept(
  				  did INT(5) PRIMARY KEY,
  				  dname VARCHAR(20) NOT NULL DEFAULT '',
  				  loc VARCHAR(30) DEFAULT ''
  				  )ENGINE=innodb DEFAULT CHARSET=utf8;
  CREATE TABLE emp(
  				eid INT(5) PRIMARY KEY,
  				ename VARCHAR(20) NOT NULL DEFAULT '',
  				job VARCHAR(20) NOT NULL DEFAULT '',
  				deptid INT(5) NOT NULL DEFAULT 0
  				)ENGINE=innodb DEFAULT CHARSET=utf8;
  ```

* ```
  #存储过程/存储函数在创建时与开启慢查询日志冲突
  #临时解决( 开启log_bin_trust_function_creators )
  SHOW VARIABLES LIKE '%log_bin_trust_function_creators%';
  SET GLOBAL log_bin_trust_function_creators=1;
  #永久解决：
  $vim /etc/my.cnf 
  [mysqld]
  log_bin_trust_function_creators = 1
  ```

* ```
  #有return
  #产生随机字符串
  DELIMITER $
  CREATE FUNCTION randstring(n INT) RETURNS VARCHAR(255)
      BEGIN
  		DECLARE all_str VARCHAR(100) DEFAULT 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
  		DECLARE return_str VARCHAR(255) DEFAULT '';
  		DECLARE i INT DEFAULT 0;
  		WHILE i<n
              DO
  				SET return_str=CONCAT(return_str,SUBSTRING(all_str,FLOOR(RAND()*52+1),1));
  				SET i=i+1;
              END WHILE;
          RETURN return_str;
      END$
  ```

* ```
  #产生随机整数
  CREATE FUNCTION rand_num() RETURNS INT(5)
      BEGIN
      	DECLARE i INT DEFAULT 0;
      	SET i=FLOOR(RAND()*100);
      	RETURN i;
      END$
  ```

###### 存储过程

* ```
  #无return
  #emp表
  CREATE PROCEDURE insert_emp(IN eid_start INT(10),IN data_times INT(10))
      BEGIN
  		DECLARE i INT DEFAULT 0;
  		SET AUTOCOMMIT=0;
  		REPEAT
  			INSERT INTO emp VALUES(eid_start+i,randstring(5),'other',rand_num());
  			SET i=i+1;
  			UNTIL i=data_times
  		END REPEAT;
  		COMMIT;
      END$
  ```

* ```
  #dept表
  CREATE PROCEDURE insert_dept(IN did_start INT(10),IN data_times INT(10))
      BEGIN
  		DECLARE i INT DEFAULT 0;
  		SET AUTOCOMMIT=0;
  		REPEAT
  			INSERT INTO dept VALUES(did_start+i,randstring(6),randstring(8));
  			SET i=i+1;
  			UNTIL i=data_times
  		END REPEAT;
  		COMMIT;
      END$
  ```

###### 分析海量数据

* ```
  TRUNCATE TABLE emp;	#清空表
  #插入数据
  DELIMITER ; 
  CALL insert_emp(1000,800000);
  CALL insert_dept(10,30);
  ```

* ```
  SHOW VARIABLES LIKE '%profiling%';
  SET profiling = on ; 
  SHOW PROFILES;  
  #会记录所有profiling打开之后的  全部SQL查询语句所花费的时间。缺点：不够精确，只能看到 总共消费的时间，不能看到各个硬件消费的时间（cpu  io ）
  SHOW PROFILE ALL FOR QUERY Query_ID;
  SHOW PROFILE cpu,block io FOR QUERY Query_ID;
  ```

* ```
  #全局查询日志 ：记录开启之后的 全部SQL语句。
  #这次全局的记录操作 仅仅在调优、开发过程中打开即可，在最终的部署实施时 一定关闭
  SHOW VARIABLES LIKE '%general_log%';
  #执行的所有SQL记录在表中
  SET GLOBAL general_log=1;		#开启全局日志
  SET GLOBAL log_output='table'; 	#设置将全部的SQL 记录在表中
  #开启后，会记录所有SQL ： 会被记录 mysql.general_log表中。
  SELECT * FROM mysql.general_log;
  #执行的所有SQL记录在文件中
  SET GLOBAL general_log=1;
  SET GLOBAL log_output='file';
  SET GLOBAL general_log_file='~/Documents/general.log';
  ```

##### 锁

* 锁机制 : 解决因**资源共享** 而**造成的并发问题**

* 操作类型：
  	a.读锁（**共享锁**）：对同一个数据，多个读操作可以同时进行，互不干扰。
      b.写锁（**互斥锁**）：如果当前写操作没有完成，则无法进行其他的读操作、写操作

* 操作范围：
  	a.表锁 ：一次性对一张表整体加锁。如MyISAM存储引擎使用表锁，**开销小、加锁快；无死锁**；但***锁的范围大，容易发生锁冲突、并发度低***。
      b.行锁 ：一次性对一条数据加锁。如InnoDB存储引擎使用行锁，***开销大，加锁慢；容易出现死锁***；**锁的范围较小，不易发生锁冲突，并发度高**（很小概率 发生高并发问题：脏读、幻读、不可重复度、丢失更新等问题）。
      c.页锁	

* ```
  #表锁
  CREATE TABLE table_lock(
  						id INT PRIMARY KEY AUTO_INCREMENT,
  						name VARCHAR(20)
  						)ENGINE=MYISAM DEFAULT CHARSET=utf8;
  INSERT INTO table_lock(name) VALUES('A1');
  INSERT INTO table_lock(name) VALUES('A2');
  INSERT INTO table_lock(name) VALUES('A3');
  INSERT INTO table_lock(name) VALUES('A4');
  INSERT INTO table_lock(name) VALUES('A5');
  INSERT INTO table_lock(name) VALUES('A6');
  ```

* 会话 session 只针对当前会话

  * 如果某一个会话 对A表加了read锁，则该会话 可以对A表进行读操作 不能进行写操作;且该会话不能对其他表进行读、写操作
    * 即如果给A表加了读锁，则当前会话只能对A表进行读操作
  * 会话0给A表加了锁；其他会话的操作：
    * a.可以对其他表（A表以外的表）进行读、写操作
    * b.对A表：读-可以; 写-需要等待释放锁

* ```
  #增加锁：
  	#LOCK TABLE 表1 READ/WRITE,表2 READ/WRITE, ...
  #查看加锁的表：
  SHOW OPEN TABLES;
  LOCK TABLE table_lock READ;		#读锁
  #释放锁:
  UNLOCK TABLES;
  LOCK TABLE table_lock WRITE;	#写锁
  MySQL表级锁的锁模式
  MyISAM在执行查询语句（SELECT）前，会自动给涉及的所有表加读锁，
  在执行更新操作（DML）前，会自动给涉及的表加写锁。
  所以对MyISAM表进行操作，会有以下情况：
  a、对MyISAM表的读操作（加读锁），不会阻塞其他进程（会话）对同一表的读请求，
  但会阻塞对同一表的写请求。只有当读锁释放后，才会执行其它进程的写操作。
  b、对MyISAM表的写操作（加写锁），会阻塞其他进程（会话）对同一表的读和写操作，
  只有当写锁释放后，才会执行其它进程的读写操作。
  ```

* ```
  #分析表锁定的严重程度： 
  SHOW STATUS LIKE 'table%';
      #Table_locks_immediate :即可能获取到的锁数
      #Table_locks_waited：需要等待的表锁数(如果该值越大，说明存在越大的锁竞争)
  #一般建议：
  		Table_locks_immediate/Table_locks_waited > 5000， 建议采用InnoDB引擎，否则MyISAM引擎
  ```

* ```
  #行锁
  CREATE TABLE line_lock(
  					   id INT PRIMARY KEY AUTO_INCREMENT,
  					   name VARCHAR(20)
  					   )ENGINE=INNODB;
  INSERT INTO line_lock(name) VALUES('B1');
  INSERT INTO line_lock(name) VALUES('B2');
  INSERT INTO line_lock(name) VALUES('B3');
  INSERT INTO line_lock(name) VALUES('B4');
  INSERT INTO line_lock(name) VALUES('B5');
  ```

* ```
  SHOW VARIABLES LIKE '%autocommit%';
  SET autocommit=0;	#关闭自动提交事务
  #开启事务
  START TRANSACTION;
  BEGIN;
  ```

* ```
  #如果会话n对某条数据a进行DML操作(关闭autocommit),则其他会话必须等待会话n结束事务(COMMIT/ROLLBACK)后  才能对数据a进行操作。
  #SESSION 0
  INSERT INTO line_lock VALUES(6,'B6');
  #SESSION 1
  UPDATE line_lock SET name='C6' WHERE id=6;
  #SESSION 0
  COMMIT;/ROLLBACK;
  #SESSION 1
  COMMIT;/ROLLBACK;
  ```

* ```
  #行锁
  #如果没有索引,则行锁会转为表锁
  #SESSION 0
  UPDATE line_lock SET name='A1' WHERE name='1';
  #SESSION 1
  UPDATE line_lock SET name='A2' WHERE name='2';
  #添加索引
  ALTER TABLE line_lock ADD INDEX name_index(name);
  #类型转换 索引失效 WHERE name=1; WHERE name='1';
  UPDATE line_lock SET name='A1' WHERE name=1;
  UPDATE line_lock SET name='A2' WHERE name=2;
  #行锁的一种特殊情况:间隙锁：值在范围内，但却不存在
  UPDATE line_lock SET name='xx' WHERE id>1 AND id<10;
  #Mysql会自动给间隙 加索 ->间隙锁
  #where : 实际加索的范围
  ```

* ```
  #查询数据加锁
  #通过FOR UPDATE对query语句进行加锁
  SELECT * FROM line_lock WHERE id=2 FOR UPDATE;
  ```

* ```
  SHOW STATUS LIKE '%innodb_row_lock%';
      Innodb_row_lock_current_waits	#当前正在等待锁的数量  
      #时间 : 从系统启到当前时间点
      Innodb_row_lock_time			#等待总时长
      Innodb_row_lock_time_avg		#平均等待时长
      Innodb_row_lock_time_max		#最大一次等待时长
      Innodb_row_lock_waits			#一共等待次数
  ```

###### 主从复制 : 读写分离

* ```
  winsat disk -driver D/S
  ```

* ```
  SHOW PROCESSLIST;
  ```

* ```
  binlog		:二进制日志
  relaylog	:中继日志
  $/usr/share/mysql/my-default.cnf
  ```

* ```
  #master
  [mysqld]
  server-id               = 1
  log_bin                 = /var/log/mysql/mysql-bin.log
  ```

* ```
  $mysqlbinlog --start-position=0 /var/log/mysql/mysql-bin.000001
  SHOW MASTER STATUS;
  SHOW BINLOG EVENTS IN 'mysql-bin.000002' FROM 0;
  #master
  USE mysql;
  CREATE USER 'repl'@'192.168.101.%' IDENTIFIED BY 'root'; 
  SELECT user,host FROM user;
  #开放主从复制权限
  GRANT REPLICATION SLAVE ON *.* TO 'repl'@'192.168.101.%';
  FLUSH PRIVILEGES;
  #slave
  STOP SLAVE;
  SHOW SLAVE STATUS;	#查看通信状态
  SHOW RELAYLOG EVENTS IN 'localhost-relay-bin.000002' FROM 0;
  #master SHOW MASTER STATUS; mysql-bin.000002
  CHANGE MASTER TO master_host='192.168.101.27',master_user='repl',master_password='root',master_log_file='mysql-bin.000002',master_log_pos=880;
  START SLAVE;
  ```

#### COOKBOOK

##### Percona工具包

* ```
  #安装
  https://www.percona.com/downloads/percona-toolkit/LATEST/
  sudo dpkg -i percona-toolkit_3.2.0-1.focal_amd64.deb
  sudo apt-get install -f
  ```
  
* ```
  #pt-query-digest分析慢查询日志
  chmod -R 777 /var/lib/mysql/
  sudo pt-query-digest /var/lib/mysql/my_slow.log
  Rank Query ID                           Response time Calls R/Call  V/M 
  ==== ================================== 响应时间===全部查询响应时间占比=执行次数=平均查询时间======= ====
  1 0x98754635E4A2BD0A62C7F17FEBCDF619 48.7712 77.7%     1 48.7712  0.00 CALL insert_emp
  #通用查询日志
  sudo pt-query-digest --type genlog /var/lib/mysql/db1.log
  #二进制日志
  sudo pt-query-digest --type binlog /var/lib/mysql/binlog.000001
  #进程列表
  sudo pt-query-digest --processlist h=localhost --iterations 10 --run-time 1m -u root -p root	#迭代10次 每分钟1次
  #TCP转存
  sudo tcpdump -s 65535 -x -nn -q -tttt -i any -c 1000 port 3306 > mysql.tcp.txt
  sudo pt-query-digest --type tcpdump mysql.tcp.txt
  ```
##### 索引

* ```
  CREATE TABLE emp(
  eid INT(11) PRIMARY KEY,
  birth DATE,
  first_name VARCHAR(20),
  last_name VARCHAR(20),
  gender ENUM('1','0'),
  KEY name(first_name,last_name)
  )ENGINE=INNODB DEFAULT CHARSET=utf8;
  #前缀索引
  ALTER TABLE emp ADD INDEX (last_name(5));	#last_name最大长度20个字符,但索引只基于前5个字符创建
  #封装在函数中的列不能使用索引
  ALTER TABLE emp ADD INDEX birth_index(birth);
  EXPLAIN SELECT COUNT(*) FROM emp WHERE birth>'2010-01-01';
  EXPLAIN SELECT COUNT(*) FROM emp WHERE YEAR(birth)>=2010;
  #添加虚拟列
  ALTER TABLE emp ADD birth_year YEAR AS (YEAR(birth)) VIRTUAL,ADD INDEX year_index(birth_year);
  EXPLAIN SELECT COUNT(*) FROM emp WHERE birth_year>=2000;
  #优化器构建执行计划时会认识到YEAR()与birth_year的定义匹配,会考虑year_index索引
  EXPLAIN SELECE COUNT(*) FROM emp WHERE YEAR(birth)>=2000;
  #不可见索引
  ALTER TABLE emp ALTER INDEX last_name INVISBLE;
  ALTER TABLE emp ALTER INDEX last_name VISBLE;
  #降序索引
  DROP INDEX name ON emp;
  ALTER TABLE emp ADD INDEX name_desc(first_name ASC,last_name DESC);
  EXPLAIN SELECT * FROM emp ORDER BY first_name ASC,last_name DESC LIMIT 10;	#Using index
  EXPLAIN SELECT * FROM emp ORDER BY first_name DESC,last_name ASC LIMIT 10;	#向后索引扫描Backward index scan
  ```

* ```
  #给出差不多的数据类型 MYSQL8已弃用
  SELECT eid,first_name,last_name FROM emp PROCEDURE ANALYSE(1,100)\G
  ```

##### 删除索引

* ```
  #减慢插入速度
  重复索引 : 重复定义相同的索引(相同的列,相同的列顺序,相同的键顺序)
  冗余索引 : 部分索引重复(最左边的列)
  #pt-duplicate-key-checker
  pt-duplicate-key-checker -u root -p root	#给出精确的删除语句
  ```

##### 查询优化器

###### 贪婪搜索算法

* ```
  
  ```

###### 启发式算法

* ```
  
  ```

* ```
  SHOW VARIABLES LIKE 'optimizer_search_depth';
  SHOW VARIABLES LIKE 'optimizer_switch';		#是一组标志 控制优化器行为
  #会话级别关闭优化器选项
  SET @@SESSION.optimizer_switch='index_merge_sort_union=off';
  ```

* ```
  #优化器提示
  #优化器提示的作用范围仅限查询的语句
  EXPLAIN SELECT /*+ NO_INDEX_MERGE(emp first_index,last_index) */ *FROM emp WHERE first_name='Adam' OR last_name='Adam';		#关闭sort_union
  EXPLAIN SELECT /*+ JOIN_ORDER(s,e) */ e.eid, salary FROM salaries s JOIN emp e ON s.eid=e.eid;		#改变表的连接顺序
  #优化器利用sort_buffer_size(默认值256k)来提升排序速度
  #sort_buffer_size的值不够大则排序算法必须执行的合并传递次数就会增加
  SHOW SESSION STATUS LIKE 'sort_merge_passes';	#会话变量统计合并传递次数
      pager grep 'rows in set';
      SELECT /*+ SET_VAR(sort_buffer_size=16M) */ * FROM emp ORDER BY birth DESC;
      nopager;
  #设置语句级别的optimizer_switch
  EXPLAIN SELECT /*+ SET_VAR(optimizer_switch='index_merge_sort_union=off') */ e.eid,salary FROM salarys s JOIN emp e ON s.eid=e.eid;
  #设置最长查询时间
  SELECT /*+ MAX_EXECUTION_TIME(100) */ * FROM emp ORDER BY first_name DESC;
  #优化器成本模型
  SELECT * FROM mysql.engine_cost;
  UPDATE mysql.engine_cost SET cost_value=0.5 WHERE cost_name='io_block_read_cost';
  FLUSH OPTIMIZER_COSTS;
  ```

* ```
  #忽略索引
  EXPLAIN SELECT e.eid,salary FROM salarys s IGNORE INDEX(form_date) JOIN emp e ON s.eid=e.eid WHERE form_date='2001-01-01';
  #用那些索引	这样就避免扫描其他索引
  EXPLAIN SELECT eid FROM emp USE INDEX(first_index,last_index) WHERE first_name='Adam' OR last_name='Adam';
  ```

* ```
  #JSON 列上不能直接建立索引
  #使用虚拟列和在虚拟列上创建索引来提取信息
  CREATE TABLE emp_json(
  					 eid INT(5) PRIMARY KEY AUTO_INCREMENT,
  					 data JSON DEFAULT NULL
  					 )ENGINE=INNODB DEFAULT CHARSET=utf8;
  INSERT IGNORE INTO emp_json(eid,data) VALUES
  (1,'{"phone":"100","address":{"city":"BeiJing","pin":"1001"}}'),
  (2,'{"phone":"102","address":{"city":"Shanghai","pin":"1002"}}'),
  (3,'{"phone":"103","address":{"city":"DaLian","pin":"1003"}}'),
  ('4','{"phone":"104","address":{"city":"Shen","pin":"1004"}}');
  EXPLAIN SELECT eid FROM emp_json WHERE data->>'$.address.city'='BeiJing';	#key=null
  ALTER TABLE emp_json ADD COLUMN city VARCHAR(20) AS (data->>'$.addres.city') VIRTUAL,ADD INDEX city_index(city);
  EXPLAIN SELECT eid FROM emp_json WHERE city='BeiJing';	#key=city_index
  ```

* ```
  #资源组	资源组只限本地服务器使用 服务器之间不复制任何与资源组相关的语句
  #为MySQL设置CAP_SYS_NICE
  ps aux|grep mysqld|grep -v grep
  sudo setcap cap_sys_nice+ep /usr/sbin/mysqld 
  getcap /usr/sbin/mysqld 
  #VCPU为CPU编号 TYPE有USER priority=0~19 SYSTEM priority -20~0 -20最高级 19最低级
  CREATE RESOURCE GROUP rg TYPE=USER VCPU=2-3 THREAD_PRIORITY=15 ENABLE;		#需要有Mysql动态权限
  #https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_resource-group-admin
  SELECT * FROM INFORMATION_SCHEMA.RESOURCE_GROUPS;
  #分配资源组
  SET RESOURCE GROUP rg FOR <thread_id>;		#分配线程
  SET RESOURCE GROUP rg;		#会话级别资源组
  select /*+ RESOURCE GROUP(rg) */ * FROM emp;	#优化器提示执行rg
  #动态调整资源组
  ALTER RESOURCE GROUP rg VCPU=3 THREAD_PRIORITY=19;
  ALTER RESCURCE GROUP rg DISABLE FORCE;
  DROP RESCURCE GROUP rg FORCE;
  #FORCE
      #使用 运行的线程将被迁至默认资源组
      #不使用 资源组中的现有线程将继续运行,直到终止,但不能为这个资源组分配新线程
  ```

##### 修改表结构

* ```
  #修改表操作的两种算法
      #in-place : (就地)不需要复制整个表的数据
      #copy : 将数据复制到一个临时的磁盘文件中并重命名
  	#rows affected 标识
  ALTER TABLE emp ADD COLUMN addr VARCHAR(100);	#0
  #修改
  ALTER TABLE emp MODIFY COLUMN addr VARCHAR(250);	#0
  ALTER TABLE emp MODIFY COLUMN addr TINYTEXT;	#(#table)
  #添加虚拟列: 元数据发生变化
  ALTER TABLE emp ADD COLUMN full_name VARCHAR(40) AS (CONCAT('first_name','++','last_name'));		#0
  ALTER TABLE emp MODIFY COLUMN full_name VARCHAR(40) AS (CONCAT('first_name','--','last_name'));		#(#table)
  ```

* ```
  #移动表
  RENAME TABLE emp TO emp_old;		#0
  RENAME TABLE mydb.emp_old TO mydbtest.emp_new;	#0
  ```

* ```
  #更改列的数据类型,添加spatial index,删除主键,转换字符集,添加/删除 加密操作...
  #对表的DML操作阻塞
  #在线修改工具pt-online-schema-change 仅在有主键或唯一键时起作用
  pt-online-schema-change D=mydb,t=emp,h=192.168.101.27 -u root --ask-pass --alter='ADD COLUMN addr CHAR(40)' --alter-foreign-keys-method=auto --execute
  #--preserver-triggers
  #--check-slave-lag  --max-lag
  ```

* ```
  #归档表
  DELETE FROM <table> WHERE time_add<DATE_ADD(NOW(),INTERVAL -1 MONTH);	#(#TABLE)<10000
  #如果DELETE语句在执行期间中止,INNODB将从UNDO日志空间将行复制到表中,这可能使表无法访问
  ```

* ```
  #pt-archiver 
  pt-archiver --source D=mydb,t=emp,h=192.168.101.27 -u root -p root --where='birth<DATE_ADD(NOW(),INTERVAL -10 YEAR)' --no-check-charset --limit 1000 --commit-each
  pt-archiver --source D=mydb,t=emp,h=192.168.101.27 -u root -p root --dest h=192.168.101.27,D=mydbtest -uroot -p root --where='1=1' --no-check-charset --limit 1000 --commit-each --no-delete	#不会从原表删除行
  ```

* ```
  #克隆表
  CREATE TABLE emp_clone LIKE emp;	#关系scham
  INSERT INTO emp_clone SELECT * FROM emp;	#如果有生成列,则报错
  INSERT INTO emp_clone(eid,....) SELECT eid,... FROM emp;
  #如果语句执行失败,为了恢复状态,INNODB会将所有的行保存在UNDO日志中
  ```

##### 表分区

* 分区仅适用于INNODB表,并且外键不能和分区结合使用

* ```
  #数据库分区的一个非常常见的用途: 按日期分隔数据
  #分区函数 partitioning function : 划分数据的规则
  	#可以是模量modulu,与一组范围或值列表 一个内部哈希函数 一个线性哈希函数简单匹配
  	#水平分区 : 表的不同行可以被分配给不同的物理分区
  	#垂直分区 : 表的不同列可以被分配给不同的物理分区 MYSQL不支持垂直分区
  RANGE	RANGE COLUMNS
  LIST	LIST COLUMNS
  HASH	LINEAR HASH
  KEY		LINEAR KEY
  ```

* ```
  #分区列应该是表中所有唯一键的一部分
  #期望基于范围或时间间隔实施分区计划,有两种选择
  	#按RANGE分区,对于分区表达式,应用在 DATE TIME DATETIME列上运行函数,返回一个整数值
  	#按RANGE COLUMNS分区,使用 DATE DATETIME列作为分区列
  ```

* ```
  #RANGE分区
  CREATE TABLE emp2(
  				  eid INT(11) NOT NULL,
  				  birth_date DATE NOT NULL,
  				  first_name VARCHAR(20) NOT NULL,
  				  last_name VARCHAR(20) NOT NULL,
  				  gender ENUM('1','0') NOT NULL,
  				  hire_date DATE NOT NULL,
  				  addr VARCHAR(100) DEFAULT NULL,
  				  PRIMARY KEY(eid),
  				  KEY name(first_name ASC,last_name(10) DESC)
  				  )ENGINE=INNODB DEFAULT CHARSET=utf8 
  				  PARTITION BY RANGE(eid)
  				  (
  				  PARTITION p0 VALUES LESS THAN (10000) ENGINE=INNODB,
  				  PARTITION p1 VALUES LESS THAN (20000) ENGINE=INNODB,
  				  PARTITION p2 VALUES LESS THAN (30000) ENGINE=INNODB,
  				  PARTITION p3 VALUES LESS THAN (40000) ENGINE=INNODB,
  				  PARTITION p4 VALUES LESS THAN (50000) ENGINE=INNODB,
  				  PARTITION pMAX VALUES LESS THAN MAXVALUE ENGINE=INNODB
  				  );
  #MAXVALUE : 避免员工编号大于50000时,插入报错
  #若想基于hire_date建立分区, 修改两部分
      #PRIMARY KEY(eid,hire_date),
      #PARTITION BY RANGE(YEAR(hire_date))
  #to_days
  	create_at DATATIME NOT NULL,
  	PARTITION BY RANGE(TO_DAYS(create_at))
  #建表后
  ALTER TABLE emp2 DROP PRIMARY KEY,ADD PRIMARY KEY(eid,hire_date);
  ALTER TABLE emp2 PARTITION BY RANGE(YEAR(hire_date))
  (
  	PARTITION p1980 VALUES LESS THAN (1980) ENGINE=INNODB,
  	...
  	PARTITION pMAX VALUES LESS THAN MAXVALUE ENGINE=INNODB
  );
  #删除分区
  ALTER TABLE emp2 REMOVE PARTITIONING;
  ```

* ```
  #RANGE COLUMNS分区
  #不接受表达式,只接受列的名称
  #允许使用基于多个列值的范围来定义分区
  #允许使用非整数类型的列来定义范围
  ALTER TABLE emp2 PARTITION BY RANGE COLUMNS(hire_date)
  (
  	PARTITION p1980 VALUES LESS THAN (1980) ENGINE=INNODB,
  	...
  	PARTITION pMAX VALUES LESS THAN MAXVALUE ENGINE=INNODB
  );
  #在分区函数中放置多个列
  CREATE TABLE range_columns(
  							a INT,
  							b INT,
  							c INT,
  							d INT,
  							e INT,
  							PRIMARY KEY(a,b,c)
  							)PARTITION BY RANGE COLUMNS(a,b,c)
  							(
  							PARTITION p0 VALUES LESS THAN (0,25,50),
  							PARTITION p1 VALUES LESS THAN (10,50,100),
  							PARTITION p2 VALUES LESS THAN (10,100,200),
  							PARTITION pMAX VALUES LESS THAN (MAXVALUE,MAXVALUE,MAXVALUE)
  							);
  #比较所需的元组来测试连续分区的定义
  SELECT (10,20,100)<(0,25,50) p0,(10,20,100)<(10,50,100) p1,(10,20,100)<(10,100,200)p2;
  ```

* ```
  #LIST 分区
  #每个分区都是根据一组值列表中的一个列值的成员来定义和选择的
  CREATE TABLE emp_list(
  					  eid INT(5),
  					  zcode INT,
  					  city VARCHAR(100),
  					  PRIMARY KEY(eid,zcode)
  					  )ENGINE=INNODB DEFAULT CHARSET=utf8 
  					  PARTITION BY LIST(zcode)
  					  (
  					  PARTITION p0 VALUES IN (560030,56007,560051,560084),
  					  PARTITION p0 VALUES IN (560030,56007,560051,560084)
  					  );
  LIST COLUMNS分区
  #直接使用列而不是整数
  CREATE TABLE emp_list_columns(
  							  eid INT(5),
  							  zcode INT,
  							  city VARCHAR(100),
  							  PRIMARY KEY(eid,zcode)
  							  )ENGINE=INNODB DEFAULT CHARSET=utf8 
  							  PARTITION BY LIST COLUMNS(city) 
  							  (
  							  PARTITION c0 VALUES IN ('city1','city2','city3'),
  							  PARTITION c1 VALUES IN ('city4','city5','city6')
  							  );
  ```

* ```
  #HASH 分区
  #HASH分区确保数据均匀地分布在数量预先确定的一组分区中
  #a.根据要进行哈希的列值指定一个列值或表达式
  #b.分区表要分为多少个分区
  CREATE TABLE emp_hash(
  					  eid INT(5),
  					  hire_date DATE,
  					  PRIMARY KEY(eid,hire_date)
  					  )ENGINE=INNODB DEFAULT CHARSET=utf8 
  					  PARTITION BY HASH(YEAR(hire_date)) 
  					  PARTITIONS 8;
  #例 hire_date='1987-11-28' YEAR(hire_date)=1987 MOD(1987,8)=3 (8个分区) 这行被分到第3分区
  #效率最高的哈希函数是对单个列进行操作的函数,其值与该列值同步地增加或减少
  #LINEAR HASH分区
  #MySQL不使用modulus操作,而是使用2的幂算法来确定分区
  CREATE TABLE emp_linear_hash(
  					  eid INT(5),
  					  hire_date DATE,
  					  PRIMARY KEY(eid,hire_date)
  					  )ENGINE=INNODB DEFAULT CHARSET=utf8 
  					  PARTITION BY LINEAR HASH(YEAR(hire_date)) 
  					  PARTITIONS 8;
  ```

* ```
  #KEY LINEAR KEY分区
  #KEY分区的哈希函数由MySQL服务器提供(这个内部哈希函数采用的是与PASSWORD()函数相同的算法)
  #如果表有主键,则用作KEY分区的任何列都必须是主键的一部分或全部
  #如果没有列名可以被指定为分区键,则使用表的主键
  CREATE TABLE emp_key(
  					  eid INT(5),
  					  hire_date DATE,
  					  PRIMARY KEY(eid,hire_date)
  					  )ENGINE=INNODB DEFAULT CHARSET=utf8 
  					  PARTITION BY KEY() 
  					  PARTITIONS 8;
  ```

* ```
  #子分区 复合分区
  #每个分区进一步划分为一个分区表
  CREATE TABLE emp_sub(
  					  eid INT(5),
  					  hire_date DATE,
  					  PRIMARY KEY(eid,hire_date)
  					  )ENGINE=INNODB DEFAULT CHARSET=utf8 
  					  PARTITION BY RANGE(YEAR(hire_date))
                        SUBPARTITION BY HASH(eid)
                        SUBPARTITIONS 4 
                        (
                        PARTITION p0 VALUES LESS THAN (1990),
                        PARTITION p1 VALUES LESS THAN (2000),
                        PARTITION p2 VALUES LESS THAN (2010),
                        PARTITION p3 VALUES LESS THAN (2020),
                        PARTITION pMAX VALUES LESS THAN MAXVALUE,
                        );
  ```

* ```
  #分区修剪 partition pruning
  #MySQL不扫描没有匹配值的分区(自动操作)
  #对给定的值,MySQL优化器会计算分区表达式,以确定哪个分区包含该值,并且只扫描这个分区
  #分区修剪只适用于查询语句
  #查询中显示地指定要扫描的分区 选项之前 表明之后
  SELECT * FROM emp_sub PARTITION (p1990) LIMIT 10;
  DELETE FROM emp_sub PARTITION (p1990,p2000) WHERE eid>'';
  ```

* ```
  #添加新分区
  #不存在MAXVALUE分区
  ALTER TABLE emp_range ADD PARTITION(
  									PARTITION p6 VALUES LESS THAN (...) ENGINE=INNODB,
  									PARTITION p7 VALUES LESS THAN (...) ENGINE=INNODB,
  									);
  #存在MAXVALUE分区
  ALTER TABLE emp_range REORGANIZE PATITION pMAX INTO 
  (
  PARTITION p6 VALUES LESS THAN (...) ENGINE=INNODB,
  PARTITION pMAX VALUES LESS THAN MAXVALUE ENGINE=INNODB
  );
  #重组分区
  ALTER TABLE emp_range REORGANIZE PARTITION p1,p2,p2 INTO 
  (
  PARTITION p_all VALUES LESS THAN (...) ENGINE=INNODB
  );
  #删除分区
  ALTER TABLE emp_range DROP PARTITION p1;
  #删除分区数据
  ALTER TABLE emp_range TRUNCATE PARTITION p1;
  ```

* ```
  #管理HASH和KEY分区
  #减少分区数量
  ALTER TABLE emp_hash COALESCE PARTITION 2;	#减少2个分区
  #增加分区
  ALTER TABLE emp_hash ADD PARTITION PARTITIONS 10;	#增加10个分区
  #rebuild optimize analyze repair
  #查看分区信息
  #SHOW TABLE STATUS 
  SHOW TABLE STATUS LIKE 'emp_range';
  #通过TABLE_NAME指定表名来查询INFORMATION_SCHEMA.PARTITIONS
  SELECT PARTITION_NAME FROM INFORMATION_SCHEMA.PARTITIONS WHERE TABLE_SCHEMA='mydb' AND TABLE_NAME='emp_range';
  SELECT * FROM INFORMATION_SCHEMA.PARTITIONS WHERE TABLE_SCHEMA='mydb' AND TABLE_NAME='emp_range' AND PARTITION_NAME='p1';
  ```

* ```
  复制表空间(.ibd)是移动数据最快的方式
  #目标和源库同样的表结构
  #目标
  ALTER TABLE emp DISCARD TABLESPACE;
  #源
  FLUSH TABLES emp FOR EXPORT;
  #复制源库中的文件
  sudo scp -i /home/mysql/.ssh/id_rsa /var/lib/mysql/test/emp#P#* mysql@192.168.101.5:/var/lib/mysql/test/
  #源
  UNLOCK TABLES;
  #目标
  ALTER TABLE emp IMPORT TABLESPACE;
  ```

  



##### 

