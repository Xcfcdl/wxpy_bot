﻿# !/usr/env python
# coding:utf-8

from wxpy import *
import random
from GetTecentNew import GetTecentNew
from duanzi import duanzi
from controler import controler
from at_me import at_me
from netmusic import Get_music
from Tenseijinngo import Tenseijinngo


bot = Bot(cache_path=True)
TuLing = Tuling("0480791e014245bb92174577c11a779f")


@bot.register(User)
def auto_reply(msg):
    if msg.type == 'Attachment' or msg.type == "Picture":
        file_name = msg.file_name
        print("收到文件:" + file_name)
        msg.get_file("./file_rec/{}".format(file_name))
        return '已收到您的文件：{}'.format(file_name)

    if u"查询 功能" in msg.text:
        return "1.图灵聊天\n2.腾讯新闻\n3.来个段子\n4.防撤回（不给你看)\n5.****隐藏****\n6.点歌 [歌名]\n7.天声人语 (文章数)"

    if controler('机器人服务', msg.text, str(msg.sender.name)).control_determine():
        print(msg)
        if msg.type == "Text":
            if u'美女' in msg.text:
                print('''有人要开车！''')
                return "美女？妹子？我有一堆你懂的图哦。要看吗？\n试试输入：我要看妹子"
            elif u'我要看妹子' in msg.text:
                print("用户{}递了一张学生卡".format(msg.sender.nick_name))
                filme = random.randint(1, 1000)
                fileName = r'./beautifulGirls/beautifulGirl ({0}).jpg'.format(str(filme))
                f = bot.friends().search(msg.sender.name)[0]
                f.send("小心营养不足哦[微笑]")
                f.send_image(fileName)
                return "要乖哦[偷笑]"

            elif u"腾讯新闻" in msg.text:
                get_new = GetTecentNew().get_TecentNew()
                print(msg.sender.nick_name + "用户请求了一条新闻:" + get_new)
                return get_new

            elif u'来个段子' in msg.text:
                print(msg.sender.nick_name + "用户请求了一条段子")
                return duanzi().get_duanzi()

            elif u'撤回了一条消息' in msg.text:
                print(msg.sender.nick_name + "撤回了一条消息！")
                return "别以为你撤回我就看不到了！"

            elif u'天声人语' in msg.text:
                a = str(msg.text).replace('天声人语', '').replace(' ', '')
                if len(a) == 0:
                    number = 1
                else:
                    number = int(a)
                essay = str(Tenseijinngo(number).run())
                return essay

            elif u'点歌' in msg.text:
                music_name = str(msg.text).split(" ")[-1]
                print('用户[{}]点了一首歌:'.format(msg.sender.nick_name) + music_name)
                music_ID = Get_music(music_name).get_musicID()
                f1 = bot.friends().search(msg.sender.name)[0]
                if music_ID.isdigit():
                    f1.send("用户点歌：{}\n".format(music_name) + "http://music.163.com/#/song?id={ID}".format(ID=music_ID))
                else:
                    return "对不起，未找到歌曲：{}".format(music_name)

            elif msg.sender.name == "小冰":
                return None

            elif u'发信息' in msg.text:
                if msg.sender.name == "小池蜂":
                    mes = str(msg.text).split(" ")
                    # 格式：发信息 id mes
                    try:
                        fr = bot.friends().search(str(mes[1]))[0]
                        fr.send(msg.sender.name + "给你发送了一条消息：" + str(mes[-1]))
                        print("主人给{toer}发送了一条信息：{messa}".format(
                            toer=str(mes[1]), messa=str(mes[-1])))
                        return "已发送"

                    except:
                        print("主人试图给{toer}发送一条信息【{messa}】未成功！".format(
                            toer=str(mes[1]), messa=str(mes[-1])))
                        return "对不起，操作未成功！请查询昵称和格式是否正确。"

            else:
                Auto_saying = TuLing.reply_text(msg)
                print("{}机器人:".format(msg.sender.nick_name) + Auto_saying)
                return Auto_saying

        elif msg.type == "Recording":
            return "语音什么的听不清啦[流泪]"
        elif msg.type == "Video":
            return "视频什么的我也看不懂。。。[流泪]"
    else:
        print("{}发来信息:".format(msg.sender.nick_name) + msg.text)
        if at_me(msg.sender.name).at_me_time() >= 3:
            print("次数：" + str(at_me(msg.sender.name).at_me_time()) + "次")
            with open(u"./cache/at_me_{}.txt".format(msg.sender.nick_name), 'w', encoding='utf-8') as at_file:
                at_file.write("0")
            return "不要随随便便找我，人家会有反应的。\n如果需要开(关)机器人服务，可以@我，并输入：\n机器人服务 开启(关闭)"
        return None


