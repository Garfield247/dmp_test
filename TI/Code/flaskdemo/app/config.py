import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config():
    # 系统秘钥 设置从服务器环境变量获取或者使用shtddsj123.
    SECRET_KEY = os.environ.get("SECRET_KEY") or "shtddsj123."
    # 数据库相关设置
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_REARDOWN = True

    UPLOADED_PATH = os.path.join(base_dir,"uploads")

    # CELERY_BROKER_URL='redis://0.0.0.0:6379/0'
    # CELERY_RESULT_BACKEND='redis://0.0.0.0:6379/0'
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir,"dmp-dev.sqlite")

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir,"dmp-test.sqlite")

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir,"dmp-pro.sqlite")


config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,

    'default':DevelopmentConfig,
}
