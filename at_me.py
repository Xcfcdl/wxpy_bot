# !/usr/env python
# coding:utf-8

import os


class at_me():
    def __init__(self, At_name):

        self.At_name = At_name
        self.path = u"./cache/at_me_{}.txt".format(self.At_name)

    def read_log(self):
        with open(self.path, 'r', encoding='utf-8') as fe:
            a = fe.read()
        return a

    def at_me_time(self):
        if os.path.exists(self.path):
            b = int(self.read_log())
            if b <= 3:
                with open(self.path, 'w', encoding='utf-8') as f:
                    b += 1
                    f.write(str(b))

        else:
            with open(self.path, 'w', encoding='utf-8') as f:
                f.write("0")

        return int(self.read_log())

