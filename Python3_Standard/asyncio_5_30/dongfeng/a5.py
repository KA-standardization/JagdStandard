import time
import asyncio

import requests
import threading


class Foo(object):

    def __init__(self, url):
        self.url = url

    def request(self):
        res = requests.get(self.url)
        time.sleep(1)
        print(len(res.text))

    def __await__(self):
        threading.Thread(target=self.request).start()


def request(url, future):
    res = len(requests.get(url).text)
    time.sleep(1)
    future.set_result(res)
    # future.done()
    # return inner()


def request2(url):
    print(url)
    # res = len(requests.get(url).text)
    # time.sleep(1)
    # print(res)


async def parse(url, loop):
    all_done = asyncio.Future()
    await asyncio.threads.to_thread(request, url=url, future=all_done)
    print('setting future to {!r}'.format(all_done.result()))


if __name__ == '__main__':
    # # loop = asyncio.get_event_loop()
    urls = 'http://www.baidu.com'
    # #
    # # tasks = []
    # s = time.time()
    # #
    # # for i in range(200):
    # #     task = asyncio.ensure_future(parse(urls, loop))
    # #     tasks.append(task)
    # #
    # # loop.run_until_complete(asyncio.wait(tasks))
    #
    for i in range(10):
        threading.Thread(target=request2, args=(urls,)).start()
    # print(time.time() - s)

    # def foo():
    #     print(1111111)
    #     yield {1: 2}
    #     # 1
    #     print(33333333)
    #
    #
    # f = foo()
    # try:
    #     print(next(f))
    #     print("-----------------")
    #     print(next(f))
    # except:
    #     pass
    # # print(next(foo()))
    # c = 2
    # [1111111,{1:2},3333333]
    # a = [i for i in range(10)]
    # b = (i for i in range(10))
    # print(b.__next__())
    # #
    # # def foo():
    # #     yield {1:2}
    # #     push
    # #
    # # def bar(a):
    # #
    # #     a= yield res()
    # #
    # #     pull
    #
    # # for i in
    # print(a)

#     """
#         def read_in_tweets_wrapper(cls, fnc):
#         @functools.wraps(fnc)
#         def read_in_tweets(tweets, queue_):
#         # tweets=[]
#             def parallel(tweets):
#                 cursor = 0
#                 for tweet in tweets:
#                     fnc(data=tweet, queue=queue_)
#                     cursor = yield tweets[cursor]
#
#             cc = parallel(tweets)
#             cursor_ = 0
#             try:
#                 next(cc)
#                 while True:
#                     cursor_ += 1
#                     cc.send(cursor_)
#             except Exception:
#                 pass
#
#         return read_in_tweets
#
#     """
#
# t = [i for i in range(10)]
#
#
# def read_in_tweets(tweets):
#     def parallel(tweets):
#         cursor = 0
#         for tweet in tweets:
#             print(cursor)
#
#
#             """
#             cursor = cursor_
#             yield tweets[cursor]
#             """
#
#     cc = parallel(tweets)
#     cursor_ = 0
#     try:
#         next(cc)
#         while True:
#             cursor_ += 1
#             cc.send(cursor_)
#     except Exception:
#         pass
#
# read_in_tweets(t)
