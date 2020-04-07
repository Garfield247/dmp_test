from flask import Blueprint
# from app.utils import ftp_server_hanlder
from app.utils.celery_tools import test


work = Blueprint("work",__name__)


@work.route("/celerytest/<int:x>_<int:y>/")
def ctest(x,y):
    res = test.delay(int(x),int(y))
    return res.get(timeout=1)


# @work.route("/ftptest/")
# def ffffff():
#     username = "user_a"
#     passwd = "123456"
#     homedir = "./"
#     port = 3445
#     res = ftp_server_hanlder(username,passwd,homedir,port)
#     return res.id
