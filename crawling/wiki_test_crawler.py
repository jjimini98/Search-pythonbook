from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen



# 원래 방법대로 하면 크롤링 권한이 막히는 <urllib.error.HTTPError: HTTP Error 403: Forbidden> 문제가 생기므로 다른 방법으로 시도 
req = Request('https://wikibook.co.kr/pyexcel/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read().decode() #html문서 가졍오기 
bs = BeautifulSoup(webpage, 'html.parser',from_encoding='utf-8')
title = bs.select("#content > div:nth-child(2) > div > div")
print(bs.find('p'))

# title = bs.select("#content > div:nth-child(2) > div > div")
# print(title)
# for t in title: 
#    with open("./crawling/wiki_python_crawling.txt","a", encoding='utf-8') as f:
#       f.write(t.text)
#       f.write("\n")


# context = bs.select("#tabs_1 > div > p:nth-child(3)")
# for c in context:
#    with open("./crawling/wiki_python_crawling.txt","a", encoding='utf-8') as f:
#          f.write(c.text)
#          f.write("\n")
#          f.write("\n")


# #url 모음에서 한 줄씩 읽어서 크롤러 함수에 인자로 넣음. 
# with open("./crawling/wiki_python_url.txt","r") as f :
#    while True:
#       line = f.readline()
#       if not line: break
#       hanbit_python_crawler(line)

#크롤링할 때 생기는 빈칸들(제대로 크롤링되지 않은 것들)은 손수 삭제함.