from flask import Flask , request , render_template, url_for, redirect
app = Flask (__name__)
 
@app.route('/',methods=['GET'])
def main():
   return render_template("home.html")

@app.route('/search', methods=['POST'])
def search():
   value = request.form['context'] # value는 값이 다음 페이지(search)로 넘어가게 됨




# result = []
# @app.route('/search',methods=['GET'])
# def search():
#       if (request.method == 'GET'):
#          return render_template("home.html")



if __name__ == "__main__":
      app.run()


   # if request.method == '': # home.html 에서 입력받은 date, input 를 가져와서 result 변수에 추가
   #    # date = request.form['date']  #검색날짜 가져오기
   #    input = request.form['input']
   #    result.append([input])
   #    # return redirect(url_for('result'))    #result 를 리다이렉트
   #    return "success"
   # # else: return render_template('home.html', rows = result)


#
#
# if __name__ == "__main__":
#     app.run()