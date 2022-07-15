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
        pass