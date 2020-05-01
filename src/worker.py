from __future__ import absolute_import, unicode_literals
from celery import Celery

REDIS_URL = 'redis://redis:6379/0'
BROKER_URL = 'amqp://admin:mypass@rabbitmq:5672//'

CELERY = Celery(
                backend=REDIS_URL,
                broker=BROKER_URL)

# CELERY.autodiscover_tasks()

# print("tasks={}".format( CELERY.tasks.keys() ))