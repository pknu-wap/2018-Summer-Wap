from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests, re

ce = requests.get("http://ce.pknu.ac.kr/05_community/01_community.php").text

soup = BeautifulSoup(ce,"html.parser")
type = []
urls = []
gong = 0


for link1 in soup.find_all(name="td", attrs={"class": "first"}):
    type.append(link1.get_text())

for link1 in soup.find_all(name="td", attrs={"class": "txt-l"}):
    urls.append(link1.find('a')['href'])

for i in range(len(type)):
    if type[i] == '공지':
        gong +=1
del urls[:gong]

print(urls)





# for link1 in soup.find_all(name="td",attrs={"class":"first"}):
#     print(link1.get_text())
#
#
# for link1 in soup.find_all(name="td",attrs={"class":"txt-l"}):
#     print(link1.find('a')['href'])



