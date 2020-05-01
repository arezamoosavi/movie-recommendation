import string
from celery import shared_task
import logging
from recengine import recommend_movie

logger = logging.getLogger(__name__)

logger.info('In tasks')

async_recommend = shared_task(recommend_movie)
