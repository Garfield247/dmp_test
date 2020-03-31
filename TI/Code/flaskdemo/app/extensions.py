from flask_cors import CORS





def config_extensions(app):
    CORS(app,supports_credentials=True)




