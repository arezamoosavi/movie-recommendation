from __future__ import absolute_import, unicode_literals
from celery import Celery


REDIS_URL = 'redis://redis:6379/0'
BROKER_URL = 'amqp://admin:mypass@rabbitmq:5672'
BACKEND = 'rpc://'

CELERY = Celery('tcelery',
                broker=BROKER_URL,
                backend=REDIS_URL,
                include=['tasks']
                )

# pfiles = ['tasks']
# CELERY.autodiscover_tasks(pfiles,force=True)