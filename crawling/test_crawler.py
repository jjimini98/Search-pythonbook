from urllib.request import urlopen
from bs4 import BeautifulSoup


def hanbit_python_crawler(url): 
   site = urlopen(url)
   bs = BeautifulSoup(site, 'html.parser',from_encoding='utf-8')
   title = bs.select("#container > div.store_view_wrap > div.store_view_wrap_l > div.store_view_area > div.store_product_info_box > h3")
   for t in title: 
      with open("./crawling/hanbit_python_crawling_test.txt","a", encoding='utf-8') as f:
         f.write(t.text)
         f.write("\n")


   #hanbit_python_crawler로 안되던 내용들을 이렇게 바꾸면 크롤링이 됨. 
   context = bs.select("#tabs_1 > div > p:nth-child(4)")

   for c in context:
      with open("./crawling/hanbit_python_crawling_test.txt","a", encoding='utf-8') as f:
         f.write(c.text)
         f.write("\n")
         f.write("\n")



#url 모음에서 한 줄씩 읽어서 크롤러 함수에 인자로 넣음. 
# with open("./crawling/hanbit_python_url.txt","r") as f :
#    while True:
#       line = f.readline()
#       if not line: break
#       hanbit_python_crawler(line)

hanbit_python_crawler("https://www.hanbit.co.kr/media/books/book_view.html?p_code=B2649943562")
