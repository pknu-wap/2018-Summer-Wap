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

    for link in ce_contents.find_all(name="tr", attrs={"class":"head"}):
        titles = link.find_all('td')
        print('[',titles[2].text,'] ','제목  : ',titles[0].text,'\n')
    for link in ce_contents.find_all(name="p", attrs={"class": "0"}):
        print(link.text)
    print('---------------------------------------------------------------------------------')


# ce_url = requests.get('http://ce.pknu.ac.kr'+'/05_community/01_community.php?bid=c_notice&page=0&sv=title&sw=&tgt=view&idx=3657').text
# ce_contents = bs(ce_url,"html.parser")
# for link in ce_contents.find_all(name="tr",attrs="head"):
#     print(link.text)
# for link in ce_contents.find_all(name="p",attrs = {"class" : "0"}):
#     print(link.text)






