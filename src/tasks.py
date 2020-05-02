import logging
from recengine import recommend_movie
from cworker import CELERY as c


async_recommend = c.task(recommend_movie)

@c.task
def addasync(a,b):
    logging.info('We are Task in celery: addasync')
    return a+b
