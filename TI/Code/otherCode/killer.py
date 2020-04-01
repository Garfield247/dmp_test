import os
import sys


def killport(port):
    command="netstat -nlp|grep :"+str(port)+"|awk '{print $7}'|awk -F '/' '{print $1}'|xargs kill -9 "
    print(command)
    res = os.system(command)
    print(res)


p=input("PORT")
killport(p)
