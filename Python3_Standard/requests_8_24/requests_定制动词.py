import requests

# WEBDAV 服务器会要求你使用 MKCOL 方法。别担心，Requests 一样可以搞定它们。你可以使用内建的 .request 方法
r = requests.request('MKCOL', '', data=None)

