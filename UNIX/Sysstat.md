# 1.Sar(system activity reporter)

> sysstat
>
> sar可以用来观测当前的活动, 以及配置归档和报告历史统计信息

```
# 未启用sar
sar
Cannot open /var/log/sysstat/sa27: No such file or directory
Please check if data collecting is enabled
# 开启sar的数据收集功能
vi /etc/default/sysstat
	ENABLED="true"
service sysstat restart
cat /etc/cron.d/sysstat
5-55/10 * * * * root command -v debian-sa1 > /dev/null && debian-sa1 1 1
*/10 * * * * root command -v debian-sa1 > /dev/null && debian-sa1 1 1 -S ALL #记录所有统计数据 sadc -S XALL可以记录更多统计数据的明细

sar -u -n TCP,ETCP

# JSON(-j)
sadf -j -- -n TCP
# SVG(-g)

# CSV(-d)
sadf -d -- -n TCP
```

```
# 实时报告
# 1秒为间隔, 5次为次数
sar -n TCP 1 5 
```

### CPU

> CPU分析提供以下选项
>
> > -P ALL :
> >
> > -u : 系统级的平均值
> >
> > -q: 运行队列长度列runq-sz和平均负载的值

### 内存

> 内存统计信息
>
> > -B : 换页统计信息 
> >
> > -H : 巨型页统计信息
> >
> > -r : 内存使用率
> >
> > -S : 交换空间统计信息
> >
> > -W : 交换统计信息
