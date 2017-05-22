# !/usr/env python
# coding:utf-8

import requests
from bs4 import BeautifulSoup


class Get_music():
    def __init__(self, name):
        self.name = name
        self.url = 'http://music.163.com/api/search/get'
        self.header = {'Referer': 'http://music.163.com/',
                       'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
                       'Host': 'music.163.com',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
                       }
        self.data = dict(s=self.name, type='1', offset='0', total='true', limit='1')

    def get_musicID(self):
        music_id = requests.post(self.url, data=self.data).text
        a = music_id.split(":")[3].split(",")[0]
        # print(a)
        return a


