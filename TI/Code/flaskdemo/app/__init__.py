import os
from flask import Flask
from app.config import config
from app.extensions import config_extensions
from app.views import config_blueprint
from app.celery_config import *


def create_app(config_name):
    # 创建flask实例
    app = Flask(__name__)
    # 载入配置
    app.config.from_object(config.get(config_name) or config['default'])
    # 初始化配置
    config[config_name].init_app(app)
    # 注册插件
    config_extensions(app)
    # 注册蓝本
    config_blueprint(app)
    return app


# celery
def make_celery(app):
    celery = Celery(__name__,broker=broker_url)
    celery.config_from_object('celery_config')
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery

# 获取配置名称
config_name = os.environ.get("FLASK_CONFIG") or 'default'
# 创建应用实例
dmp_app = create_app(config_name)
celery_ = make_celery(dmp_app)
