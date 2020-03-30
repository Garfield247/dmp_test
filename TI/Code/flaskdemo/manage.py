from flask_script import Manager,Server
from app import create_app

config_name = os.environ.get("FLASK_CONFIG") of 'default'

app = create_app(config_name)

manager = Manager(app)

manager.add_command("runserver",Server(host="0.0.0.0",port=5555))

if __name__ == "__main__":
    manager.run()
