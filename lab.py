from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
import threading
import time

class AsyncTask:
    def __init__(self):
        pass

    def TaskA(self):
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

                print('[', titles[2].text, '] ', '제목  : ', titles[0].text, '\n')

                # date = (titles[2].text)
                # title = (titles[0].text)
            for link in ce_contents.find_all(name="p", attrs={"class": "0"}):
                print(link.text)
                if check == 0:
                    check = 1
                    contents += link.text
                else:
                    contents = contents + "\n" + link.text
                # print(contents)
            print('--------------------------------------------------------------------------------')

        threading.Timer(10,self.TaskA).start()

    def TaskB(self):
        print ('Process B')
        threading.Timer(3, self.TaskB).start()

def main():
    print ('Async Function')
    at = AsyncTask()
    at.TaskA()

if __name__ == '__main__':
    main()


