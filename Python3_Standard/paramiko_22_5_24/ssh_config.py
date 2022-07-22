# -*- coding: utf-8 -*-
key = r'C:\Users\root\.ssh\id_rsa'
hosts = {
    'twitter-1': {'host': 'xx.xx.xx.xx', 'user': 'root', 'is_idRsa': True, 'key': key,
                  'cmd': {'stop': 'systemctl stop imfaker-twitter-worker-crawl.service',
                          'start': 'systemctl start imfaker-twitter-worker-crawl.service',
                          'restart': 'systemctl restart imfaker-twitter-worker-crawl.service'}},
    'twitter-2': {'host': 'xx.xx.xx.xx', 'user': 'root', 'is_idRsa': True, 'key': key,
                  'cmd': {'stop': 'systemctl stop imfaker-twitter-worker-crawl.service',
                          'start': 'systemctl start imfaker-twitter-worker-crawl.service',
                          'restart': 'systemctl restart imfaker-twitter-worker-crawl.service'}},
    'twitter-3': {'host': 'xx.xx.xx.xx', 'user': 'root', 'is_idRsa': True, 'key': key,
                  'cmd': {'stop': 'systemctl stop imfaker-twitter-worker-crawl.service',
                          'start': 'systemctl start imfaker-twitter-worker-crawl.service',
                          'restart': 'systemctl restart imfaker-twitter-worker-crawl.service'}},
    'twitter-4': {'host': 'xx.xx.xx.xx', 'user': 'root', 'is_idRsa': True, 'key': key,
                  'cmd': {'stop': 'systemctl stop twitter-crawl-users-tweets.service',
                          'start': 'systemctl start twitter-crawl-users-tweets.service',
                          'restart': 'systemctl restart twitter-crawl-users-tweets.service'}},
    'youtube-1': {'host': 'xx.xx.xx.xx', 'user': 'root', 'is_idRsa': True, 'key': key,
                  'cmd': {'stop': 'systemctl stop twitter-crawl-users-tweets.service',
                          'start': 'systemctl start twitter-crawl-users-tweets.service',
                          'restart': 'systemctl restart twitter-crawl-users-tweets.service'}},
}
