import time
import urllib
import threading
from queue import Queue
from urllib.parse import urlparse

import feedparser

thread_num = 2
q1 = Queue()
urls = ['http://feed.cnblogs.com/blog/sitehome/rss']


def message(s):
    print('{}: {}'.format(threading.current_thread().name, s))


def download_(q):
    while True:
        url = q.get()
        filename = url.rpartition('/')[-1]
        message('down {}'.format(filename))
        res = urllib.request.urlopen(url)
        data = res.read()
        message('write {}'.format(filename))
        with open(filename, 'wb') as f:
            f.write(data)
        q.task_done()


for i in range(thread_num):
    worker = threading.Thread(target=download_, args=(q1,), name='worker-{}'.format(i))
    worker.setDaemon(True)
    worker.start()

for url in urls:
    res = feedparser.parse(url, agent='queue_fetch_podcasts_4_28.py')
    for entry in res['entries'][:5]:
        print(entry['link'])
        q1.put(entry['link'])

q1.join()
