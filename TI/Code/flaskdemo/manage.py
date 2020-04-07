import os
from flask import Flask
from app import create_app
from app.utils import celery_app
from flask_script import Manager,Server

# 获取配置名称
config_name = os.environ.get("FLASK_CONFIG") or 'default'
# 创建应用实例
dmp_app = create_app(config_name)
dmp_app.app_context().push()
# 使用Manager对APP进行接管
manager = Manager(dmp_app)
# 添加服务启动的命令行脚本
manager.add_command("runserver",Server(host="0.0.0.0",port=5555,use_debugger=True))



if __name__ == "__main__":
    manager.run()
