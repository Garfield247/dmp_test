from pyhive import hive

conn = hive.Connection(host="192.168.3.140",port=10000,database="test",username="root",password=None)
cursor =  conn.cursor()
cursor.execute("select * from emp limit 10")
for result in cursor.fetchall():
    print(result)

cursor.close()
conn.close()