@bot.register(Group)
def auto_reply(msg):
    print(msg)
    # 如果是群聊，但没有被 @，
    if not (isinstance(msg.sender, Group) and not msg.is_at):
        print("<<<你被人@了>>>")
        if u"查询 功能" in msg.text:
            return "1.图灵聊天\n2.腾讯新闻\n3.来一个段子\n4.防撤回（不给你看)\n5.****隐藏****\n6.点歌 [歌名]"

        if controler('群聊机器人', msg.text, str(msg.member.name)).control_determine():
            print("群聊机器人已经被启动")

            if msg.type == "Text":
                if u'美女' in msg.text:
                    print('''有人要开车！''')
                    return "美女？妹子？我有一堆你懂的图哦。要看吗？\n试试输入：我要看妹子"

                elif u'我要看妹子' in msg.text:
                    print('''有人要开车！''')
                    filme = random.randint(1, 1000)
                    fileName = r'./beautifulGirls/beautifulGirl ({0}).jpg'.format(str(filme))
                    f = bot.friends().search(msg.sender.name)[0]
                    f.send_text("小心营养不足哦[微笑]")
                    f.send_image(fileName)
                    return "要乖哦[微笑]"

                elif u"腾讯新闻" in msg.text:
                    get_new = GetTecentNew().get_TecentNew()
                    print(msg.sender.name + "用户请求了一条新闻:" + get_new)
                    return get_new

                elif u'点歌' in msg.text:
                    music_name = str(msg.text).split(" ")[-1]
                    print('用户[{}]点了一首歌:'.format(msg.sender.nick_name) + music_name)
                    music_ID = Get_music(music_name).get_musicID()
                    f1 = bot.friends().search(msg.sender.name)[0]
                    if music_ID.isdigit():
                        f1.send(
                            "用户点歌：{}\n".format(music_name) + "http://music.163.com/#/song?id={ID}".format(ID=music_ID))
                    else:
                        return "对不起，未找到歌曲：{}".format(music_name)

                elif u'段子' in msg.text:
                    if u'来个段子' in msg.text:
                        print(msg.sender.name + "用户请求了一条段子")
                        return duanzi().get_duanzi()
                    elif u'再来一个段子' in msg.text:
                        print(msg.sender.name + "用户请求了一条段子")
                        return "好，再来一个：" + duanzi().get_duanzi()
                    else:
                        pass

                elif u'撤回了一条消息' in msg.text:
                    print(msg.sender.name + "撤回了一条消息！")
                    host = bot.friends().search(msg.sender.nick_name)[0]
                    host.send(msg.sender.name + "撤回了一条消息！但我还不会记录。。。[哭]")

                else:
                    Auto_saying = TuLing.reply_text(msg)
                    print("{}群聊机器人:".format(msg.sender.nick_name) + Auto_saying)
                    return Auto_saying

        else:
            print("{}发来信息:".format(msg.sender.nick_name) + msg.text)
            if at_me(msg.sender.name).at_me_time() >= 3:
                print("已经被@次数：" + str(at_me(msg.sender.name).at_me_time()) + "次")
                with open(u"./cache/at_me_{}.txt".format(msg.sender.nick_name), 'w', encoding='utf-8') as at_file:
                    at_file.write("0")
                return "不要随随便便找我，人家会有反应的。\n如果需要开(关)机器人服务，可以@我，并输入：\n机器人服务 开启(关闭)"
            return None


@bot.register(msg_types=FRIENDS)
# 自动接受验证信息中包含 '***' 的好友请求
def auto_accept_friends(msg):
    new_friend = bot.accept_friend(msg.card)
    # 或 new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('我自动接受了你的好友请求，你可以向我发消息了')


embed()
