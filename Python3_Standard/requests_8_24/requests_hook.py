import requests


# Requests有一个钩子系统，你可以用来操控部分请求过程，或信号事件处理
# 你可以通过传递一个 {hook_name: callback_function} 字典给 hooks 请求参数为每个请求分配一个钩子函数
def print_url(r, *args, **kwargs):
    print(r.url)
    print(r.headers)
    print(r.request.headers)


hooks = dict(response=print_url)

'''
若执行你的回调函数期间发生错误，系统会给出一个警告。
若回调函数返回一个值，默认以该值替换传进来的数据。若函数未返回任何东西，也没有什么其他的影响
'''

r = requests.get('http://httpbin.org', hooks=dict(response=print_url))
# print(r.text)
