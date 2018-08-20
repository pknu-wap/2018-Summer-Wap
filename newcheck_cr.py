import requests as r
from bs4 import BeautifulSoup as bs
import time
import json

def run_check():
    while 1:
        raw = r.post('http://www.pknu.ac.kr/usrBoardActn.do?p_bm_idx=5&p_boardcode=PK10000005', {'p_pageno' : 1})
        soup = bs(raw.content, 'html.parser')
        sel = soup.find('tbody')

        urls = [i['href'] for i in sel.find_all('a')]

        for i in urls:
            get_title = r.get('http://pknu.ac.kr'+i)
            soup = bs(get_title.content, 'html.parser')
            raw_info = soup.find_all('td')
            info = {'title' : raw_info[0].text,
                    'date' : raw_info[1].text,
                    'author' : raw_info[2].text,
                    'url' : "http://pknu.ac.kr"+i}

            print(json.dumps(info, indent = 2, ensure_ascii = False))
        print('done')
        time.sleep(100)
