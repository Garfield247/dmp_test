from hdfs3 import HDFileSystem

cli = HDFileSystem(host="192.168.3.140",post=8020)


cli.ls("/")
