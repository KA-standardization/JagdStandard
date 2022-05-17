import os

from celery import Celery

from . import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django.settings")

celery_app = Celery('task')
celery_app.config_from_object(config)
celery_app.autodiscover_tasks()
