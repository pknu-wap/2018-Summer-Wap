from bs4 import BeautifulSoup as bs
import requests
import pymysql
import json



while 1:
    try:
        user = input('MYSQL user 이름을 입력하세요 : ')
        ps = input('MYSQL 비밀번호를 입력하세요 : ')
        infolist = ['user','company']
        conn = pymysql.connect(host='localhost',
                                          user=user,
                                          password=ps,
                                          db='gohwak',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        break

    except pymysql.err.OperationalError:
        print("user이름과 password를 확인하세요")

def before_update():
    curs = conn.cursor()
    sql = "select * from cecroll"
    curs.execute(sql)
    rows = curs.fetchall()
    before_update = rows[-1]
    bef_json = json.dumps(before_update, indent=2, ensure_ascii=False)
    bef_url = json.loads(bef_json).get('url')

    return bef_url

def update_data():

    ce = requests.get("http://ce.pknu.ac.kr/05_community/01_community.php").text
    ce_table = bs(ce, "html.parser")
    urls = []

    for link in ce_table.find_all(name="td", attrs={"class": "txt-l"}):
        urls.append(link.find('a')['href'])

    for url in urls:
        check = 0
        ce_url = requests.get('http://ce.pknu.ac.kr' + url).text
        ce_contents = bs(ce_url, "html.parser")
        urrl = ('http://ce.pknu.ac.kr' + url)
        contents = ""

        for link in ce_contents.find_all(name="tr", attrs={"class": "head"}):
            titles = link.find_all('td')
            date = (titles[2].text)
            title = (titles[0].text)

        for link in ce_contents.find_all(name="p", attrs={"class": "0"}):
            # print(link.text)
            if check == 0:
                check = 1
                contents += link.text
            else:
                contents = contents + "\n" + link.text

        try:
            with conn.cursor() as cursor:
                sql = 'INSERT INTO cecroll (title, created, url, content) VALUES ("%s", "%s", "%s", "%s")' % (
                title, date, urrl, contents)
                cursor.execute(sql)
            conn.commit()
        except:
            continue



def after_update():

    curs = conn.cursor()
    sql = "select * from cecroll"
    curs.execute(sql)
    rows = curs.fetchall()
    after_update = rows[-1]
    aft_json = json.dumps(after_update, indent=2, ensure_ascii=False)
    aft_url = json.loads(aft_json).get('url')

    return aft_url



def compare(bef_url,aft_url):

    if bef_url == aft_url:
        return '새로 추가된 내용이 없다링...\n' +'('+ bef_url+')'
    else:
        return '공지사항이 추가되었다링 :).\n' +'('+ aft_url+')'



if __name__ == '__main__':
    conn.close()