import pymysql

ip = '118.67.131.97'
port = 3306
user = 'root'
pw = 'jimin980908'
db_name = 'pyinder'

conn = pymysql.connect(host = ip, port = port , user = user , password= pw , db = db_name)
cursor = conn.cursor()

tag_list = ['초보자', ]