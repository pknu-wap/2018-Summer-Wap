import requests as r
from bs4 import BeautifulSoup as bs
import json
import pymysql

connection = pymysql.connect(host='localhost',
                             user='jeong',
                             password='qwe123',
                             db='2018SW',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def get_info(i):
    po = {'p_pageno' : i}
    raw = r.post('http://www.pknu.ac.kr/usrBoardActn.do?p_bm_idx=5&p_boardcode=PK10000005', po)
    soup = bs(raw.content, 'html.parser')
    sel = soup.find('tbody')
    info = []

    urls = [i['href'] for i in sel.find_all('a')]
    urls = urls[7:]
    urls.reverse()


    for i in urls:
        get_title = r.get('http://pknu.ac.kr'+i)
        soup = bs(get_title.content, 'html.parser')
        raw_info = soup.find_all('td')

        info = {'title' : raw_info[0].text.strip(),
                'date' : raw_info[1].text.strip(),
                'author' : raw_info[2].text.strip(),
                'url' : ('http://pknu.ac.kr'+i).strip()}

        if '"' in info['title']:
            sql = f"INSERT INTO mainpage_notice (url, title, author, date) VALUES ('{info['url']}','{info['title']}','{info['author']}','{info['date']}')"
        else:
            sql = f'INSERT INTO mainpage_notice (url, title, author, date) VALUES ("{info["url"]}","{info["title"]}","{info["author"]}","{info["date"]}")'
        with connection.cursor() as cursor:
            cursor.execute(sql)
        connection.commit()
        print(info)


for i in range(590,0,-1):
    get_info(i)
