from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='111111',
                       db='gohwak',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

ce = requests.get("http://ce.pknu.ac.kr/05_community/01_community.php").text

ce_table = bs(ce,"html.parser")
urls = []


for link in ce_table.find_all(name="td", attrs={"class": "txt-l"}):
    urls.append(link.find('a')['href'])



for url in urls:
    check = 0
    ce_url = requests.get('http://ce.pknu.ac.kr'+ url).text
    ce_contents = bs(ce_url,"html.parser")
    urrl = ('http://ce.pknu.ac.kr'+ url)
    contents = ""
    for link in ce_contents.find_all(name="tr", attrs={"class":"head"}):
        titles = link.find_all('td')
        date = (titles[2].text)
        title = (titles[0].text)
    for link in ce_contents.find_all(name="p", attrs={"class": "0"}):
        print(link.text)
        if check == 0:
            check = 1
            contents += link.text
        else:
            contents = contents + "\n"+ link.text

    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO cecroll (title, created, url, content) VALUES ("%s", "%s", "%s", "%s")' %(title, date, urrl, contents)
            cursor.execute(sql)
        conn.commit()
    except:
        continue
conn.close()