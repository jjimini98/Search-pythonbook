import pymysql 

ip = '118.67.131.97'
port = 3306
user = 'root'
pw = 'jimin980908'
db_name = 'test'

conn = pymysql.connect(host = ip, port = port , user = user , password= pw , db = db_name)
cursor = conn.cursor()


# datalist = ["위키북스 책소개.txt", "이지스퍼블리싱 책소개.txt", "한빛미디어 책소개.txt"]
data = "test.txt"

def get_title_contents(data):
   res  = list()
   Flag = 0
   route = "C:\\Users\\jimin\\vscode\\DataArchitecture\\dataset\\"

   with open(route + data, "r", encoding='utf-8') as file:
      line = file.readlines()
      for x in line :

         if x == '\n': 
            Flag +=1
            continue

         elif Flag ==2 and x != '\n': 
            title = x 
            title = title.rstrip()

            Flag = 0
            
         elif Flag == 0 and x != title: 
            contents = x 
            contents = contents.rstrip()
            

            res.append([title, contents])
   return res
            
         

sql = '''INSERT INTO Book(title, intro) values (%s, %s) '''


for x in get_title_contents(data):
   cursor.execute(sql, (x[0],x[1]))

conn.commit()