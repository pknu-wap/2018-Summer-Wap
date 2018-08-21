from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
import pymysql
import json

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='111111',
                       db='gohwak',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

curs = conn.cursor()
sql = "select * from itcroll"
curs.execute(sql)
rows = curs.fetchall()
before_update = rows[0]
bef_json = json.dumps(before_update,indent=2,ensure_ascii=False)
bef_url = json.loads(bef_json).get('url')
print(bef_url)


itcae = requests.get("http://cms.pknu.ac.kr/itcae/view.do?no=9576").text

itcae_table = bs(itcae,"html.parser")
urls = []

itcae = itcae_table.find(name="ul", attrs={"id": "board_list"})
for link in itcae.find_all(name="li"):
    urls.append(link.find('a')['href'])


for url in urls:
    check = 0
    itcae_url = requests.get('http://cms.pknu.ac.kr'+ url).text
    itcae_contents = bs(itcae_url,"html.parser")

    urrl = ('http://cms.pknu.ac.kr'+ url)

    contents = ""
    for link in itcae_contents.find_all(name="div", attrs={"id":"board_view"}):

        titlescrap = link.find('h3')
        namedate = link.find_all('strong')

        title = (titlescrap.text)
        writer = (namedate[0].text)
        date = (namedate[1].text)

        # print(date,'     ',title,'     ',writer)

    for link in itcae_contents.find_all(name="div", attrs={"class": "board_stance"}):

        if check == 0:
            check = 1
            contents += link.text
        else:
            contents = contents + "\n"+ link.text

    #     print(contents)
    # print('-----------------------------------------------------------------------------------')

    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO itcroll (title, created, writer, url, content) VALUES ("%s", "%s","%s", "%s", "%s")' %(title, date, writer, urrl, contents)
            cursor.execute(sql)
        conn.commit()
    except:
        continue

sql = "select * from itcroll"
curs.execute(sql)
rows = curs.fetchall()
after_update = rows[0]
aft_json = json.dumps(before_update,indent=2,ensure_ascii=False)
aft_url = json.loads(aft_json).get('url')
print(aft_url)

if bef_url == aft_url:
    print('새로 추가된 내용이 없습니다.')
else:
    print('공지사항이 추가되었습니다.','\n',rows[0])
conn.close()

