from flask import Blueprint
from app.utils import ftp_server_hanlder
work = Blueprint("work",__name__)


@work.route("/ftptest/")
def ffffff():
    username = "user_a"
    passwd = "123456"
    homedir = "./"
    port = 3445
    res = ftp_server_hanlder(username,passwd,homedir,port)
    return res.id
