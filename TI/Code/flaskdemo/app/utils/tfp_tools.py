from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()

authorizer.add_user(username='user',password='12345',homedir='./')



handler = FTPHandler
handler.authorizer = authorizer




handler.passive_ports = range(2000,4000)



server = FTPServer(('0.0.0.0',3221),handler)

server.serve_forever()
