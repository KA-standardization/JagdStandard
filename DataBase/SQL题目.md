# SQL语句

```
from sqlalchemy import create_engine
con=create_engine('mysql+pymysql://root:wangyu1990.@47.105.119.239:3306/demo?charset=utf8mb4')
USE demo;
```

### 统计三月下单的人数

```
SELECT COUNT(DISTINCT userid) FROM other_info WHERE MONTH(paytime)=3;
```

### 统计每个月下单，并且状态已完成，的人数

```
SELECT MONTH(paytime) AS 月份,COUNT(DISTINCT userid) AS 人数 FROM other_info WHERE ispay=1 GROUP BY 月份;
```

### 统计三月已支付的复购率

```
select count(`userid`)/(select count(distinct `userid`) from order_info where `ispaid`='已支付' and month(`paidtime`)=3) as 三月复购率 from (select month(`paidtime`) as 月份,`userid`,count(`userid`) as usercount from `order_info` where `ispaid`='已支付' and month(`paidtime`)=3 group by `userid` having count(`userid`) >1) tmp
SELECT COUNT(userid)/(SELECT COUNT(DISTINCT userid) FROM other_info WHERE ispay=1 AND MONTH(paytime)=3) AS 复购率 FROM (SELECT userid FROM other_info WHERE ispay=1 AND MONTH(paytime)=3 GROUP BY userid HAVING COUNT(userid)>1) tmp; 
```

### 统计每个月已支付的复购率

```
select 月份,concat(count(if(uc>1,1,null))/count(userid)*100,'%') as 各月复购 from (select month(paidtime) as 月份,userid,count(userid) as uc from order_info where ispaid='已支付' group by 月份,userid) as tmp group by 月份;
SELECT 月份,COUNT(IF(count_uid>1,1,null))/COUNT(userid) AS 复购率 FROM 
	(SELECT MONTH(paytime) AS 月份,userid,COUNT(userid) AS count_uid FROM order_info WHERE ispay=1 GROUP BY 月份,userid) as tmp 
GROUP BY 月份;
```

### 求3月份的回购率

```
SELECT userid FROM other_info WHERE ispay=1 AND MONTH(paytime)=3;
SELECT COUNT(DISTINCT userid)/(SELECT COUNT(DISTINCT userid) FROM other_info WHERE ispay=1 AND MONTH(paytime)=3) FROM other_info WHERE ispay=1 AND MONTH(paytime)=4 AND userid in (SELECT DISTINCT userid FROM other_info WHERE ispay=1 AND MONTH(paytime)=3);
```

### 求每个月的回购率

```
select tmp1.日期,count(tmp1.userid),count(tmp2.userid) from
(select date_format(`paidtime`,"%Y-%m-01") as 日期,userid from order_info where ispaid='已支付' group by 日期,userid) as tmp1
left join
(select date_format(`paidtime`,"%Y-%m-01") as 日期,userid from order_info where ispaid='已支付' group by 日期,userid) as tmp2
on tmp1.userid=tmp2.userid and tmp1.日期 = date_sub(tmp2.日期,interval 1 month) group by tmp1.日期;
```

### 统计男女的消费频次

```
select sex as 性别,avg(ct) as 平均消费次数 from (select us.userid,sex,count(oi.userid) as ct from order_info as oi inner join (select * from user_info where sex is not null) as us on oi.userid = us.userid where ispaid='已支付' group by sex,us.userid) as tmp group by sex;
```

### 统计不同年龄段的消费能力

```
select gb,sum(sp) from (select gb,sum(`price`) as sp,ui.userid from `order_info` as oi
inner join
(select userid,ceil((year(now())-year(`birth`))/10) as gb from `user_info` where birth > '1900-01-01') as ui on oi.userid=ui.userid where ispaid='已支付' group by gb,ui.userid) as tmp
group by gb;
```

### 二八法则

```
#存储过程
#delimiter //
#call 
create procedure pro_res()
begin
    declare num20 int default 0;
    declare num80 int default 0;
    declare res20 int default 0;
    declare res80 int default 0;
    select ceil(count(distinct `userid`)*0.2) into num20 from `order_info`  where  `ispaid`='已支付';
    select ceil(count(distinct `userid`)*0.8) into num80 from `order_info` where `ispaid`='已支付';
    select sum(消费和) into res20 from (select sum(`price`) as 消费和 from `order_info` group by `userid` order by 消费和 desc limit num20) as tmp;
    select sum(消费和) into res80 from (select sum(`price`) as 消费和 from `order_info` group by `userid` order by 消费和 asc limit num80) as tmp;
    select res20 as top20,res80 as top80 from dual;
end//
```

