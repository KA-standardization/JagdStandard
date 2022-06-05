"""
    http [flags] [METHOD] URL [ITEM [ITEM]]
    get:
        http get baidu.com/w s==abc s2==bcd
    post:
        http post baidu.com/w body=abc
        http post baidu.com/w body=abc flag:=true
        http post baidu.com/w body=@./aaa.json          http post baidu.com/w < ./aaa.json
    提交表单:
        http -f post baidu.com/w username=root passwd=root
    设置请求头:
        http get baidu.com header:val user-again:
        http get baidu.com header:val user-again; 空值
    跟随重定向
        http -F baidu.com
    代理:
        http --proxy=http:http://192.168.1.104:8080 ---proxy=https:https://192.168.1.104:8080 baidu.com
    关闭SSL验证: --verify=no 响应头: --headers 或 -h 响应体: --body 或 -b 两者: --verbose 或 -v 默认输出是两者
    输出到文件:
        http https://www.baidu.com > ./aaa.txt
    下载:
        -d 下载
        -o 来指定输出地址
        http -d -o ./aaa/ baidu.com/aaa.zip
"""