from flask_cors import CORS
from app.utils import make_celery


def config_extensions(app):
    CORS(app)
    # celery插件


