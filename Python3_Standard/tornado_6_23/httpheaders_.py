from tornado.httputil import HTTPHeaders

a = {"A": 2, "B": 3}
headers = HTTPHeaders(a)
print(list(headers.keys()))
headers.add("Set-Cookie", "A")
headers.add("Set-Cookie", "D")
print(list(headers.keys()))
print(headers.get_list("Set-Cookie"))
for (k, v) in sorted(headers.get_all()):
    print('%s: %s' % (k, v))
