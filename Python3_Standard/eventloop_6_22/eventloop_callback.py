import queue
import functools

eventloop = None


class EventLoop(queue.Queue):

    def start(self):
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


def save_data(data, callback):
    print('DATA: {}'.format(data))
    # save_res_to_db(res,callback)


def print_response(res):
    print('Response: {}'.format(res))


if __name__ == '__main__':
    eventloop = EventLoop()
    eventloop.put(foo)
    # eventloop.put(functools.partial(save_data, "buch", print_response))
    eventloop.start()
