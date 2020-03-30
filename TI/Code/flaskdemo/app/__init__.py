from flask import Flask
from app.config import config
from app.extensions import config_extensions
from app.views import config_blueprint



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
