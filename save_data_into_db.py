from bs4 import BeautifulSoup as bs
import requests as r
import re
import pymysql


conn = pymysql.connect(host = 'localhost',
                               user = 'root',
                               password = 'unggung9236',
                               db = 'WAP',
                               charset = 'utf8mb4',
                               cursorclass = pymysql.cursors.DictCursor)



for i in range(1,9):
    w = r.get("http://cms.pknu.ac.kr/pkuocean/view.do?no=1253&pageIndex=%d&view=list&sv=TITLE&sw=" %i)

    l = 'http://cms.pknu.ac.kr'
    w_list = bs(w.content, "html.parser")
    u = w_list.select('li > a')
    w2_list = w_list.find('ul', {'id' : 'board_list'})
    lis = w2_list.find_all("li")
    print(i)

    for li in lis:
        a_tag = li.find("a")
        num= a_tag.find("span",{'class' : 'num'})
        if num.text == '':
            continue
        title= a_tag.find("h4")
        title = (title.get_text().strip())
        t = title
        date= a_tag.find("span",{'class' : 'date'})
        date0 = (date.text)
        d = date0
        writer= a_tag.find("span",{'class' : 'writer'})
        writer0 = (writer.text)
        wr = writer0
        url=li.find("a")
        urls=l + url.get('href')
        urls0 = (urls)
        u = urls0

        desc = r.get(urls)
        soup = bs(desc.content, 'html.parser')
        #print(soup.find('a'))
        lis2 = soup.find('div', {'class' : 'board_stance'})
        desc = lis2.text
        desc0 = (desc)
        de = desc0


        with conn.cursor() as cursor:
            cursor = conn.cursor()
            sql = 'INSERT INTO note_crawling (title, description, created, author, url) VALUES ("%s", "%s", "%s", "%s", "%s")' %(t,de,d,wr,u)
            print(sql, t, de, d, wr, u)
            cursor.execute(sql)
            conn.commit()
            print('==========================')

conn.close()
