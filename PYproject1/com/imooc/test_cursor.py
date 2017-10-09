import pymysql

conn = pymysql.Connect(host='localhost', port=3306, user='root', passwd='200396', db='imooc', charset='utf8')
cursor = conn.cursor()

sql = 'select * from user'
cursor.execute(sql)

print (cursor.rowcount)
rs  = cursor.fetchone()
print (rs)

rs = cursor.fetchmany(3)
print (rs)

rs = cursor.fetchall()
print (rs)



cursor.close()
conn.close()