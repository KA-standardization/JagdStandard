import tornado.ioloop
import tornado.web
'''
异步接口多种风格
回调参数
返回占位符 ( Future, Promise, Deferred)
交付到队列
回调注册（例如 POSIX 信号）
'''

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write("Holle")


def make_app():
    return tornado.web.Application([(r"/", Handler)])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
