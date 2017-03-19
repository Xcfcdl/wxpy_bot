# !/usr/bin/en python
# coding:utf-8


import requests
from bs4 import BeautifulSoup as bs
import random


class GetTecentNew():
    def __init__(self):
        self.url = "http://news.qq.com/"
        self.putout = []

    def get_TecentNew(self):
        wbdata = requests.get(self.url).text
        soup = bs(wbdata, "lxml")
        news_title = soup.select("div.text > em.f14 > a.linkto")
        i = 1
        for n in news_title:
            title = n.get_text()
            link = n.get("href")
            data = dict(序号=i, 标题=title, 链接=link)
            # print(i, data)
            i += 1
            self.putout.append(data)

        select = random.randrange(1, len(self.putout))
        put = self.putout[select]["标题"]+"\n详情请看:\n"+self.putout[select]["链接"]
        return put
