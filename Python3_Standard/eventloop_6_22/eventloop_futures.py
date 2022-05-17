import queue
import functools
import asyncio

eventloop = None


class EventLoop(queue.Queue):

    def start(self):
        while True:
            function = self.get()
            function()


def foo():
    global eventloop
    print('Holle')
    eventloop.put(bar)


def bar():
    global eventloop
    print('Jagd')
    eventloop.put(foo)


# @asyncio.coroutine
def save_data(data, callback):
    print("Data: {}".format(data))
    # res=yield save_res_to_db(res,callback)


if __name__ == '__main__':
    eventloop = EventLoop()
    eventloop.put(foo)
    # eventloop.put(functools.partial(save_data, 'holle', bar))
    eventloop.start()
