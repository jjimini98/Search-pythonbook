import pymysql


ip = '118.67.131.97'
port = 3306
user = 'root'
pw = 'jimin980908'
db_name = 'pyinder'

value = "파이썬"

conn = pymysql.connect(host=ip, port=port, user=user, password=pw, db=db_name)
cursor = conn.cursor()
sql = '''SELECT intro FROM Book'''
cursor.execute(sql)
result = cursor.fetchall()
# return render_template('search.html',value = value)
# for x in result:
#     for t in x :
#         if value in t :
