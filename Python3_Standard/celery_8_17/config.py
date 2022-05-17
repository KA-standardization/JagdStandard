broker_url = 'redis://127.0.0.1:6379/1'
broker_pool_limit = 10

timezone = 'Asia/Shanghai'
accept_content = ['pickle', 'json']

task_serializer = 'pickle'

result_backend = 'redis://127.0.0.1:6379/1'
result_serializer = 'pickle'
result_expires = 3600
result_cache_max = 10000

worker_redirect_stdouts_level = 'INFO'