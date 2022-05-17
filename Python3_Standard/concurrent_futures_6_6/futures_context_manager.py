from concurrent import futures


def task(n):
    print(n)


# 并发的运行并等待它们都完成 上下文管理器退出 会调用执行器 shutdown()方法
with futures.ThreadPoolExecutor(max_workers=2) as ex:
    ex.submit(task, 1)
    ex.submit(task, 2)
    ex.submit(task, 3)
    ex.submit(task, 4)
    ex.submit(task, 5)
