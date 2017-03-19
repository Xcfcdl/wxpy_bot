# !/usr/bin/env python
# coding:utf-8
# 用来手动开关机器人，可以设置在文件传输
import os


class controler(object):
    """docstring for control do or not do."""

    def __init__(self, set_order, msg_order, log_name):
        # set_order:开关口令
        # msg_order:收到信息 填（msg.text）
        # log_name:储存的名字（msg.sender.nick_name）群的话（msg.member.name（特定用户）或者群名（是啥来着））
        super(controler, self).__init__()
        self.order = set_order
        self.msg_order = str(msg_order)
        self.path = log_name

    def read_log(self):
        path = u".\cache\{}.txt".format(self.path)
        with open(path, 'r', encoding='utf-8') as fe:
            a = fe.read()
        return a

    def open_close(self):
        if "@" in self.msg_order:
            self.msg_order = "{} ".format(self.order)+str(self.msg_order).split(" ")[-1]
        opened = ["{order} 开启".format(order=self.order)]
        closed = ["{order} 关闭".format(order=self.order)]
        if self.msg_order in opened:
            with open(r".\cache\{}.txt".format(self.path), 'w', encoding='utf-8') as f:
                f.write("1")
        elif self.msg_order in closed:
            with open(r".\cache\{}.txt".format(self.path), 'w', encoding='utf-8') as f:
                f.write("0")
        else:
            with open(r".\cache\{}.txt".format(self.path), 'w', encoding='utf-8') as f:
                f.write("0")

    def control_determine(self):

        if os.path.exists(r".\cache\{}.txt".format(self.path)):
            if str(self.msg_order).split(" ")[-1] in ["open", "开", "开启", "close", "关", "关闭"]:
                self.open_close()
                print("机器人状态改变")

        else:
            with open(r".\cache\{}.txt".format(self.path), 'w', encoding='utf-8') as f:
                f.write("0")

        return bool(int(self.read_log()))
