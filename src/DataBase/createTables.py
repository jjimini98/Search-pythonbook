import pymysql

ip = '118.67.131.97'
port = 3306
user = 'root'
pw = 'jimin980908'
db_name = 'pyinder'


conn = pymysql.connect(host = ip, port = port , user = user , password= pw , db = db_name)

cursor = conn.cursor()

sql1 ='''CREATE TABLE Book ( 
   id INT NOT NULL AUTO_INCREMENT ,
   title VARCHAR(255) NOT NULL,
   picture LONGBLOB,
   intro VARCHAR(1000) NOT NULL, 
   Tag_id INT NOT NULL,
   PRIMARY KEY (id) ) '''
# intro의 데이터타입 500으로 부족해서 1000으로 늘림 


sql2 = ''' CREATE TABLE Review ( 
   review_id INT NOT NULL AUTO_INCREMENT,
   user_id INT NOT NULL,
   contents VARCHAR(255) NOT NULL,
   date DATE NOT NULL,
   rate FLOAT NOT NULL,
   Book_id INT NOT NULL,
   PRIMARY KEY (review_id) ) ''' 


sql3 = '''CREATE TABLE Tag ( 
   id INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(100) NOT NULL,
   PRIMARY KEY (id) )''' 

sql4 = '''CREATE TABLE Search ( 
   id INT NOT NULL AUTO_INCREMENT,
   keyword VARCHAR(255) NOT NULL,
   count INT NOT NULL,
   PRIMARY KEY (id) )'''

sql5 = '''ALTER TABLE Review ADD CONSTRAINT Book_Review FOREIGN KEY (Book_id) REFERENCES Book(id) ''' 


sql6 = '''ALTER TABLE Book ADD CONSTRAINT Tag_Book FOREIGN KEY (Tag_id) REFERENCES Tag(id)'''



cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
cursor.execute(sql6)



conn.commit()
conn.close() 

