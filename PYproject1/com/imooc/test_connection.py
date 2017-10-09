import pymysql

conn = pymysql.Connect(host='localhost', port=3306, user='root', passwd='200396', db='imooc', charset='utf8')
cursor = conn.cursor()

print (conn)
print (cursor)

cursor.close()
conn.close()