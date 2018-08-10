import requests as r
import pymysql
from bs4 import BeautifulSoup as bs

conn = pymysql.connect(host = 'localhost',
                               user = 'root',
                               password = 'unggung9236',
                               db = 'WAP',
                               charset = 'utf8mb4',
                               cursorclass = pymysql.cursors.DictCursor)

notice = r.get("http://cms.pknu.ac.kr/pkuocean/view.do?no=1253&pageIndex=1&view=list&sv=TITLE&sw=")

soup = bs(notice.content, 'html.parser')

l = 'http://cms.pknu.ac.kr'
u = soup.select('li > a')
w2_list = soup.find('ul', {'id' : 'board_list'})
lis = w2_list.find_all("li")

def cr():
    check = 0
    for li in lis:
        a_tag = li.find("a")
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

        try:
            with conn.cursor() as cursor:
                cursor = conn.cursor()
                sql = 'INSERT INTO note_crawling (title, description, created, author, url) VALUES ("%s", "%s", "%s", "%s", "%s")' %(t,de,d,wr,u)
                cursor.execute(sql)
                conn.commit()
                check += 1
                print('==========================')
        
        except Exception as e:
            print(e)

    if check != 0:
        print("새로운 게시글이 있습니다.")
    else:
        print("새로운 게시글이 없습니다.")

cr()