# * 该符号使得查询语句返回指定表的所有列
# () 里的查询条件被一起评估
# as 关键字重新命名查询所返回的列,即是创建别名,新的列名被称作别名.创建号的别名对于查询语句大有裨益,它能让查询结果更易于理解
# 把查询包装为一个内嵌视图,这样就可以引用别名了 $4
	select * from 
		(select sal as salary, comm as commission from emp) x
	where salary < 5000;
# 串联多列的值
	#Oracle DB2 PostgreSQL
	select ename||' works as a '||job as msg from emp where deptno=10;
	#MySQL
	select concat(ename,' work as a ',job) as msg from emp where deptno=10;
	#SQL Server
	select ename+' work as a '+job as msg from emp where deptno=10;
# 在SELECT语句中使用条件逻辑 case表达式能够对查询结果执行条件逻辑判断,else子句是可选的,若没有它,则对不满足测试条件的行,case表达式会返回null
	select ename,sal,
		case when sal<=2000 then 'underpaid' 
			 when sal>=4000 then 'overpaid' 
			 else 'ok'
		end as status
	from emp;
# 限定返回的行数
	#DB2
	select * from emp fetch first 5 row only
	#MySQL PostgreSQL
	select * from emp limit 5
	#Oracle rownum函数=1会成功
	select * from emp where rownum <= 5
	#SQL Server
	select top 5 * from emp 
# 随机返回若干行记录 内置函数rand()
	#DB2
	select ename, job from emp order by rand() fetch first 5 rows only; 
	#MySQL
	select ename, job from emp order by rand() limit 5;
	#PostgreSQL
	select ename, job from emp order by random() limit 5;
	#Oracle
	select * from (select ename, job from emp order by dbms_random.value()) where rawnum <= 5
	#SQL Server
	select top 5 ename, job from emp order by newid();
#查找Null值
	select * from emp where comm is null; 
#把null值转换为实际值 coalesce函数 若comm不为null 会返回comm 否则返回0
	select coalesce(comm, 0) from emp;
	select case 
		when comm is not null then comm 
		else 0 
	end from emp; 
#查找匹配
	select ename, job from emp where deptno in (10,20) and (ename like '%I%' or job like '%ER');
#第2章 查询结果排序 知道如何控制和修改结果集 
#以指定顺序返回查询结果 order by 指定一个数值来指代该列 数值从1开始
	select ename,job,sal from emp where deptno=10 order by 3 asc/desc;
#多字段排序 可以根据一个没有被包含在select列表里的列来排序,如果你的查询语句里有group by 或distinct那么就不能按照select列表之外的列进行排序
	select deptno,ename,job from emp order by deptno asc,sal desc;
#依据子串排序 按照最后两个字符对检索结果进行排序 length(job)-2找的是下标
	#DB2 MySQL Oracle PostgreSQL
	select ename,job from emp order by substr(job,length(job)-2);
	#SQL Server
	select ename,job from emp order by substring(job,len(job)-2,2);
#对含有字母和数字的列排序 $16
	create view V as select ename||' '||deptno as data from emp;
	#Oracle PostgreSQL
	#按照deptno排序
	select data from V order by 
		replace(data,replace(translate(data,'0123456789','##########'),'#',''),'');
	#按照ename排序
	select data from emp order by
		replace(translate(data,'0123456789','##########'),'#','');
	#DB2 隐式类型转换比Oracle PostgreSQL更严格,因此创建视图时要先将deptno的类型转换为char
	#按照deptno排序
	select * from (select ename||' '||cast(deptno as char(2)) as data from emp) v 
		order by 
		replace(data,replace(translate(data,'##########','0123456789')'#',''),'');
	#按照ename排序
	select * from (select ename||' '||cast(deptno as char(2)) as data from emp) v 
		order by
		replace(translate(data,'##########','0123456789'),'#','');
#排序时对null的处理 对可能为空的列进行升序或降序排列
	#DB2 MySQL PostgreSQL SQL Server 添加辅助列 只存在于查询语句里,而不存在于表中
		#非null值comm升序排列,全部null值放到最后
		select ename,sal,comm from 
			(select ename,sal,comm,case when comm is null then 0 else 1 end as is_null from emp) x 
			order by is_null desc, comm asc;
		#非null值comm降序排列,全部null值放到最后
		select ename,sal,comm from 
			(select ename,sal,comm,case when comm is null then 0 else 1 end as is_null from emp) x
			order by is_null desc, comm desc;
		#非null值comm升序排列,全部null值放到最前面
		select ename,sal,comm from 
			(select ename,sal,comm,case when comm is null then 0 else 1 end as is_null from emp) x
			order by is_null asc,comm asc;
		#非null值comm降序排列,全部null值放到最前面
		select ename,sal,comm from 
			(select ename,sal,comm,case when comm is null then 0 else 1 end as is_null from emp) x
			order by is_null asc,comm desc;
	#Oracle
		#非null值comm升序排列,全部null值放到最后
		select ename,sal,comm from emp order by comm asc nulls last;
		#非null值comm降序排列,全部null值放到最后
		select ename,sal,comm from emp order by comm desc nulls last;
		#非null值comm升序排列,全部null值放到最前面
		select ename,sal,comm from emp order by comm asc nulls first;
		#非null值comm降序排列,全部null值放到最前面
		select ename,sal,comm from emp order by comm desc nulls first;
#依据条件逻辑动态调整排序项
	#如果job==salesman 就按照comm排序,否则就按照sal排序 在order by子句中使用case表达式
	select ename,sal,job,comm from emp order by case when job=='salesman' then comm else sal end;
	select ename,sal,job,comm,case when job=='salesman' then comm else sal end as ordered from emp order by 5;
			1		2	3	4	5
#第3章 多表查询

	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
