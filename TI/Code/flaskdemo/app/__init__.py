
from flask import Flask
from app.extensions import config_extensions
from app.views import config_blueprint
from app.utils import celery_app
from app.config import config
# from app.celery_config import celery_conf

def create_app(config_name):
    # 创建flask实例
    app = Flask(__name__)
    # celery_app.config_from_object('app.celery_config')
    # celery_app.conf.update(celery_conf)
    # 载入配置
    app.config.from_object(config.get(config_name) or config['default'])
    # 初始化配置
    config[config_name].init_app(app)
    # 注册插件
    config_extensions(app)
    # 注册蓝本
    config_blueprint(app)
    return app


