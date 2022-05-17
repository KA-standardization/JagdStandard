import requests
from requests.auth import HTTPDigestAuth

'''
requests.get('https://api.github.com/user', auth=('user', 'pass'))

HTTP 身份认证形式是摘要式身份认证

url = 'http://httpbin.org/digest-auth/auth/user/pass'
requests.get(url, auth=HTTPDigestAuth('user', 'pass'))

Oauth 是一种常见的 Web API 认证方式 https://oauth.net/
import requests
from requests_oauthlib import OAuth1
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

requests.get(url, auth=auth)
'''