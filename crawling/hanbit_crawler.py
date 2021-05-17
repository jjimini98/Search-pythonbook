# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen("https://www.hanbit.co.kr/media/books/book_view.html?p_code=B8494674601")
# bs = BeautifulSoup(html,"html.parser")
# for x in bs.select("#tabs_1"):
#    print(x)


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.hanbit.co.kr/media/books/book_view.html?p_code=B9090689318")
bs = BeautifulSoup(html, 'html.parser')
title = str(bs.select("#container > div.store_view_wrap > div.store_view_wrap_l > div.store_view_area > div.store_product_info_box > h3"))
