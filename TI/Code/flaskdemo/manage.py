import os
from flask_script import Manager,Server
from app import create_app

# 获取配置名称
config_name = os.environ.get("FLASK_CONFIG") or 'default'
# 创建应用实例
app = create_app(config_name)
# 使用Manager对APP进行接管
manager = Manager(app)
# 添加服务启动的命令行脚本
manager.add_command("runserver",Server(host="0.0.0.0",port=5555))



if __name__ == "__main__":
    manager.run()
