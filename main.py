# !/usr/env python
# coding:utf-8

from wxpy import *
import random
from GetTecentNew import GetTecentNew
from duanzi import duanzi
from controler import controler
from at_me import at_me

bot = Bot(cache_path=True)
host = bot.friends().search("小池蜂")[0]
tuling = Tuling(api_key="0480791e014245bb92174577c11a779f")
except_group = bot.groups().search('wxpy 交流群')[0]


@bot.register(User)
def auto_reply(msg):
    if msg.type == 'Attachment' or msg.type == "Picture":
        file_name = msg.file_name
        print("收到文件:" + file_name)
        msg.get_file("./file_rec/{}".format(file_name))
        return '已收到您的文件：{}'.format(file_name)

    if controler('机器人服务', msg.text, str(msg.sender.name)).control_determine():
        print("{}机器人服务正在运行:".format(msg.sender.nick_name))
        if msg.type == "Text":
            if u'美女' in msg.text:
                print('''有人要开车！''')
                return "美女？妹子？我有一堆你懂的图哦。要看吗？\n试试输入：我要看妹子"
            elif u'我要看妹子' in msg.text:
                print("用户{}递了一张学生卡".format(msg.sender.nick_name))
                filme = random.randint(1, 1000)
                fileName = r'.\beautifulGirls\beautifulGirl ({0}).jpg'.format(str(filme))
                f = bot.friends().search(msg.sender.name)[0]
                f.send("小心营养不足哦[微笑]")
                f.send_image(fileName)
                return "要乖哦[偷笑]"

            elif u"腾讯新闻" in msg.text:
                get_new = GetTecentNew().get_TecentNew()
                print(msg.sender.nick_name + "用户请求了一条新闻:" + get_new)
                return get_new

            elif u'段子' in msg.text:
                if u'来个段子' in msg.text:
                    print(msg.sender.nick_name + "用户请求了一条段子")
                    return duanzi().get_duanzi()
                elif u'再来一个段子' in msg.text:
                    print(msg.sender.nick_name + "用户请求了一条段子")
                    return "好，再来一个：" + duanzi().get_duanzi()
                else:
                    pass

            elif u'撤回了一条消息' in msg.text:
                print(msg.sender.nick_name + "撤回了一条消息！")
                host.send(msg.sender.nick_name + "撤回了一条消息！")

            elif msg.sender.name == "小冰":
                return None

            elif msg.sender.name == "小池蜂":
                if u'发信息' in msg.text:
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
                    pass

            else:
                Auto_saying = tuling.reply_text(msg, to_member=True)
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
        print("》》》你被人@了>>")
        if controler('群聊机器人', msg.text, str(msg.member.name)).control_determine():
            print("群聊机器人已经被启动")
            if msg.type == "Text":
                if u'美女' in msg.text:
                    print('''有人要开车！''')
                    return "美女？妹子？我有一堆你懂的图哦。要看吗？\n试试输入：我要看妹子"

                elif u'我要看妹子' in msg.text:
                    print('''群里有人要开车！''')
                    filme = random.randint(1, 1000)
                    fileName = r'.\beautifulGirls\beautifulGirl ({0}).jpg'.format(str(filme))
                    f = bot.friends().search(msg.sender.name)[0]
                    f.send_text("小心营养不足哦[微笑]")
                    f.send_image(fileName)
                    return "要乖哦[微笑]"

                elif u"查询" in msg.text:
                    if u"查询 功能" in msg.text:
                        return "1.图灵聊天\n2.腾讯新闻\n3.来一个段子\n4.防撤回（不给你看)\n5.看妹子图[我要看妹子]--来自煎蛋网的1000张图）"

                elif u"腾讯新闻" in msg.text:
                    get_new = GetTecentNew().get_TecentNew()
                    print(msg.sender.name + "用户请求了一条新闻:" + get_new)
                    return get_new

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
                    host.send(msg.sender.name + "撤回了一条消息！但我还不会记录。。。[哭]")

                else:
                    Auto_saying = tuling.reply_text(msg, to_member=True)
                    print("{}群聊机器人:".format(msg.sender.nick_name) + Auto_saying)
                    return Auto_saying

        else:
            print("{}发来信息:".format(msg.sender.nick_name) + msg.text)
            if at_me(msg.sender.name).at_me_time() >= 3:
                print("次数：" + str(at_me(msg.sender.name).at_me_time()) + "次")
                with open(u"./cache/at_me_{}.txt".format(msg.sender.nick_name), 'w', encoding='utf-8') as at_file:
                    at_file.write("0")
                return "不要随随便便找我，人家会有反应的。\n如果需要开(关)机器人服务，可以@我，并输入：\n机器人服务 开启(关闭)"
            return None


@bot.register(except_group)
def ignore():
    # 啥也不做
    return


bot.start()
