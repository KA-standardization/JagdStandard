'''
select...into outfile 的结果只包含了表数据，默认以 Tab 分隔，也可指定分隔符：outfile '/path/file'，中的 path 需要有mysql的权限
select * from e into outfile "/data/mysql/e.sql" fields terminated by ',';


load data 需要有处理文件的权限， GRANT FILE ON *.* TO user@host;
load data infile "/data/mysql/e.sql" into table e fields terminated by ',';


如果数据被某种符号封闭着，需要指定 ‘ fields enclosed by ’ ：
"1669"  "Jim"   "Smith"
load data infile "/data/mysql/e.sql" into table e fields enclosed by '"';
格式上的限制，如 LINES TERMINATED BY 'string' ，指定 file 的换行符，如 ‘\n’ 。


LOAD DATA INFILE ... [REPLACE|IGNORE] INTO TABLE ： replace into 表示如果导入过程中有唯一性约束，直接覆盖；ignore into 则跳过。
LOAD DATA LOCAL INFILE ： 在非服务端执行load data需要使用local。比如在 ipA 处登录 ipB 上的mysqld，就需要用到 local 。
可以指定字段： LOAD DATA INFILE ... INTO TABLE xxx (col1,col2,...)
可以设定值： LOAD DATA LOCAL INFILE '$tmpfile' REPLACE INTO TABLE db.tbname (a,b,c,d,e,f) set g=11,h='xxx';

执行 select into outfile 和 load data infile 需要开启 secure_file_priv ，空值代表文件可以在任意处，也可指定具体路径，NULL表示禁止使用

mysqlimport -u root -pPassword [--local] dbname filename.txt [OPTION]
指定 --local 后，文本文件可以放在任何地方进行导入，否则只能放在mysql的data目录下
--fields-terminated-by=字符串：设置字符串为字段之间的分隔符，可以为单个或多个字符。默认值为制表符“\t”。
--fields-enclosed-by=字符：设置字符来括住字段的值，只能为单个字符。
--fields-optionally-enclosed-by=字符：设置字符括住CHAR、VARCHAR和TEXT等字符型字段，只能为单个字符。
--fields-escaped-by=字符：设置转义字符，默认值为反斜线“\”。
--lines-terminated-by=字符串：设置每行数据结尾的字符，可以为单个或多个字符，默认值为“\n”。
--ignore-lines=n：表示可以忽略前n行。
'''