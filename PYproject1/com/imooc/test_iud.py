import pymysql

conn = pymysql.Connect(host='localhost', port=3306, user='root', passwd='200396', db='imooc', charset='utf8')
cursor = conn.cursor()

sql_insert = "insert into user(userid, username) values(10,'name10')"
sql_update = "update user set username = 'name91' where userid = 9"
sql_delete = "delete from user where userd < 3"

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)

    conn.commit()
except Exception as e:
    print (e)
    conn.rollback()

cursor.close()
conn.close()