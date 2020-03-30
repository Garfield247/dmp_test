from flask_dropzone import Dropzone



dropzone = Dropzone()


def config_extensions(app):
    dropzone.init_app(app)




