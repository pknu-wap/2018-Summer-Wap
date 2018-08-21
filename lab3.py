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
                                          db='gohwak',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        break

    except pymysql.err.OperationalError:
        print("user이름과 password를 확인하세요")

def check_new():
    raw = r.post('http://www.pknu.ac.kr/usrBoardActn.do?p_bm_idx=5&p_boardcode=PK10000005', {'p_pageno' : 1})
    soup = bs(raw.content, 'html.parser')
    sel = soup.find('tbody')

    urls = [i['href'] for i in sel.find_all('a')]
    urls = urls[7:]
    print(urls)
    sql = "SELECT title FROM mainpage_notice ORDER BY id DESC LIMIT 1"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        last_title = cursor.fetchall()

    for i in urls:
        get_title = r.get('http://pknu.ac.kr/%27'+i)
        soup = bs(get_title.content, 'html.parser')
        raw_info = soup.find_all('td')
        info = raw_info[0].text.strip()
        print(info)
check_new()