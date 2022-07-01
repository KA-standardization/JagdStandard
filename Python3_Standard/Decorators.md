[官方文档](https://flask-rq2.readthedocs.io/en/latest/)

$2020/10/10$

# 一. Decorators[:crossed_flags:](https://flask-rq2.readthedocs.io/en/latest/#decorators)

**作用**：轻量的异步任务队列

**PS**:和celery比起来

## 1. 定义一个函数, 并指定其为一个job

```python
from flask_rq2 import RQ
# 实例化一个 EQ 对象,用于将函数变成一个 job 任务 
rq = RQ()
# A specific queue name can also be passed as argument:
# 一个指定的队列名也可以被当作参数传递.
# 这里加了装饰器就是一个闭包的效果了, 当前函数可以调用装饰器函数里面的方法
@rq.job('low', timeout=60)
def add(x, y):
    return x + y
```

## 2. 添加 `cron` 形式的任务的多种方式：

```python
job = add.queue(1, 2)
# Or if you decide to use a different queue and timeout dynamically during runtime:
# 或者如果你需要使用不同的队列名并且在运行时动态的设置过期时间.
# Some other parameters are available as well:
# 还有些别的参数也能用: result_ttl,ttl...
job2 = add.queue(3, 4, queue='high', timeout=60 * 2)

# queue job in 60 seconds. 每60秒进入任务队列等候
add.schedule(timedelta(seconds=60), 1, 2)

# queue job at a certain datetime (UTC!)  指定时间在任务队列进行等候
add.schedule(datetime(2016, 12, 31, 23, 59, 59), 1, 2)

# queue job in 14 days and then repeat once 14 days later. 
# 使job进行排队, 并在14填之后重复执行一次
add.schedule(timedelta(days=14), 1, 2, repeat=1)

# queue job in 12 hours with a different queue
add.schedule(timedelta(hours=12), 1, 2, queue='high', timeout=60 * 2)

# queue job every day at moon(UTC!)
# 基本参数:
#       pattern: cron表达式(str)
#       name: 当前任务名(str)
#       1 和 2 表示传到 job 里面的参数
add.cron('0 0 12 * * ?', 'add-one-two', 1, 2)
# queue job every minute with a different queue
# 在使用不同队列的情况下, 每分钟进入一次队列
add.cron('* * * * *', 'add-one-two', 1, 2, queue='high', timeout=55)
# 好像一般都是先写一个表达式, 然后写一个任务名 还有一些参数, 后面需要的就传关键字参数
```

# 二. RQ backends[:crossed_flags:]

## 1. get_queue

```python
# get_queue(相当于创建一个 queue 队列):
# Returns default queue or specific queue for name given as argument:
default_queue = rq.get_queue() 
# 返回一个队列名为 low 的队列     
low_queue = rq.get_queue('low')
# enqueue: 创建一个任务来对一个函数进行延迟调用, 并将其放入队列中
easy_job = default_queue.enqueue(add, args=(1, 2))
hard_job = low_queue.enqueue(add, args=(1e100, 2e200))
```

## 2. get_worker

```python
# get_worker(相当于创建一个 worker):
# Returns a worker for default queue or specific queues for names given as arguments:
# 为默认队列返回一个 worker, 或者根据参数指定的队列返回其 worker
# Creates a worker that handle jobs in ``default`` queue.
default_worker = rq.get_worker()
default_worker.work(burst=True)
# Creates a worker that handle jobs in both ``simple`` and ``low`` queues.
# 创建一个能够同时处理 low 和 simple 两个队列的 worker
low_n_simple_worker = rq.get_worker('low', 'simple')
low_n_simple_worker.work(burst=True)
```

## 3. get_scheduler

```python
# Returns an RQ Scheduler instance for periodically enqueuing jobs:
# 返回一个定时任务对象来定期的将任务入队.
# check every 10 seconds if there are any jobs to enqueue.
# 每十秒检查一次, 如果有任何任务进入队列中.
scheduler = rq.get_scheduler(interval=10)
scheduler.run()
```

# 三. Configuration[:crossed_flags:](https://flask-rq2.readthedocs.io/en/latest/#configuration)

## 1. RQ_REDIS_URL

```python
app.config['RQ_REDIS_URL'] = 'redis://localhost:6379/0'
```

## 2.RQ_QUEUES

The default queues that the worker and CLI commands (`empty`, `info` and `worker`) act on by default

worker 和 CLI 命令行默认操作的队列.

```python
app.config['RQ_QUEUES'] = ['default']
```

## 3. RQ_ASYNC

$ 异步队列开关 $

Whether or not to run jobs asynchronously. Defaults to `True` meaning that jobs only run when they are processed by the workers.

是否异步的运行任务.默认设置为**True**表示任务只有被worker 处理的时候才能被运行.

```python
app.config['RQ_ASYNC'] = True
```

Set to `False` to run jobs immediatedly upon enqueuing in-process. This may be useful for testing purposes or other constrained environments. This is the main switch, use with discretion.

设置**False**表示任务进入队列中将会被同时处理.这个可能会对测试或者其他受限制的环境有帮助.但这个是一个重要的开关, 请谨慎使用. 

## 4. RQ_SCHEDULER_CLASS

$New in version 17.1.*$

The dotted import path of the scheduler class to enqueue scheduled jobs with.

意思好像是说`scheduler`(定时任务)这个类导入的路径,好吧.不懂

```python
app.config['RQ_SCHEDULER_CLASS'] = 'myproject.scheduler.MyScheduler'
```

默认是**'rq_scheduler.Scheduler'**

## 5. RQ_SCHEDULER_QUEUE

The name of the queue to enqueue scheduled jobs in.

```python
app.config['RQ_SCHEDULER_QUEUE'] = 'scheduled'
```

默认是**'default'**

## 6.RQ_SCHEDULER_INTERVAL

The default interval the RQ Scheduler checks for jobs to enqueue, in seconds.	

RQ调度器默认检查任务的时间间隔.单位是秒

```python
app.config['RQ_SCHEDULER_INTERVAL'] = 1
```

默认 60.

# 四. CLI support 命令行操作[:crossed_flags:](https://flask-rq2.readthedocs.io/en/latest/#cli-support)

没整出来:question:

Flask-RQ2 only supports the [Click](http://click.pocoo.org/) based [CLI feature in Flask >= 0.11](http://flask.pocoo.org/docs/dev/cli/). If you’re using Flask < 0.10 you’ll need to install a backport package called [Flask-CLI](http://pythonhosted.org/Flask-CLI/) as well, e.g.:

```
pip install Flask-CLI
```

Or install it in one go:

```
pip install Flask-RQ2[cli]
```

Please call `flask rq --help` for more information, assuming you’ve set the `FLASK_APP` environment variable to the Flask app path.

### Commands

There isn’t an official overview of CLI commands in the RQ documentation, but these are the commands that Flask-RQ2 support.

- `worker` – Starts an [RQ worker](http://python-rq.org/docs/workers/) (required to run jobs).
- `scheduler` – Starts an [RQ Scheduler](https://github.com/ui/rq-scheduler) (optional for scheduled jobs).
- `info` – Shows an [RQ command-line monitor](http://python-rq.org/docs/monitoring/).
- `empty` – Empty the given [RQ queues](http://python-rq.org/docs/).
- `requeue` – Requeues [failed jobs](http://python-rq.org/docs/exceptions/).
- `suspend` – Suspends all workers.
- `resume` – Resumes all workers.

Please call each command with the `--help` option to learn more about their required and optional paramaters.

# 五. Unit Testing 单元测试[:crossed_flags:](https://flask-rq2.readthedocs.io/en/latest/#unit-testing)

To use Flask-RQ2 in unit tests, set the variable `RQ_CONNECTION_CLASS = 'fakeredis.FakeStrictRedis'`. The *fakeredis* module is required and can be installed with `pip install fakeredis`. Excerpts of how this can be integrated into a Flask app are shown below.

```python
# config.py

class Config:
    APP_NAME = os.environ.get('APP_NAME')
    RQ_CONNECTION_CLASS = 'fakeredis.FakeStrictRedis'
# app/__init__.py

rq = RQ()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    rq.init_app(app)
```

# 六、示例:crossed_flags:

这里 **说明** 一下：这玩意儿  Windows跑不了， 需要的话移步Linux 或  maxOS系统。

- my_scripts:

```python
"""
这里需要给这个框架打个补丁, 跳过是否在主线程的判断
"""
import threading
import signal
from rq import worker


def _install_signal_handlers(self):
    """Installs signal handlers for handling SIGINT and SIGTERM
    gracefully.
    """
    # 这里判断了一下是否是在主线程里面, 如果没有在主线程里面的话, 就无法进入
    if threading.current_thread() == threading.main_thread():
        signal.signal(signal.SIGINT, self.request_stop)  # SIGINT:2
        signal.signal(signal.SIGTERM, self.request_stop)  # SIGTERM:15
    # request_stop: 父进程结束后, 子进程正常结束



def patch_model():
    worker.Worker.install_signal_handlers = worker.Worker._install_signal_handlers
    worker.Worker._install_signal_handlers = _install_signal_handlers
```



- app.py content:

```python
import time

from flask import Flask
from flask_rq2 import RQ

app = Flask(__name__)
app.debug = True

app.config['RQ_OTHER_HOST'] = 'localhost'
app.config['RQ_OTHER_PORT'] = 6379
app.config['RQ_OTHER_PASSWORD'] = None
app.config['RQ_OTHER_DB'] = 0

rq = RQ(app)


def takes_a_while(echo):
    time.sleep(1)
    return echo


@rq.job
def do_something(echo):
    time.sleep(1)
    return echo


@rq.job('low')
def do_something_low(echo):
    time.sleep(1)
    return echo


# @rq.job('low', connection='other')
@rq.job('low')
def do_something_low_on_connection(echo):
    time.sleep(1)
    return echo


@app.route('/')
def home():
    return "Home"


@app.route('/doit1')
def doit():
    echo = rq.get_queue().enqueue(takes_a_while, 'do it')
    print(echo)
    # <FlaskJob 29436d3b-85a4-49db-90c3-5765ae6c05d8:
    # app.takes_a_while('do it')>
    return 'Success1'


@app.route('/doit2')
def doit2():
    # connection 表示连接的数据库是哪个
    # One can change the connection settings for the default server like so
	# 这个  ‘do it 2’ 就是这个任务的job_id(用来从这个队列里面取出任务)
    echo = rq.get_queue().enqueue(takes_a_while, 'do it 2',
                                  name="low", connection="other")
    print(echo)
    # <FlaskJob a5333f12-a05e-4e93-a0b0-47ef5cf6ae84:
    #   app.takes_a_while('do it 2', connection='other', name='low')>
    # 返回的也是一个 FlaskJob 对象
    return 'Success2'


@app.route('/doit3')
def doit3():
    with rq.connection:
        q = rq.get_queue('low')
        q.enqueue(takes_a_while, 'do it 3')
    return 'Success3'


@app.route('/doit4')
def doit4():
    echo = do_something('decorated')
    print(echo)  # 这里没有进入队列
    return 'Success4'


@app.route('/doit5')
def doit5():
    echo = do_something_low('doit5')
    print(echo)   # 没有进入
    return 'Success5'


@app.route('/doit6')
def doit6():
    echo = do_something_low_on_connection('doit6')
    print(echo)  #
    return 'Success6'

@app.route('/doit7')
def doit7():
    echo = rq.get_worker().work(True)
    print(echo)
    return 'Success7'
```

- somewhere.py content:

```python
"""
这里面是一些自己定义的函数
"""
import socket
import time

import requests
from redis import Redis
from rq import get_current_job
from rq.decorators import job


def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())


redis_conn = Redis()


@job('low', connection=redis_conn, timeout=5)
def add(x, y):
    job = get_current_job()
    job.meta['handled_by'] = socket.gethostname()
    job.meta[''] = None
    job.save_meta()
    return x + y


def fib(num):
    return num


def takes_a_while():
    time.sleep(1)
    echo = 'hello world'
    return echo

```

- app.py content:
- - 这里需要注意的是需要使用manager 命令行的方式进行启动，否则会玄学报错。

```python
import time
from datetime import timedelta

from flask import Flask
from flask_rq2 import RQ
from flask_script import Manager
from flask_socketio import SocketIO
from somewhere import fib, takes_a_while, add


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['RQ_OTHER_HOST'] = 'localhost'
    app.config['RQ_OTHER_PORT'] = 6379
    app.config['RQ_OTHER_PASSWORD'] = None
    app.config['RQ_OTHER_DB'] = 0
    socket_io = SocketIO(app)
    # is_async = False 表示队列不是异步的, 此时直接绕开了 worker
    # bypassing worker
    rq = RQ(app, is_async=True)
    return app, rq, socket_io


app, rq, socket_io = create_app()
# 交到 Manager 手上才能成功运行, 原因不明
manager = Manager(app=app)
```

```python
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/doit1')
def doit1():
    q = rq.get_queue('low')
    job = q.enqueue(fib, 8)
    print(job.result)
    return 'ok'


@app.route('/doit2')
def doit2():
    # connection 表示连接的数据库是哪个
    # One can change the connection settings for the default server like so
    # 这里有两种形式将函数放到队列里面, 还有一种是在函数是在函数上面加上装饰器来进行处理
    q = rq.get_queue('low')
    # q.enqueue(foo, args=(1, 2), kwargs={'a': 1}, job_timeout=30)
    job = q.enqueue(takes_a_while,
                    'do it 2',
                    name="low",
                    connection="other",
                    # args='hello world'
                    )
    # print(echo.)
    print(job.result)
    print(q)
    print(len(q))  # 只有正在排队的 jobs 可被计算在队列长度中
    time.sleep(2)
    print(job.result)
    # print(echo.result)

    # <FlaskJob a5333f12-a05e-4e93-a0b0-47ef5cf6ae84:
    #   app.takes_a_while('do it 2', connection='other', name='low')>
    # 返回的也是一个 FlaskJob 对象
    return 'Success2'


@app.route('/doit3')
def doit3():
    low_queue = rq.get_queue('low')
    low_worker = rq.get_worker('low')
    easy_job = low_queue.enqueue_in(timedelta(seconds=10), add, job_id='qwe', args=(1, 2))
    low_worker.work(burst=True)
    return 'Success doit3'


@app.route('/doit4')
def doit4():
    low_queue = rq.get_queue('low')
    # 如果是 定时任务 的话, 可以使用 enqueue_at:
    # job = queue.enqueue_at(datetime(2019, 10, 8, 9, 15), say_hello)

    easy_job = low_queue.enqueue(add, job_id='qwe', args=(1, 2))
    # easy_job = low_queue.enqueue_in(timedelta(seconds=10), add, job_id='qwe', args=(1, 2))
    print(easy_job)
    print(easy_job.result)  # None
    return 'Success4'


@app.route('/doit5')
def doit5():
    low_queue = rq.get_queue('low')
    easy_job = low_queue.enqueue(add, job_id='ewq', args=(1, 2))
    job = rq.get_queue('low').fetch_job('ewq')
    print('==============')
    print('status:', job.get_status())
    low_worker = rq.get_worker('low')  # 整个 worker 出来  
    # TODO: burst 模式下可能会出现一些问题, 需要增加异常处理
    low_worker.work(burst=True)  # 然后开始干活, burst 表示队列里面没有任务的话, worker 直接退出
    # 延迟一秒, 保证该任务已经顺利完成了
    time.sleep(1)
    # 获取 low 队列, 然后根据 job_id fetch 出指定的任务,
    # 但是此时 任务已经结束了, 状态为 done
    print('result:', job.result)  # job.result 为任务运行后的结果
    print(type(job))  # flask_rq2.job.FlaskJob
    print(job.get_status())
    print(job.args)
    # exc_info 里面存放的是任务没有顺利执行时存放的错误信息,
    # 如果没有错误, 那么里面的信息为空
    print('exc_info:', job.exc_info)
    print('meta:', job.meta)     # meta 表示函数存放的 arbitrary info, 可以通过meta直接取
    return 'Success5'

```

- run.py content

```python
from app import manager
from my_scripts import patch_model

if __name__ == '__main__':
    patch_model()
    manager.run()
```

