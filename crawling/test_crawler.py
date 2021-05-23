from urllib.request import urlopen
from bs4 import BeautifulSoup


def hanbit_crawler(url): 
   site = urlopen(url)
   bs = BeautifulSoup(site, 'html.parser',from_encoding='utf-8')
   title = bs.select("#container > div.store_view_wrap > div.store_view_wrap_l > div.store_view_area > div.store_product_info_box > h3")
   for t in title: 
      with open("./crawling/hanbit_crawling.txt","a", encoding='utf-8') as f:
         f.write(t.text)
         f.write("\n")

   context = bs.select("#tabs_1 > div > p:nth-child(3)")
   print("context is")
   print(context)
   for t in context:
      with open("./crawling/hanbit_crawling.txt","a", encoding='utf-8') as f:
         f.write(t.text)
         f.write("\n")




hanbit_crawler("https://www.hanbit.co.kr/media/books/book_view.html?p_code=B7267069633")