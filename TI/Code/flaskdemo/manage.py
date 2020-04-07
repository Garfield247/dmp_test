from app import dmp_app
from flask_script import Manager,Server

# 使用Manager对APP进行接管
manager = Manager(dmp_app)
# 添加服务启动的命令行脚本
manager.add_command("runserver",Server(host="0.0.0.0",port=5555,use_debugger=True))



if __name__ == "__main__":
    manager.run()
