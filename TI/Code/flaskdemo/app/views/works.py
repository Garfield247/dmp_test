from flask import Blueprint
from app.utils import ftp_server_hanlder
from app.utils.celery_tools import test
from app.utils import celery_app


work = Blueprint("work",__name__)


@work.route("/celerytest/<int:x>_<int:y>/")
def ctest(x,y):
    res = test.delay(int(x),int(y))
    return str(res.ready())


@work.route("/ftptest/")
def ffffff():
    username = "user_a"
    passwd = "123456"
    homedir = "./"
    port = 3475
    res = ftp_server_hanlder.delay(username,passwd,homedir,port)
    return res.id




@work.route("/killtask/<task_id>")
def killer(task_id):
    celery_app.control.revoke(task_id, terminate=True)
    return "OK"
