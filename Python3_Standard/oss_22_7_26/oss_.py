import oss2
auth = oss2.Auth('user', 'password')
# bucket = oss2.Bucket(auth, 'oss地址', '实例名称')
bucket = oss2.Bucket(auth, 'https://oss-cn-shanghai.aliyuncs.com', 'abc-cba')
# bucket.put_object(f'video_covers/{item_id}.png', r.content)