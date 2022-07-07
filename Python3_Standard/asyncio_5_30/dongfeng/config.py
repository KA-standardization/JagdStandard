# -*- coding:utf-8 -*-
import time
import random
import hashlib

import redis
import requests

pool_redis_cluster = redis.ConnectionPool(host='10.0.4.105', port=6379, decode_responses=True)
redis_cluster = redis.StrictRedis(connection_pool=pool_redis_cluster)


class ZhiHuClient(object):

    @classmethod
    def get_encrypt_b(cls, to_encrypt):
        fmd5 = hashlib.new('md5', to_encrypt.encode()).hexdigest()
        res = requests.post('http://10.0.17.100:3000/encrypt', data={'fist': fmd5})
        encrypt_str = res.text
        return encrypt_str

    @classmethod
    def get_ip(cls):
        t = int(time.time())
        if t % 2 == 0:
            proxies = {
                'http': 'http://proxy:orderId=O21072616193919678168&sign=3014798228629a3c2ee159b7a0bd35c7&time=1627290066&pid=-1&cid=@proxy-service2.vpsnb.net:14223',
                'https': 'http://proxy:orderId=O21072616193919678168&sign=3014798228629a3c2ee159b7a0bd35c7&time=1627290066&pid=-1&cid=@proxy-service2.vpsnb.net:14223'
            }
            return proxies
        else:
            limit_num = int(redis_cluster.get('public:iproxy:91vps_num')) - 1
            xy = redis_cluster.get(f'public:iproxy:91vps:ip_{random.randint(0, limit_num)}')
            proxies = {
                'http': 'http://' + xy,
                'https': 'http://' + xy,
            }
            return proxies
