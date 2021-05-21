from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.hanbit.co.kr/media/books/book_view.html?p_code=B2649943562")
bs = BeautifulSoup(html, 'html.parser')
title = bs.select("#container > div.store_view_wrap > div.store_view_wrap_l > div.store_view_area > div.store_product_info_box > h3")
print(title)
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


   