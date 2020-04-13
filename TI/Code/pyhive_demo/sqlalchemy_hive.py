from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *


engine  = create_engine("presto://192.168.3.140:10000/test/emp")
logs = Table("")
