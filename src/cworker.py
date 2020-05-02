from __future__ import absolute_import, unicode_literals
from celery import Celery

CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'
CELERY_RESULT_BACKEND = 'rpc://'

REDIS_URL = 'redis://redis:6379/0'
# BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'

CELERY = Celery('c',
                # backend=CELERY_RESULT_BACKEND,
                broker=REDIS_URL,
                )
# CELERY = Celery()
# CELERY.config_from_object('config', namespace='CELERY')

pfiles = ['tasks']
CELERY.autodiscover_tasks(pfiles,force=True)

# print("tasks={}".format( CELERY.tasks.keys() ))