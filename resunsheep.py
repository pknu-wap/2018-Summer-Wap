from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
import pymysql

# conn = pymysql.connect(host='localhost',
#                        user='root',
#                        password='111111',
#                        db='gohwak',
#                        charset='utf8mb4',
#                        cursorclass=pymysql.cursors.DictCursor)

ce = requests.get("http://cms.pknu.ac.kr/pkuocean/view.do?no=1253&pageIndex=1&view=list&sv=TITLE&sw=").text

ce_table = bs(ce,"html.parser")
urls = []

cms = a = ce_table.find(name="ul", attrs={"id": "board_list"})
for link in cms.find_all(name="li"):
    urls.append(link.find('a')['href'])


for url in urls:
    check = 0
    ce_url = requests.get('http://cms.pknu.ac.kr'+ url).text
    ce_contents = bs(ce_url,"html.parser")

    urrl = ('http://cms.pknu.ac.kr'+ url)

    contents = ""
    for link in ce_contents.find_all(name="div", attrs={"id":"board_view"}):

        titlescrap = link.find('h3')
        namedate = link.find_all('strong')

        title = (titlescrap.text)
        date = (namedate[0].text)
        writer = (namedate[1].text)

        # print(date,'     ',title,'     ',writer)

    for link in ce_contents.find_all(name="div", attrs={"class": "board_stance"}):

        if check == 0:
            check = 1
            contents += link.text
        else:
            contents = contents + "\n"+ link.text

    #     print(contents)
    # print('-----------------------------------------------------------------------------------')
#     # try:
#     #     with conn.cursor() as cursor:
#     #         sql = 'INSERT INTO cecroll (title, created, url, content) VALUES ("%s", "%s", "%s", "%s")' %(title, date, urrl, contents)
#     #         cursor.execute(sql)
#     #     conn.commit()
#     # except:
#     #     continue
# conn.close()






