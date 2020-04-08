from celery import Celery
from flask import current_app
from app.celery_config import *

# celery_app = Celery(__name__)
# celery_app.conf.update(celery_conf)
# celery_app.conf.update(task_serializer = 'json',
#         result_serializer = 'json',
#         accept_content = ['json'],
#         timezone = 'Asia/Shanghai',
#         enable_utc = True,
#         )
def make_celery():
    celery = Celery(
        __name__,
        backend= CELERY_RESULT_BACKEND,
        broker= BROKER_URL
    )
    celery.config_from_object('app.celery_config')

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with current_app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
celery_app = make_celery()

@celery_app.task
def test(x,y):
    return str(x+y)
