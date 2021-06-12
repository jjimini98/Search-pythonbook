import pymysql

ip = '118.67.131.97'
port = 3306
user = 'root'
pw = 'jimin980908'
db_name = 'pyinder'

conn = pymysql.connect(host = ip, port = port , user = user , password= pw , db = db_name)
cursor = conn.cursor()

tag_list = ["파이썬", "기초", "딥러닝", "초보", "수학", "머신러닝", "Tensorflow", "비전공자", "입문서", "자료구조", "중고급", "입문자","알고리즘", "중급"]

sql = '''INSERT INTO Tag(name) VALUES (%s)'''


for x in tag_list:
   cursor.execute(sql,x)

conn.commit()
conn.close()