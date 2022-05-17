import gevent


def foo():
    print("aaa")
    gevent.sleep(1)  # celery.send
    print("aaaaaa")


def bar():
    print("bbb")
    gevent.sleep(1)  # celery.send
    print("bbbbbb")


if __name__ == '__main__':
    # 协程每遇到阻塞就执行别的协程，每建立一个协程就建立一个链接
    gevent.joinall([gevent.spawn(foo), gevent.spawn(bar), ])
