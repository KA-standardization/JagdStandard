import os

from celery import Celery

from . import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django.settings")

celery_app = Celery('task')
celery_app.config_from_object(config)
celery_app.autodiscover_tasks()
# pypy -m celery multi start t5 -A imfaker.twitter.task.twitter_task:celery --without-gossip --without-heartbeat --without-mingle -c 8 -Q:t5 twitter.web.user.tweets
#  ps -ef |grep pypy|gawk '{print $2}'|xargs kill -9