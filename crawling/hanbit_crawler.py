from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.hanbit.co.kr/media/books/book_view.html?p_code=B2649943562")
bs = BeautifulSoup(html, 'html.parser')
#타이틀 부분 코드는 아무 사이트나 넣어도 돌아감! 이 코드는 재사용이 가능하겠다. 
title = bs.select("#container > div.store_view_wrap > div.store_view_wrap_l > div.store_view_area > div.store_product_info_box > h3")


context = bs.select("#tabs_1")
print(context)




import urllib.request
from bs4 import BeautifulSoup
 
#여기에 함수를 구현해봅시다.
req = urllib.request.urlopen("https://www.hanbit.co.kr/media/books/book_view.html?p_code=B2649943562")
res = req.read()
 
soup = BeautifulSoup(res,'html.parser')
keywords = context.find("li")
#get_text() == 데이터에서 문자열만 추출
#strip() == 데이터의 양옆 공백제거
#[:20]의 이유? 인기검색어의 중복을 막고 20위까지만 출력하기 위함
keywords = [each_line.get_text().strip() for each_line in keywords]
# print(keywords)



# title result : [<h3>실전 시계열 분석</h3>]
# 텍스트만 꺼내야함
# for t in title: 
#    with open("./crawling/hanbit_crawling.txt","w") as f:
#       f.write(t.text)
#       f.write("\n")

# context = bs.select("#tabs_1 > div > p:nth-child(3)")

# for t in context:
#    with open("./crawling/hanbit_crawling.txt","a") as f:
#       f.write(t.text)
#       f.write("\n")
#       f.write("\n")





   