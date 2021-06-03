import pymysql

conn = pymysql.connect(host = '118.67.131.97',
                        port = 3306,
                        user = 'root',
                        password = 'jimin980908',
                        charset = 'utf8')


cursor = conn.cursor()

sql = "CREATE DATABASE pyinder"

cursor.execute(sql)

conn.commit()
conn.close() 