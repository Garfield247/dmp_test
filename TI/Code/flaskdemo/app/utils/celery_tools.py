from celery import Celery
from flask import current_app
from app.celery_config import *

celery_app = Celery(__name__,backend=result_backend,borker=broker_url)

@celery_app.task
def test(x,y):
    return str(x+y)
