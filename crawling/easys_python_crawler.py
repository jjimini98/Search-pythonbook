rom urllib.request import urlopen
from bs4 import BeautifulSoup


def easys_python_crawler(url): 
   site = urlopen(url)
   bs = BeautifulSoup(site, 'html.parser',from_encoding='utf-8')
   title = bs.select("#BOOK_TITLE")
   for t in title: 
      with open("./crawling/easys_python_crawling.txt","a", encoding='utf-8') as f:
         f.write(t.text)
         f.write("\n")


   context = bs.select("#tab03 > div > p:nth-child(3)")
   for c in context:
      with open("./crawling/easys_python_crawling.txt","a", encoding='utf-8') as f:
            f.write(c.text)
            f.write("\n")
            f.write("\n")


#url 모음에서 한 줄씩 읽어서 크롤러 함수에 인자로 넣음. 
with open("./crawling/easys_python_url.txt","r") as f :
   while True:
      line = f.readline()
      if not line: break
      easys_python_crawler(line)
