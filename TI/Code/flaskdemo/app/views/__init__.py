from .main import main
from .users import user
from .datas import data
from .works import work


DEFAULT_BLUEPRINT = (
    (main,''),
    (user,'/user'),
    (data,'/data'),
    (work,'/work'),
)

def config_blueprint(app):
    for blueprint,prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint,url_prefix=prefix)
