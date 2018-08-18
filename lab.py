from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
import threading
import time
ce = requests.get("http://ce.pknu.ac.kr/05_community/01_community.php").text
cms = requests.get("http://cms.pknu.ac.kr/pkuocean/view.do?no=1253&pageIndex=1&view=list&sv=TITLE&sw=").text

ce_table = bs(ce, "html.parser")
cms_table = bs(cms,"html.parser")

urls = []
urls2 = []

class Gohwak:
    def __init__(self):
        pass

    def Ce(self):

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

                print('[', titles[2].text, '] ', '제목  : ', titles[0].text, '\n')

                # date = (titles[2].text)
                # title = (titles[0].text)
            for link in ce_contents.find_all(name="p", attrs={"class": "0"}):
                # print(link.text)
                if check == 0:
                    check = 1
                    contents += link.text
                else:
                    contents = contents + "\n" + link.text
                # print(contents)
            print('--------------------------------------------------------------------------------')

        threading.Timer(20,self.Ce).start()
    def Cms(self):
        cms = a = cms_table.find(name="ul", attrs={"id": "board_list"})
        for link in cms.find_all(name="li"):
            urls2.append(link.find('a')['href'])

        for url in urls2:
            check = 0
            cms_url = requests.get('http://cms.pknu.ac.kr' + url).text
            cms_contents = bs(cms_url, "html.parser")

            urrl = ('http://cms.pknu.ac.kr' + url)

            contents = ""
            for link in cms_contents.find_all(name="div", attrs={"id": "board_view"}):
                titlescrap = link.find('h3')
                namedate = link.find_all('strong')

                title = (titlescrap.text)
                date = (namedate[0].text)
                writer = (namedate[1].text)

                print(date,'     ',title,'     ',writer)

            for link in cms_contents.find_all(name="div", attrs={"class": "board_stance"}):
                # print(link.text)
                if check == 0:
                    check = 1
                    contents += link.text
                else:
                    contents = contents + "\n" + link.text

            #     print(contents)
            print('-----------------------------------------------------------------------------------')

            threading.Timer(10, self.Cms).start()

    def Check(self):
        print ('Update fin')
        threading.Timer(20, self.Check).start()

def main():
    print ('Go Hwak')
    gh = Gohwak()
    gh.Ce()
    gh.Cms()
    gh.Check()

if __name__ == '__main__':
    main()


