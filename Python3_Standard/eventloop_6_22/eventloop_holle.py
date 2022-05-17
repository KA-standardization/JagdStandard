import queue
import functools

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


if __name__ == '__main__':
    eventloop = EventLoop()
    eventloop.put(foo)
    eventloop.start()
