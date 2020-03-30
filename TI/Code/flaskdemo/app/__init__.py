from flask import Flask
from app.config import config


def create_app(config_name):
    # 创建flask实例
    app = Flask(__name__)
    # 载入配置
    app.config.from_object(config.get(config_name) or config['default'])
    # 初始化配置
    config[config_name].init_app(app)

    return app
