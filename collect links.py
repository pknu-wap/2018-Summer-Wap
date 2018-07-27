import requests as r
from bs4 import BeautifulSoup as bs

l = r.get("http://cms.pknu.ac.kr/pkuocean/view.do?no=1253")
soup = bs(l.content, 'html.parser')
url = soup.select(
    'li > a'
)
for link in url:
    print(link.get('href'))


#일단 뽑는데 의.의를 두었다. 정리는 내일..
