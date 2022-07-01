# * �÷���ʹ�ò�ѯ��䷵��ָ�����������
# () ��Ĳ�ѯ������һ������
# as �ؼ�������������ѯ�����ص���,���Ǵ�������,�µ���������������.�����ŵı������ڲ�ѯ����������,�����ò�ѯ������������
# �Ѳ�ѯ��װΪһ����Ƕ��ͼ,�����Ϳ������ñ����� $4
	select * from 
		(select sal as salary, comm as commission from emp) x
	where salary < 5000;
# �������е�ֵ
	#Oracle DB2 PostgreSQL
	select ename||' works as a '||job as msg from emp where deptno=10;
	#MySQL
	select concat(ename,' work as a ',job) as msg from emp where deptno=10;
	#SQL Server
	select ename+' work as a '+job as msg from emp where deptno=10;
# ��SELECT�����ʹ�������߼� case���ʽ�ܹ��Բ�ѯ���ִ�������߼��ж�,else�Ӿ��ǿ�ѡ��,��û����,��Բ����������������,case���ʽ�᷵��null
	select ename,sal,
		case when sal<=2000 then 'underpaid' 
			 when sal>=4000 then 'overpaid' 
			 else 'ok'
		end as status
	from emp;
# �޶����ص�����
	#DB2
	select * from emp fetch first 5 row only
	#MySQL PostgreSQL
	select * from emp limit 5
	#Oracle rownum����=1��ɹ�
	select * from emp where rownum <= 5
	#SQL Server
	select top 5 * from emp 
# ������������м�¼ ���ú���rand()
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
#����Nullֵ
	select * from emp where comm is null; 
#��nullֵת��Ϊʵ��ֵ coalesce���� ��comm��Ϊnull �᷵��comm ���򷵻�0
	select coalesce(comm, 0) from emp;
	select case 
		when comm is not null then comm 
		else 0 
	end from emp; 
#����ƥ��
	select ename, job from emp where deptno in (10,20) and (ename like '%I%' or job like '%ER');
#��2�� ��ѯ������� ֪����ο��ƺ��޸Ľ���� 
#��ָ��˳�򷵻ز�ѯ��� order by ָ��һ����ֵ��ָ������ ��ֵ��1��ʼ
	select ename,job,sal from emp where deptno=10 order by 3 asc/desc;
#���ֶ����� ���Ը���һ��û�б�������select�б������������,�����Ĳ�ѯ�������group by ��distinct��ô�Ͳ��ܰ���select�б�֮����н�������
	select deptno,ename,job from emp order by deptno asc,sal desc;
#�����Ӵ����� ������������ַ��Լ�������������� length(job)-2�ҵ����±�
	#DB2 MySQL Oracle PostgreSQL
	select ename,job from emp order by substr(job,length(job)-2);
	#SQL Server
	select ename,job from emp order by substring(job,len(job)-2,2);
#�Ժ�����ĸ�����ֵ������� $16
	create view V as select ename||' '||deptno as data from emp;
	#Oracle PostgreSQL
	#����deptno����
	select data from V order by 
		replace(data,replace(translate(data,'0123456789','##########'),'#',''),'');
	#����ename����
	select data from emp order by
		replace(translate(data,'0123456789','##########'),'#','');
	#DB2 ��ʽ����ת����Oracle PostgreSQL���ϸ�,��˴�����ͼʱҪ�Ƚ�deptno������ת��Ϊchar
	#����deptno����
	select * from (select ename||' '||cast(deptno as char(2)) as data from emp) v 
		order by 
		replace(data,replace(translate(data,'##########','0123456789')'#',''),'');
	#����ename����
	select * from (select ename||' '||cast(deptno as char(2)) as data from emp) v 
		order by
		replace(translate(data,'##########','0123456789'),'#','');
#����ʱ��null�Ĵ��� �Կ���Ϊ�յ��н��������������
	#DB2 MySQL PostgreSQL SQL Server ��Ӹ����� ֻ�����ڲ�ѯ�����,���������ڱ���
		#��nullֵcomm��������,ȫ��nullֵ�ŵ����
		select ename,sal,comm from 
			(select ename,sal,comm,case when comm is null then 0 else 1 end as is_null from emp) x 
			order by is_null desc, comm asc;
		#��nullֵcomm��������,ȫ��nullֵ�ŵ����
		select ename,sal,comm from 
			(select ename,sal,comm,case when comm is null then 0 else 1 end as is_null from emp) x
			order by is_null desc, comm desc;
		#��nullֵcomm��������,ȫ��nullֵ�ŵ���ǰ��
		select ename,sal,comm from 
			(select ename,sal,comm,case when comm is null then 0 else 1 end as is_null from emp) x
			order by is_null asc,comm asc;
		#��nullֵcomm��������,ȫ��nullֵ�ŵ���ǰ��
		select ename,sal,comm from 
			(select ename,sal,comm,case when comm is null then 0 else 1 end as is_null from emp) x
			order by is_null asc,comm desc;
	#Oracle
		#��nullֵcomm��������,ȫ��nullֵ�ŵ����
		select ename,sal,comm from emp order by comm asc nulls last;
		#��nullֵcomm��������,ȫ��nullֵ�ŵ����
		select ename,sal,comm from emp order by comm desc nulls last;
		#��nullֵcomm��������,ȫ��nullֵ�ŵ���ǰ��
		select ename,sal,comm from emp order by comm asc nulls first;
		#��nullֵcomm��������,ȫ��nullֵ�ŵ���ǰ��
		select ename,sal,comm from emp order by comm desc nulls first;
#���������߼���̬����������
	#���job==salesman �Ͱ���comm����,����Ͱ���sal���� ��order by�Ӿ���ʹ��case���ʽ
	select ename,sal,job,comm from emp order by case when job=='salesman' then comm else sal end;
	select ename,sal,job,comm,case when job=='salesman' then comm else sal end as ordered from emp order by 5;
			1		2	3	4	5
#��3�� ����ѯ

	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
