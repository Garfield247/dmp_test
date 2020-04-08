from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from app.utils import celery_app


@celery_app.task
def ftp_server_hanlder(username,passwd,homedir,port):
    authorizer = DummyAuthorizer()
    authorizer.add_user(username=username,password=passwd,homedir=homedir)
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.passive_ports = range(2000,4000)
    server = FTPServer(('0.0.0.0',port),handler)
    server.serve_forever()
