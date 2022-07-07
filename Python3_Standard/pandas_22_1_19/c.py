import pandas as pd
import numpy as np
import json
import redis

pool_redis_cluster = redis.ConnectionPool(host='10.0.4.105', port=6379, decode_responses=True)
redis_cluster = redis.StrictRedis(connection_pool=pool_redis_cluster)

base2 = []
base = []
df = pd.read_excel('./base2.xlsx')

for index, item in df.iterrows():
    base_url_token = item[1]
    base.append(base_url_token)

for i in base:
    for k, v in redis_cluster.hscan_iter(f'zhihu:f2:{i}'):
        v = json.loads(v)
        tmp = {
            '东风粉丝url_token': i,
            '东风粉丝的关注url_token': k,
            "name": v.get('name'),
            "avatar_url": v.get("avatar_url"),
            "url": v.get("url"),
            "headline": v.get("headline"),
            "gender": v.get("gender", -1),
            "follower_count": v.get("follower_count", 0),
            "answer_count": v.get("answer_count", 0),
            "articles_count": v.get("articles_count", 0),
        }
        base2.append(tmp)

df2 = pd.DataFrame(data=base2)
df2.to_excel('./zhihu.xlsx')
