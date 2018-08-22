import requests as r
from bs4 import BeautifulSoup as bs
import time
import json
import pymysql

while 1:
    try:
        user = input('MYSQL user 이름을 입력하세요 : ')
        ps = input('MYSQL 비밀번호를 입력하세요 : ')
        infolist = ['user','company']
        connection = pymysql.connect(host='localhost',
                                          user=user,
                                          password=ps,
                                          db='2018sw',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        break

    except pymysql.err.OperationalError:
        print("user이름과 password를 확인하세요")

def get_newest_db():

    sql = "SELECT * FROM mainpage_notice ORDER BY id DESC LIMIT 1"

    with connection.cursor() as cursor:
        cursor.execute(sql)
        last_title = cursor.fetchall()

    return json.dumps(last_title[0], ensure_ascii = False, indent = 2)

def get_newest_homepage():
    po = {'p_pageno' : 1}
    raw = r.post('http://www.pknu.ac.kr/usrBoardActn.do?p_bm_idx=5&p_boardcode=PK10000005', po)
    soup = bs(raw.content, 'html.parser')
    sel = soup.find('tbody')
    combined_info = []

    urls = [i['href'] for i in sel.find_all('a')]
    urls = urls[7:]

    for i in urls:
        get_title = r.get('http://pknu.ac.kr'+i)
        soup = bs(get_title.content, 'html.parser')
        raw_info = soup.find_all('td')

        info = {'title' : raw_info[0].text.strip(),
                'date' : raw_info[1].text.strip(),
                'author' : raw_info[2].text.strip(),
                'url' : ('http://pknu.ac.kr'+i).strip()}

        combined_info.append(info)

    return combined_info
