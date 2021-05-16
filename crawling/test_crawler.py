# 일단 알라딘으로 크롤링 

from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=193931483")
soup = BeautifulSoup(html, "html.parser")
pr = soup.find_all("div", {"class":"Ere_prod_mconts_box"})

print(pr)
