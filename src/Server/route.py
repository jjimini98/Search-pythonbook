from flask import Flask , request , render_template, url_for, redirect
import pymysql
app = Flask (__name__)

ip = '118.67.131.97'
port = 3306
user = 'root'
pw = 'jimin980908'
db_name = 'pyinder'

conn = pymysql.connect(host=ip, port=port, user=user, password=pw, db=db_name)
cursor = conn.cursor()


from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
lis = []
data = {}
result = []

@app.route('/')
def index(): # 리스트(board)를 html 파일로 넘기기
 return render_template('home.html', rows = lis)

@app.route('/search', methods = ['POST'])
def add():
    if request.method == 'POST':
        question = request.form['input']
        lis.append(question)
        data = question
        sql = """insert into Search (keyword) values (%s)"""
        cursor.executemany(sql,data)
        conn.commit()

        sql = '''SELECT title, intro FROM Book'''
        cursor.execute(sql)
        answer = cursor.fetchall()
        for each in answer:
            for x in each:
                if question in x:
                    result.append(x)

    return render_template('search.html', data= [result, question])



if __name__ == '__main__':
    app.run()






# @app.route('/',methods=['GET'])
# def main():
#
#     return render_template("home.html", data= "")
#
#
# @app.route('/search', methods=['POST'])
# def search():
#     result = []
#     value = request.form['input'] # value는 값이 다음 페이지(search)로 넘어가게
#
#     sql = '''SELECT intro FROM Book'''
#     cursor.execute(sql)
#     answer = cursor.fetchall()
#
#     for x in answer:
#         for t in x:
#             if value in t:
#                 result.append(t)
#     return  render_template('search.html')





if __name__ == "__main__":
      app.run()


