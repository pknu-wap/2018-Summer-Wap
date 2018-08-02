from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests as r
import re


w = r.get("http://cms.pknu.ac.kr/pkuocean/view.do?no=1253")

l = 'http://cms.pknu.ac.kr'
w_list = bs(w.content, "html.parser")
u = w_list.select('li > a')
w2_list = w_list.find('ul', {'id' : 'board_list'})
lis = w2_list.find_all("li")



for li in lis:
    a_tag = li.find("a")
    num= a_tag.find("span",{'class' : 'num'})
    if num.text == '':
        continue   
    title= a_tag.find("h4")
    print(title.get_text().strip())
    span1= a_tag.find("span",{'class' : 'date'})
    print(span1.text)
    span2= a_tag.find("span",{'class' : 'writer'})
    print(span2.text)
    urls=li.find("a")
    urls=l + urls.get('href')
    
    desc = r.get(urls)
    soup = bs(desc.content, 'html.parser')
    #print(soup.find('a'))
    lis2 = soup.find('div', {'class' : 'board_stance'})
    desc = lis2.text
    print(desc)

print('----------------------------------------------------------------------------')