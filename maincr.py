import requests as r
from bs4 import BeautifulSoup as bs

def get_info(i):
    po = {'p_pageno' : i}
    raw = r.post('http://www.pknu.ac.kr/usrBoardActn.do?p_bm_idx=5&p_boardcode=PK10000005', po)
    soup = bs(raw.content, 'html.parser')
    sel = soup.find('tbody')
    info = []

    titles = [i.text.strip() for i in sel.find_all('a')]
    authors = [i.text.strip() for i in sel.find_all('td', {'class' : 'author'})]
    dates = [i.text.strip() for i in sel.find_all('td', {'class' : 'date'})]
    urls = [i['href'] for i in sel.find_all('a')]

    for i in range(len(titles)):
        info.append([[titles[i],authors[i],dates[i],'http://www.pknu.ac.kr'+urls[i]]])

    print(info)

for i in range(1,200):
    get_info(i)
