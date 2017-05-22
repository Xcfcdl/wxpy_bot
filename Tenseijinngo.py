import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import time


def getItems(url):
    try:
        reg = requests.get(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        wbd = BeautifulSoup(reg.text, 'lxml')
        datas = wbd.select('.tweet')
    except AttributeError as e:
        print(e)
        return None
    return datas


def getLink(items):
    links = []
    if items is not None:
        for item in items:
            # title = item.select('p')
            # time = item.select('.ago')[0]['title']
            link = 'https://twishort.com' + item.select('.ago')[0]['href']
            links.append(link)

    else:
        print('获取不到链接列表')
        links = None
    return links


def get_essay(links, num):
    essayList = []
    if links is not None:
        print('现有链接数：' + str(len(links)))
        print('请求中')
        while num > 0:
            try:
                reg = requests.get(links[num - 1])
                num = num - 1
            except HTTPError as e:
                print(e)
                return None
            try:
                wbd = BeautifulSoup(reg.text, 'lxml')
                page = wbd.select('#onetweet')
                essay = page[0].select('p')[0].text.strip().replace('\n\n\u3000', '').replace('\n\r\n\u3000', '')
                essayList.append(essay)
                print('获取成功')
                time.sleep(2)
            except AttributeError as e:
                print(e)
                return None
    else:
        print('链接数为空！')
    return essayList


class Tenseijinngo:
    def __init__(self, number):
        self.cont = int(number)

    def run(self):
        global essays
        if self.cont <= 10:
            url = "https://twishort.com/user/ayrton27?offset=0"
            items = getItems(url)
            linkList = getLink(items)
            essays = get_essay(linkList, self.cont)
        elif self.cont > 10:
            for p in range(self.cont // 10):
                if p < self.cont // 10:
                    url = "https://twishort.com/user/ayrton27?offset={}".format(p)
                    items = getItems(url)
                    linkList = getLink(items)
                    essays = get_essay(linkList, 10)
                else:
                    url = "https://twishort.com/user/ayrton27?offset={}".format(self.cont // 10)
                    items = getItems(url)
                    linkList = getLink(items)
                    essays = get_essay(linkList, self.cont % 10)
        else:
            print('输入有误，请重新输入')
        return essays

