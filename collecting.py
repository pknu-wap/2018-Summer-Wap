# 학과 공지사항 모아오기
# 제목, 작성자, 작성일, 링크
#공지사항 전체다 끌어옴(빼야할 것: num가 ...된 것들)
import requests as r
from bs4 import BeautifulSoup as bs

a = r.get("http://cms.pknu.ac.kr/pkuocean/view.do?no=1253")
soup = bs(a.content, 'html.parser')
soup2 = soup.find_all('ul', {'id' : 'board_list'})

content = []

for i in soup2:
    i = i.select('h4')
    for j in i:
        content.append(j.get_text().strip())

for j in content:
    print(j)