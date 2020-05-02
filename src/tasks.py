import string
from celery import shared_task
import logging
from recengine import recommend_movie

# async_recommend = shared_task(recommend_movie)

@shared_task
def addasync(a,b):
    logging.info('We are Task in celery: addasync')
    return a+b
