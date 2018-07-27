from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests

ce = requests.get("http://ce.pknu.ac.kr/05_community/01_community.php").text

ce_table = bs(ce,"html.parser")
type = []
urls = []
gong = 0


for link in ce_table.find_all(name="td", attrs={"class": "first"}):
    type.append(link.get_text())

for link in ce_table.find_all(name="td", attrs={"class": "txt-l"}):
    urls.append(link.find('a')['href'])

for i in range(len(type)):
    if type[i] == '공지':
        gong +=1
del urls[:gong]


for url in urls:
    ce_url = requests.get('http://ce.pknu.ac.kr'+ url).text
    ce_contents = bs(ce_url,"html.parser")

    for link in ce_contents.find_all(name="tr"):
        print(link.get_text())







