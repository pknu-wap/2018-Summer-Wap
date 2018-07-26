from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("http://ce.pknu.ac.kr/05_community/01_community.php")
soup = BeautifulSoup(url,"html.parser")
cnt_artist = 0
cnt_title = 0



for link1 in soup.find_all(name="td",attrs={"class":"txt-l"}):
    cnt_title += 1
    # print(str(cnt_title))
    print(link1.text)



