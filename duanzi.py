# !/usr/env python
# coding:utf-8
from bs4 import BeautifulSoup as bs
import requests
import random


class duanzi():
    def __init__(self):
        self.n = random.randint(1, 200)

    def get_duanzi(self):
        url = 'http://www.qiushibaike.com/text/page/' + str(self.n) + '/'

        # url = 'http://www.qiushibaike.com/8hr/page/'+str(n)+'/'

        heads = {

            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Referer': 'http://www.qiushibaike.com/',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cookie': '_xsrf=2|db27040e|6b4ed8d9536590d4ec5d2064cc2bef4f|1474364551; _qqq_uuid_="2|1:0|10:1474364551|10:_qqq_uuid_|56:MzBlNWFkOGE3MWEyMzc1MWIxMTE3MDBlZjM2M2RkZWQxYzU5YTg1Yw==|1dd2a4f4ceacad26b5da9cc295d2965226ea25ee73289855cf032629c4992698"; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1474364592; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1474364595; _ga=GA1.2.1125329542.1474364596'

        }

        res = requests.get(url, headers=heads).text

        soup = bs(res, "lxml")

        fuckDuanzi = []

        someData = soup.select("div.content span")

        num = 0

        for some in someData:
            num += 1

            fuckDuanzi.append(some.text)

        mess = fuckDuanzi[random.randint(1, 19)]

        return mess
