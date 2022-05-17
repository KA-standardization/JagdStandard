import tornado.ioloop
import tornado.web
import tornado.httpclient
import tornado.escape


class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write('holle')


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
        }
        request = tornado.httpclient.HTTPRequest(
            url='https://maimai.cn/search/feeds?query=%E8%85%BE%E8%AE%AF&limit=20&offset=80&searchTokens=%5B%22%E8%85%BE%E8%AE%AF%22%5D&highlight=true&sortby=time&jsononly=1',
            headers=headers)
        response = await http.fetch(request)
        json = {'res': repr(response.body)}
        # if response.headers['Content-Type'] == "application/json; charset=utf-8":
        #     json = tornado.escape.json_decode(response.body)
        self.write(json)


def make_app():
    return tornado.web.Application([(r'/', Handler), (r'/holle', MainHandler)])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    io_loop = tornado.ioloop.IOLoop.current()
    io_loop.start()
