# -*- coding: UTF-8 -*-
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
import time
import random
import os
from pynput import mouse
from pynput import keyboard
import pygame
from pypinyin import lazy_pinyin
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=256)
pygame.mixer.music.load(r'.\600.wav')
biao = 'abcdefghijklmnopqrstuvwxyz0123456789?/()-.'
mimabiao = {'a': '*-', 'b': '-***', 'c': '-*-*', 'd': '-**', 'e': '*', 'f': '**-*', 'g': '--*', 'h': '****', 'i': '**',
            'j': '*---', 'k': '-*-', 'l': '*-**', 'm': '--', 'n': '-*', 'o': '---', 'p': '*--*', 'q': '--*-',
            'r': '*-*', 's': '***', 't': '-', 'u': '**-', 'v': '***-', 'w': '*--', 'x': '-**-', 'y': '-*--',
            'z': '--**', '1': '*----', '2': '**---', '3': '***--', '4': '****-', '5': '*****', '6': '-****',
            '7': '--***', '8': '---**', '9': '----*', '0': '-----', '?': '**--**', '/': '-**-*', '(': '-*--*-',
            ')': '-*--*-', '-': '-****-', '.': '*-*-*-'}
fanmimabiao = {'*-': 'a', '-***': 'b', '-*-*': 'c', '-**': 'd', '*': 'e', '**-*': 'f', '--*': 'g', '****': 'h',
               '**': 'i', '*---': 'j', '-*-': 'k', '*-**': 'l', '--': 'm', '-*': 'n', '---': 'o', '*--*': 'p',
               '--*-': 'q', '*-*': 'r', '***': 's', '-': 't', '**-': 'u', '***-': 'v', '*--': 'w', '-**-': 'x',
               '-*--': 'y', '--**': 'z', '*----': '1', '**---': '2', '***--': '3', '****-': '4', '*****': '5',
               '-****': '6', '--***': '7', '---**': '8', '----*': '9', '-----': '0', '**--**': '?', '-**-*': '/',
               '-****-': '-', '*-*-*-': '.'}
baochun = []
scale = 50
def shijianHuanSuan(time):
    if time < 60:
        time = '{:.0f}秒'.format(time)
    elif time < 3600:
        time = '{:.0f}分 {:.0f}秒'.format(time // 60, time % 60)
    elif time < 86400:
        time = '{:.0f}时 {:.0f}分 {:.0f}秒'.format(time // 3600, (time % 3600) // 60, (time % 3600) % 60)
    else:
        time = '{:.0f}天 {:.0f}时 {:.0f}分 {:.0f}秒'.format(time // 86400, (time % 86400) // 3600, ((time % 86400) % 3600) // 60,
                                        (((time % 86400) % 3600) % 60))
    return time

def jiesao():
    global mima, mogenmima
    if xuanze2 == '1':
        if geshu <= 0:
            mima = '你已经没有密文可以破译 !!!'
            mogenmima = '你已经没有密文可以破译 !!!'
        if xuanze3 == '1':
            print('密码===||  ' + mogenmima + '   ||')
        else:
            print('密码===||  ' + mima + '   ||')
        print('=====-----|NvN|计 时 开 始|NvN|-----=====')
        # print('【注意空格】例如： | ee == * *(一个空格) |\t| e e == *  *(两个空格) |')
        if fabaoqi == '1':
            print('【左键】输入 【上滚】退出 【中键】半自动间距 【右键】清除 【鼠标移动到左上角】暂停')
        else:
            print('设置完毕，当前发报器模式【键盘】，按键表')
            for i in fabaojian:
                if i == '保存':
                    continue
                print('【' + i + '|' + fabaojian[i] + '】', end=' ')
            print()
        print('如果打错了，可以使用  ******（即6个*） 来删除最近的一个错误')
    else:
        print('介绍：')
        print('【注意空格】例如： | ee == * *(一个空格) |\t| e e == *  *(两个空格) |')
        if fabaoqi == '1':
            print('【左键】输入 【上滚】退出 【下滚】保存 【中键】半自动间距 【右键】清除 【鼠标移动到左上角】暂停')
        else:
            print('设置完毕，当前发报器模式【键盘】，按键表')
            for i in fabaojian:
                print('【' + i + '|' + fabaojian[i] + '】', end=' ')
            print()
        print('如果打错了，可以使用  ******（即6个*） 来删除最近的一个错误')
        print('自由发报区')
        print('=' * 50)


def jingdutiao(a=0.01, b='>'):
    print("开始加载".center(scale // 2, "-"))
    start = time.perf_counter()
    for i in range(scale + 1):
        r = b * i
        y = ' ' * (scale - i)
        p = (i / scale) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}{}]{:.2f}s".format(p, r, y, dur), end="")
        time.sleep(a)
    print("\n" + "加载完毕".center(scale // 2, '-'))


def on_move(x, y):
    global zantin
    if x < 5 and y < 5:
        zantin = False
        return False


def on_scroll(x, y, dx, dy):
    global qiaochulai, kai
    try:
        if dy > 0:
            if xuanze2 == '1':
                kai = False
            return False
        else:
            if xuanze2 == '2' and qiaochulai.strip() != '' and qiaochulai.strip() not in baochun:
                baochun.append('#')
                baochun.append(qiaochulai.strip())
                baochun.append(jieshi.strip())
                print(' {}保存成功 !!!{}'.format('<=>' * 6, '<=>' * 6))
                print('  {}不必担心，我不会保存一样的东西 !!!{}'.format('<=>' * 2, '<=>' * 2))
    except:
        pass
def fabaoqiXuanZe():
    global fabaojian
    print('你希望使用什么模拟发报器：【1】鼠标   【2】键盘')
    while 1:
        fabaoqi = input('请选择:')
        if fabaoqi == '1':
            pass
        elif fabaoqi == '2':
            print('检测到你选中了键盘，下面进行按键设置 ? 请你按下它')
            for i in fabaojian:
                print('请决定>'+i+'<键:')
                with keyboard.Listener(on_press=anjianXuanZe) as jianpanlistener:
                    jianpanlistener.join()
                fabaojianMa[i] = jutiAnJian
                fabaojian[i] = jutiAnJian
                test = input('按键垃圾回收器【请回车】')
                if fabaojian[i][:4] != 'Key.' and test[:1] in ['1','2','3','4','5','6','7','8','9','0','.']:
                    fabaojian[i] = test[:1]
                if fabaojian[i][0] == "'" and fabaojian[i][2] == "'":
                    fabaojian[i] = fabaojian[i][1:2]
        else:
            print('请二选一')
            continue
        return fabaoqi
def anjianXuanZe(key):
    global jutiAnJian
    jutiAnJian = str(key)
    return False
def jianpan_on_press(key):
    global atime, btime, qiaochulai, jieshi, xuanze7,danCiXianZhi
    try:
        # if key == keyboard.Key.enter:
        #     print('enter按')
        # elif key.char == 'v':
        #     print('v按')
        if danCiXianZhi:    #切记，如果这个函数里，弄了两个及以上键的时候就不能用这个了
            raise Exception
        try:
            if xuanze7 == '1':
                pygame.mixer.music.load(r'.\600.wav')
                pygame.mixer.music.stop()
                xuanze7 = 0
        except:
            pass
        if fabaojianMa['输入'] == str(key):
            danCiXianZhi = True
            pygame.mixer.music.play(-1)
            atime = time.perf_counter()
            if time.perf_counter() - btime > 0.3:
                qiaochulai += ' '
            if xuanze2 == '2' or xuanze3 == '1' and xuanze8 == '3' or xuanze3 == '4':
                if time.perf_counter() - btime > 0.7:
                    qiaochulai += ' '
    except:
        pass
def jianpan_on_release(key):
    global atime, btime, qiaochulai, jieshi, xuanze7,qiaochulai, kai,zantin,danCiXianZhi
    try:
        # if key == keyboard.Key.esc:
        #     return False
        # elif key.char == "c":
        #     print('c放')
        if xuanze2 == '1' and time.perf_counter() - timea - bushijian > shijian:
            return False
        if fabaojianMa['输入'] == str(key):
            danCiXianZhi = False
            pygame.mixer.music.stop()
            btime = time.perf_counter()
            if time.perf_counter() - atime <= 0.1:
                qiaochulai += '*'
            else:
                qiaochulai += '-'
            if qiaochulai.strip()[-6:] == '******':
                sanchu = 0
                for w in qiaochulai.split(' ')[::-1]:
                    if w == '':
                        sanchu += 1
                    elif w == '******':
                        sanchu += 6
                    else:
                        sanchu += len(w) + 1
                        break
                qiaochulai = qiaochulai[:len(qiaochulai) - sanchu].strip()
            if xuanze2 == '1':
                os.system('cls')
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),
                                        (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
                jiesao()
                print('=' * 50)
                print('\r你的报文=>|' + qiaochulai)
                print('=' * 50)
                daojishi = int(shijian - ((time.perf_counter() - timea) - bushijian))
                if daojishi < 60:
                    print('你有总共 {:.0f} 秒 !!!'.format(shijian))
                    print('还剩 {:.0f} 秒 !!!'.format(daojishi))
                elif daojishi < 3600:
                    print('你有总共 {:.0f}分 {:.0f}秒 !!!'.format(shijian // 60, shijian % 60))
                    print('还剩 {:.0f}分 {:.0f}秒 !!!'.format(daojishi // 60, daojishi % 60))
                elif daojishi < 86400:
                    print('你有总共 {:.0f}时 {:.0f}分 {:.0f}秒 !!!'.format(shijian // 3600, (shijian % 3600) // 60,
                                                        (shijian % 3600) % 60))
                    print('还剩 {:.0f}时 {:.0f}分 {:.0f}秒 !!!'.format(daojishi // 3600, (daojishi % 3600) // 60,
                                                      (daojishi % 3600) % 60))
                else:
                    print('你有总共 {:.0f}天 {:.0f}时 {:.0f}分 {:.0f}秒 !!!'.format(shijian // 86400, (shijian % 86400) // 3600,
                                                            ((shijian % 86400) % 3600) // 60,
                                                            (((shijian % 86400) % 3600) % 60)))
                    print('还剩 {:.0f}天 {:.0f}时 {:.0f}分 {:.0f}秒 !!!'.format(daojishi // 86400, (daojishi % 86400) // 3600,
                                                          ((daojishi % 86400) % 3600) // 60,
                                                          (((daojishi % 86400) % 3600) % 60)))
                print('-' * 15)
                if qiaochulai.strip() == mogenmima.strip():
                    return False
            else:
                jieshi = ''
                if qiaochulai.strip() != '':
                    zanshi = qiaochulai.strip().split(' ')
                    for q in range(len(zanshi)):
                        if zanshi[q] == '':
                            if zanshi[q + 1] == '':
                                continue
                            jieshi += ' '
                        else:
                            try:
                                jieshi += fanmimabiao[zanshi[q]]
                            except:
                                if zanshi[q] == '-*--*-':
                                    if '(' not in jieshi:
                                        jieshi += '('
                                    elif ')' not in jieshi:
                                        jieshi += ')'
                                    elif len(jieshi.split('(')) > len(jieshi.split(')')):
                                        jieshi += ')'
                                    elif len(jieshi.split('(')) == len(jieshi.split(')')):
                                        jieshi += '('
                                elif zanshi[q] == '******':
                                    jieshi = jieshi.strip()[:-1]
                os.system('cls')
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),
                                        (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
                jiesao()
                print('\r你的报文=>|' + qiaochulai)
                print('=' * 50)
                print('解释》' + jieshi)
                print('-' * 50)
        elif fabaojianMa['暂停'] == str(key):
            zantin = False
            return False
        elif fabaojianMa['保存'] == str(key):
            if xuanze2 == '2' and qiaochulai.strip() != '' and qiaochulai.strip() not in baochun:
                baochun.append('#')
                baochun.append(qiaochulai.strip())
                baochun.append(jieshi.strip())
                print(' {}保存成功 !!!{}'.format('<=>' * 6, '<=>' * 6))
                print('  {}不必担心，我不会保存一样的东西 !!!{}'.format('<=>' * 2, '<=>' * 2))
        elif fabaojianMa['退出'] == str(key):
            if xuanze2 == '1':
                kai = False
            return False
        elif fabaojianMa['清空'] == str(key):
            qiaochulai = ''
            jieshi = ''
            os.system('cls')
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),
                                    (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
            jiesao()
        elif fabaojianMa['半自动间距'] == str(key):
            qiaochulai += ' '
    except:
        pass
def on_click(x, y, button, pressed):
    global atime, btime, qiaochulai, jieshi, xuanze7
    try:
        if pressed:
            try:
                if xuanze7 == '1':
                    pygame.mixer.music.load(r'.\600.wav')
                    pygame.mixer.music.stop()
                    xuanze7 = 0
            except:
                pass
            if button == button.left:
                pygame.mixer.music.play(-1)
                atime = time.perf_counter()
                if time.perf_counter() - btime > 0.3:
                    qiaochulai += ' '
                if xuanze2 == '2' or xuanze3 == '1' and xuanze8 == '3' or xuanze3 == '4':
                    if time.perf_counter() - btime > 0.7:
                        qiaochulai += ' '
        else:
            if xuanze2 == '1' and time.perf_counter() - timea - bushijian > shijian:
                return False
            elif button == button.left:
                pygame.mixer.music.stop()
                btime = time.perf_counter()
                if time.perf_counter() - atime <= 0.1:
                    qiaochulai += '*'
                else:
                    qiaochulai += '-'
                if qiaochulai.strip()[-6:] == '******':
                    sanchu = 0
                    for w in qiaochulai.split(' ')[::-1]:
                        if w == '':
                            sanchu += 1
                        elif w == '******':
                            sanchu += 6
                        else:
                            sanchu += len(w) + 1
                            break
                    qiaochulai = qiaochulai[:len(qiaochulai) - sanchu].strip()
                if xuanze2 == '1':
                    os.system('cls')
                    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),
                                            (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
                    jiesao()
                    print('=' * 50)
                    print('\r你的报文=>|' + qiaochulai)
                    print('=' * 50)
                    daojishi = int(shijian - ((time.perf_counter() - timea) - bushijian))
                    if daojishi < 60:
                        print('你有总共 {:.0f} 秒 !!!'.format(shijian))
                        print('还剩 {:.0f} 秒 !!!'.format(daojishi))
                    elif daojishi < 3600:
                        print('你有总共 {:.0f}分 {:.0f}秒 !!!'.format(shijian // 60, shijian % 60))
                        print('还剩 {:.0f}分 {:.0f}秒 !!!'.format(daojishi // 60, daojishi % 60))
                    elif daojishi < 86400:
                        print('你有总共 {:.0f}时 {:.0f}分 {:.0f}秒 !!!'.format(shijian // 3600, (shijian % 3600) // 60,
                                                            (shijian % 3600) % 60))
                        print('还剩 {:.0f}时 {:.0f}分 {:.0f}秒 !!!'.format(daojishi // 3600, (daojishi % 3600) // 60,
                                                          (daojishi % 3600) % 60))
                    else:
                        print('你有总共 {:.0f}天 {:.0f}时 {:.0f}分 {:.0f}秒 !!!'.format(shijian // 86400, (shijian % 86400) // 3600,
                                                                ((shijian % 86400) % 3600) // 60,
                                                                (((shijian % 86400) % 3600) % 60)))
                        print('还剩 {:.0f}天 {:.0f}时 {:.0f}分 {:.0f}秒 !!!'.format(daojishi // 86400, (daojishi % 86400) // 3600,
                                                              ((daojishi % 86400) % 3600) // 60,
                                                              (((daojishi % 86400) % 3600) % 60)))
                    print('-' * 15)
                    if qiaochulai.strip() == mogenmima.strip():
                        return False
                else:
                    jieshi = ''
                    if qiaochulai.strip() != '':
                        zanshi = qiaochulai.strip().split(' ')
                        for q in range(len(zanshi)):
                            if zanshi[q] == '':
                                if zanshi[q + 1] == '':
                                    continue
                                jieshi += ' '
                            else:
                                try:
                                    jieshi += fanmimabiao[zanshi[q]]
                                except:
                                    if zanshi[q] == '-*--*-':
                                        if '(' not in jieshi:
                                            jieshi += '('
                                        elif ')' not in jieshi:
                                            jieshi += ')'
                                        elif len(jieshi.split('(')) > len(jieshi.split(')')):
                                            jieshi += ')'
                                        elif len(jieshi.split('(')) == len(jieshi.split(')')):
                                            jieshi += '('
                                    elif zanshi[q] == '******':
                                        jieshi = jieshi.strip()[:-1]
                    os.system('cls')
                    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),
                                            (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
                    jiesao()
                    print('\r你的报文=>|' + qiaochulai)
                    print('=' * 50)
                    print('解释》' + jieshi)
                    print('-' * 50)
            elif button == button.middle:
                qiaochulai += ' '
            elif button == button.right:
                qiaochulai = ''
                jieshi = ''
                os.system('cls')
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),
                                        (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
                jiesao()
    except:
        pass


def qianxi():
    global timea, bianmaqian, qiaochulai, mima, mogenmima, bushijian
    mima = ''
    mogenmima = ''
    for i in range(geshu):
        a = random.randint(0, 41)
        mima += biao[a:a + 1]
        mogenmima += mimabiao[biao[a:a + 1]] + ' '
        if xuanze3 != '2':
            if xuanze3 == '1':
                if xuanze8 != '1':
                    if random.randint(0, 5) == 3:
                        mima += ' '
                        mogenmima += ' '
            elif random.randint(0, 5) == 3:
                mima += ' '
                mogenmima += ' '
    print()
    jiesao()
    timea = time.perf_counter()
    print()
    qiaochulai = ''
    while 1:
        if fabaoqi == '1':
            with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
                listener.join()
        else:
            with keyboard.Listener(on_press=jianpan_on_press, on_release=jianpan_on_release) as jianpanlistener:
                jianpanlistener.join()
        pygame.mixer.music.stop()
        if kai == False:
            bushijian = 0
            return
        if time.perf_counter() - timea - bushijian > shijian:
            bushijian = 0
            tongJi['超时'] += 1
            return 1
        elif qiaochulai.strip() == mogenmima.strip():
            bushijian = 0
            print()
            print('正确的钥匙 ！！！ 发送成功 ！！！')
            tongJi['正确'] += 1
            break
        else:
            tongJi['暂停'] += 1
            print()
            timeb = time.perf_counter()
            print('已经为你暂停发报 ！！！')
            print('已经开启快速编辑模式，你可以自由复制些什么 !!!')
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x40 | 0x100))
            os.system('pause')
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
            bushijian += time.perf_counter() - timeb
            print('已关闭快速编辑模式 !!!')
            print('>===继续发报===<')
            tongJi['暂停时间'] += time.perf_counter() - timeb


def ashichang(xuanze, kaiguan=True):
    print()
    print('PS: 你不需要在意 24小时 和 60分钟 和 60秒 的规则')
    print('    直接回车代表输入 0')
    print('如果你直接回车，默认时间为 一分钟')
    if kaiguan:
        if xuanze == '1':
            print('你需要多长时间解决一道 ？？？')
            print('接下来你需要分别输入 小时|分钟|秒')
        elif xuanze == '2':
            liebiao = []
            print('你需要输入 两轮   小时|分钟|秒')
            print('一轮为 随机时长的 最小值，一轮为 随机时长的 最大值')
            print('如果两轮输入的值一样大，相当于 固定时长')
            print('大小不分先后顺序\n')
            print('|<=>第一轮<=>|\n')
        else:
            liebiao = []
            print('你需要输入先输入 小时|分钟|秒 再输入 公差（即递增/递减的值）')
            print('公差为  零  则不变')
        print('=' * 12)
    while 1:
        shichang = 0
        for i in ['小时', '分钟', '秒']:
            if i == '小时':
                zanshi = 3600
            elif i == '分钟':
                zanshi = 60
            else:
                zanshi = 1
            while 1:
                xuanze = input('请决定(' + i + '): ')
                if set(xuanze) <= {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                    if xuanze != '':
                        shichang += int(xuanze) * zanshi
                    print('=' * 12)
                    break
                else:
                    print('抱歉，我无法识别你想要多久……AvA')
        if shichang == 0:
            shichang = 60
            print('你选择了默认 一分钟 !!!')
        if kaiguan:
            if xuanze4 == '1':
                break
            elif xuanze4 == '2' or xuanze4 == '3' or xuanze4 == '4':
                liebiao.append(shichang)
                if len(liebiao) == 1:
                    print()
                    if xuanze4 == '2':
                        print('|<=>第二轮<=>|\n')
                    else:
                        print('|<=>现在决定 公差<=>|\n')
                elif len(liebiao) == 2:
                    if xuanze4 == '2':
                        shichang = [min(liebiao), max(liebiao)]
                    elif xuanze4 == '3':
                        shichang = [liebiao[0] - liebiao[1], liebiao[1]]
                    else:
                        shichang = [liebiao[0] + liebiao[1], -liebiao[1]]
                    break
        else:
            break
    return shichang


def achangdu():
    print()
    print('你希望起始的密文长度是多少 ？？？')
    print('如果你直接回车，默认长度为20')
    if xuanze5 == '2':
        liebiao = []
        print('你需要先后输入两个密文长度')
        print('一个为密文长度的最小值，一个为密文长度的最大值')
        print('如果两次输入的值一样大，相当于 固定长度')
        print('大小不分先后顺序\n')
        print('|<=>第一个<=>|\n')
    elif xuanze5 == '3' or xuanze5 == '4':
        liebiao = []
        print('你需要输入先输入 初始密文长度 再输入 公差（即递增/递减的值）')
        print('公差为  零  则不变')
    while 1:
        changdu = 20
        zanshi = input('请决定: ')
        if set(zanshi) <= {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            if zanshi == '':
                print('你选择了默认 20 个长度 !!!')
            elif zanshi != '':
                changdu = int(zanshi)
            if xuanze5 == '1':
                break
            elif xuanze5 == '2' or xuanze5 == '3' or xuanze5 == '4':
                liebiao.append(changdu)
                if len(liebiao) == 1:
                    print()
                    if xuanze5 == '2':
                        print('|<=>第二个<=>|\n')
                    else:
                        print('|<=>现在决定 公差<=>|\n')
                elif len(liebiao) == 2:
                    if xuanze5 == '2':
                        changdu = [min(liebiao), max(liebiao)]
                    elif xuanze5 == '3':
                        changdu = [liebiao[0] - liebiao[1], liebiao[1]]
                    else:
                        changdu = [liebiao[0] + liebiao[1], -liebiao[1]]
                    break
        else:
            print('我无法识别你要多长……呀嘞呀嘞')
    return changdu


def chongdie(q):
    global shuchu
    for w in range(len(q)):
        if q[w] == ' ' or w != 0 and q[w] == '*' and (q[w - 1] == '*' or q[w - 1] == '-') or w != 0 and q[
            w] == '-' and (q[w - 1] == '*' or q[w - 1] == '-'):
            continue
        zanshi = q[w]
        if q[w] == '*' or q[w] == '-':
            z = w
            while 1:
                z += 1
                try:
                    if q[z] != '*' and q[z] != '-':
                        zanshi = q[w:z]
                        break
                except:
                    zanshi = q[w:z]
                    break
        try:
            if zanshi == '-':
                raise 0
            shuchu += mimabiao[zanshi]
            shuchu += ' '
        except:
            try:
                if w != 0:
                    shuchu = shuchu.strip()
                if zanshi == '-*--*-':
                    if '(' not in shuchu:
                        shuchu += '('
                    elif ')' not in shuchu:
                        shuchu += ')'
                    elif len(shuchu.split('(')) > len(shuchu.split(')')):
                        shuchu += ')'
                    elif len(shuchu.split('(')) == len(shuchu.split(')')):
                        shuchu += '('
                    continue
                shuchu += fanmimabiao[zanshi]
            except:
                shuchu += '×'


def qiedangao(w):
    global shuchu
    for i in zuanhuanwenben:
        if i == '':
            continue
        zanshi = i.strip().split(w)
        for q in zanshi:
            q = q.strip()
            if q == ' ':
                continue
            try:
                if q == '-':
                    raise 0
                shuchu += mimabiao[q]
                shuchu += ' '
            except:
                try:
                    if zanshi.index(q) != 0:
                        shuchu = shuchu.strip()
                    if q == '-*--*-':
                        if '(' not in shuchu:
                            shuchu += '('
                        elif ')' not in shuchu:
                            shuchu += ')'
                        elif len(shuchu.split('(')) > len(shuchu.split(')')):
                            shuchu += ')'
                        elif len(shuchu.split('(')) == len(shuchu.split(')')):
                            shuchu += '('
                        continue
                    shuchu += fanmimabiao[q]
                except:
                    chongdie(q)
        shuchu += ' '


if __name__ == "__main__":
    fabaoqi = ''
    jutiAnJian = ''
    shujuku = {}
    shujukuMiWen = {}
    fabaojianMa={}
    danCiXianZhi = False
    fabaojian = {'输入':'','暂停':'','保存':'','退出':'','清空':'','半自动间距':''}
    tongJi = {'正确': 0, '超时': 0, '总次数': 0, '正确率': 0, '暂停': 0,'暂停时间':0,'总时间':0}
    tongJi_ZiYou = {'暂停': 0,'暂停时间':0,'总时间':0}
    print()
    bushijian = 0
    while 1:
        zantin = True
        kai = True
        print('欢迎使用摩根密码系列 ！！!')
        print('请使用英文输入法 !!!')
        print(' ==================||在cmd||')
        print(' =||你可以更舒适的使用这个程序。例如 【查询】Ctrl+F')
        print(' =||如果你的输入框一塌糊涂，你可以试着按下Esc键')
        print(' =||你可以很轻松地实现在同一台电脑上与同伴进行PK')
        print('本系列有以下几种玩法:\n')
        print('【1】摩根密码翻译器 【2】真·发电报 【3】摩根密码表 【147】退出程序')
        while 1:
            xuanze1 = input('请选择:')
            if xuanze1 == '147' or xuanze1 == '1' or xuanze1 == '2' or xuanze1 == '3':
                break
            else:
                print('抱歉，目前本人只想到以上4种选项 @v@')
        if xuanze1 == '147':
            break
        elif xuanze1 == '1':
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x40 | 0x100))
            print()
            print('快速编辑模式已启用 !!!')
            print('本选项为 密文与译文 的相互转换')
            print('PS: 支持   中文输入 和 密文译文混合输入   哦~~~')
            print('           |->符号还是需要用英文的哟')
            print('如果你的“字母语字母之间”，“单词与单词之间”的两种间距完美的话，转换后应该不会有问题')
            print('即使某几个间距多按或少按了，不必担心，我已经做了一些划分的处理，一些错误我可以帮你避免，但还是请你完美控制好两种间隔 ^H^')
            print('如果你想翻译文章，请在退出本功能后选择【历史串接】')
            print('【输入一个空格】 退出\n')
            tiaoshu = 0
            while 1:
                tiaoshu += 1
                print('<=>' * 10, end='')
                print('【{}】'.format(tiaoshu))
                zuanhuanwenben = input('[=]>请输入:')
                shujuku[tiaoshu] = zuanhuanwenben.strip()
                zuanhuanwenben = zuanhuanwenben.lower()
                if zuanhuanwenben == ' ':
                    print('为文章翻译而设计:【1】历史串接   【2】直接退出')
                    print(' ' * 14,'|===显示模式===|')
                    print('=' * 20, '原文', '=' * 20)
                    print('=' * 20, '译文', '=' * 20)
                    while 1:
                        chuanjie = input('请选择:')
                        chuanjieBianHao = []
                        if chuanjie == '1':
                            chuanjieBianHao.append(input('请输入一端的编号(首编号/尾编号):'))
                            chuanjieBianHao.append(input('请输入另一端的编号(首编号/尾编号):'))
                            try:
                                chuanjieBianHao[0] = int(chuanjieBianHao[0])
                                chuanjieBianHao[1] = int(chuanjieBianHao[1])
                                chuanjieBianHao = sorted(chuanjieBianHao)
                                print('=' * 20, '原文', '=' * 20)
                                for i in range(chuanjieBianHao[0],chuanjieBianHao[1]+1):
                                    print('\t',end='')
                                    print(shujuku[i])
                                print('=' * 20, '译文', '=' * 20)
                                for i in range(chuanjieBianHao[0],chuanjieBianHao[1]+1):
                                    print('\t',end='')
                                    print(shujukuMiWen[i])
                            except:
                                print()
                                print('!-!'*22)
                                print('!-!    出错了，编号应为 正整数,范围应为 [1->倒数第二个]    !-!')
                                print('!-!' * 25)
                                print()
                            print('为文章翻译而设计:【1】历史串接   【2】直接退出')
                        elif chuanjie == '2':
                            shujuku = {}
                            shujukuMiWen = {}
                            break
                        else:
                            print('请二选一')
                    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),
                                            (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
                    break
                zanshi = lazy_pinyin(zuanhuanwenben)
                zuanhuanwenben = ''
                for i in zanshi:
                    if i.strip() != '':
                        zuanhuanwenben += i + ' '
                shuchu = ''
                konggeshu = {}
                keyschangdu = []
                zanshi = []
                zuanhuanwenben = zuanhuanwenben.strip()
                for i in range(len(zuanhuanwenben)):
                    if zuanhuanwenben[i] == ' ' and zuanhuanwenben[i - 1] != ' ':
                        q = i
                        while 1:
                            q += 1
                            if zuanhuanwenben[q] != ' ':
                                konggeshu[' ' * (q - i)] = konggeshu.get(' ' * (q - i), 0) + 1
                                break
                if konggeshu == {}:
                    try:
                        if zuanhuanwenben == '-':
                            raise 0
                        shuchu = mimabiao[zuanhuanwenben]
                    except:
                        try:
                            if zuanhuanwenben == '-*--*-':
                                if '(' not in shuchu:
                                    shuchu = '('
                                elif ')' not in shuchu:
                                    shuchu = ')'
                                elif len(shuchu.split('(')) > len(shuchu.split(')')):
                                    shuchu = ')'
                                elif len(shuchu.split('(')) == len(shuchu.split(')')):
                                    shuchu = '('
                                shuchu = shuchu.strip()
                                print('||转换后|>>' + shuchu)
                                continue
                            shuchu = fanmimabiao[zuanhuanwenben]
                        except:
                            chongdie(zuanhuanwenben)
                else:
                    values = list(konggeshu.values())
                    keys = list(konggeshu.keys())
                    for i in keys:
                        keyschangdu.append(len(i))
                    try:
                        if values.count(max(values)) > 1:
                            for i in range(values.count(max(values))):
                                zanshi.append(keys[values.index(max(values))])
                                del keys[values.index(max(values))]
                                del values[values.index(max(values))]
                            for i in range(len(zanshi)):
                                zanshi[i] = len(zanshi[i])
                            zanshi = [' ' * max(zanshi), ' ' * min(zanshi)]
                            if konggeshu[min(zanshi)] < 2:
                                zanshi = [zanshi[1], zanshi[1]]
                        else:
                            zanshi.append(keys[values.index(max(values))])
                            zanshi = [zanshi[0] + ' ', zanshi[0]]
                            if len(zanshi[0]) > max(keyschangdu):
                                zanshi[0] = zanshi[1]
                    except:
                        pass
                    changzongshu = 0
                    for i in keyschangdu:
                        if i > len(zanshi[0]):
                            changzongshu += 1
                    try:
                        if changzongshu >= konggeshu[zanshi[0]] and konggeshu[zanshi[1]] >= 2:
                            zanshi[0] = zanshi[0] + ' '
                    except:
                        pass
                    zuanhuanwenben = zuanhuanwenben.split(zanshi[0])
                    qiedangao(zanshi[1])
                shuchu = shuchu.strip()
                shujukuMiWen[tiaoshu] = shuchu
                print('||转换后|>>' + shuchu)
        elif xuanze1 == '2':
            print()
            while 1:
                if fabaoqi == '':
                    fabaoqi = fabaoqiXuanZe()
                else:
                    print('检测到发报器已经完成设置，你需要修改吗？【1】继续   【2】修改')
                    while 1:
                        xiugaiyiyuan = input('请选择:')
                        if xiugaiyiyuan == '1':
                            break
                        elif xiugaiyiyuan == '2':
                            fabaoqi = fabaoqiXuanZe()
                            break
                        else:
                            print('请二选一')
                if fabaoqi == '1':
                    print('>=<' * 20)
                    print('设置完毕，当前发报器模式【鼠标】')
                    print('>=<' * 20)
                else:
                    print('>=<' * 20)
                    print('设置完毕，当前发报器模式【键盘】，按键表')
                    for i in fabaojian:
                        print('【' + i + '|' + fabaojian[i] + '】', end=' ')
                    print()
                    print('>=<' * 20)
                break
            print()
            print('【1】情景模式   【2】自由模式')
            while 1:
                xuanze2 = input('请选择:')
                if xuanze2 == '1' or xuanze2 == '2':
                    break
                else:
                    print('请二选一 !!!')
            if xuanze2 == '1':
                print()
                if tongJi != {'正确': 0, '超时': 0, '总次数': 0, '正确率': 0, '暂停': 0, '暂停时间': 0, '总时间': 0}:
                    print('检测到上次的统计信息未删除，请问是否重置？【1】否   【2】是')
                    while 1:
                        chongzhi = input('请决定:')
                        if chongzhi == '1':
                            break
                        elif chongzhi == '2':
                            tongJi = {'正确': 0, '超时': 0, '总次数': 0, '正确率': 0, '暂停': 0, '暂停时间': 0, '总时间': 0}
                            break
                        else:
                            print('请二选一')
                    print()
                print('间隔指的是文本之间的间隔，比如 aa无间隔     a a有间隔')
                print('而且 输入间隔 说的也是文本之间的间隔')
                print('【1】简单：你只需要照抄密文,可选择 不需要/手动/自动 输入间隔')
                print('【2】普通：不需要输入间隔')
                print('【3】困难：手动输入间隔')
                print('【4】真实：自动输入间隔，你需要把握好时间')
                while 1:
                    xuanze3 = input('请选择:')
                    if xuanze3 == '1' or xuanze3 == '2' or xuanze3 == '3' or xuanze3 == '4':
                        break
                    else:
                        print('请四选一 !')
                if xuanze3 == '1':
                    print()
                    print('【1】不需要输入间隔 【2】手动输入间隔 【3】自动输入间隔')
                    while 1:
                        xuanze8 = input('请选择:')
                        if xuanze8 == '1' or xuanze8 == '2' or xuanze8 == '3':
                            break
                        else:
                            print('请三选一 !')
                print()
                print('【1】 固定时长: 每一道密文时长 相等')
                print('【2】 随机时长: 每一道密文时长都是 随机生成')
                print('【3】 递增时长: 每解决一道密文，规定时长会 变长')
                print('【4】 递减时长: 每解决一道密文，规定时长会 变短')
                while 1:
                    xuanze4 = input('请选择: ')
                    if xuanze4 == '1' or xuanze4 == '2' or xuanze4 == '3' or xuanze4 == '4':
                        break
                    else:
                        print('请四选一 !')
                shichang = ashichang(xuanze4)
                print()
                print('【1】 固定长度: 每一道密文密码数 相等')
                print('【2】 随机长度: 每一道密文密码数都是 随机生成')
                print('【3】 递增长度: 每解决一道密文，规定密码数 变长')
                print('【4】 递减长度: 每解决一道密文，规定密码数 变短')
                while 1:
                    xuanze5 = input('请选择: ')
                    if xuanze5 == '1' or xuanze5 == '2' or xuanze5 == '3' or xuanze5 == '4':
                        break
                    else:
                        print('请四选一 !')
                changdu = achangdu()
                print()
                print('你希望有上司吗 ？？？')
                print('【1】 希望  【2】 不希望')
                while 1:
                    xuanze6 = input('请回答:')
                    if xuanze6 == '1' or xuanze6 == '2':
                        break
                    else:
                        print('请二选一 !')
                if xuanze6 == '1':
                    print()
                    print('你的上司一般多久让你发一份密文 ???')
                    dendai = ashichang(xuanze6, False)
                    print()
                    print('你希不希望在上司给你发电报后提醒你')
                    print('【1】希望  【2】不希望')
                    while 1:
                        xuanze7 = input('请决定:')
                        if xuanze7 == '1' or xuanze7 == '2':
                            if xuanze7 == '1':
                                print('已为你设置提示音')
                            break
                        else:
                            print('请二选一 !')
                    print('现在，等待你的上司给你委派工作 !!!')
                qishiShiJian = time.perf_counter()
                while kai:
                    if xuanze6 == '1':
                        suiji = random.randint(0, dendai)
                        tt = time.perf_counter()
                        while 1:
                            print(' ' * 60, end='')
                            dendaishichang = int(time.perf_counter() - tt)
                            if dendaishichang < 60:
                                zanshi = '\r||<=>' + '.' * (dendaishichang % 7) + '你等待了 ' + str(
                                    dendaishichang) + ' 秒 ' + ('.' * (dendaishichang % 7) + '<=>||')
                            elif dendaishichang < 3600:
                                zanshi = '\r||<=>' + '.' * (dendaishichang % 7) + '你等待了 ' + '{:.0f}分 {:.0f}秒'.format(
                                    dendaishichang // 60, dendaishichang % 60) + ('.' * (dendaishichang % 7) + '<=>||')
                            elif dendaishichang < 86400:
                                zanshi = '\r||<=>' + '.' * (dendaishichang % 7) + '你等待了 ' + '{:.0f}时 {:.0f}分 {:.0f}秒'.format(
                                    dendaishichang // 3600, (dendaishichang % 3600) // 60,
                                    (dendaishichang % 3600) % 60) + ('.' * (dendaishichang % 7) + '<=>||')
                            else:
                                zanshi = '\r||<=>' + '.' * (dendaishichang % 7) + '你等待了 ' + '{:.0f}天 {:.0f}时 {:.0f}分 {:.0f}秒'.format(
                                    dendaishichang // 86400, (dendaishichang % 86400) // 3600,
                                    ((dendaishichang % 86400) % 3600) // 60,
                                    (((dendaishichang % 86400) % 3600) % 60)) + ('.' * (dendaishichang % 7) + '<=>||')
                            print(zanshi, end='\r')
                            if time.perf_counter() - tt > suiji:
                                print()
                                if xuanze7 == 0:
                                    xuanze7 = '1'
                                if xuanze7 == '1':
                                    pygame.mixer.music.load(r'.\W48.wav')
                                    pygame.mixer.music.play(-1)
                                break
                            time.sleep(1)
                    if xuanze4 == '1':
                        shijian = shichang
                    elif xuanze4 == '2':
                        shijian = random.randint(shichang[0], shichang[1])
                    else:
                        shichang[0] += shichang[1]
                        shijian = shichang[0]
                    if xuanze5 == '1':
                        geshu = changdu
                    elif xuanze5 == '2':
                        geshu = random.randint(changdu[0], changdu[1])
                    else:
                        changdu[0] += changdu[1]
                        geshu = changdu[0]
                    jingdutiao()
                    bianmaqian = ''
                    if qianxi():
                        print()
                        if shijian <= 0:
                            print('本次你没有时间可以破译 !!!')
                        else:
                            if shijian < 60:
                                print('Because没有在 {:.0f}秒 内发送，需要重新开始发送 ^_^\n'.format(shijian))
                            elif shijian < 3600:
                                print('Because没有在 {:.0f}分 {:.0f}秒 内发送，需要重新开始发送 ^_^\n'.format(shijian // 60, shijian % 60))
                            elif shijian < 86400:
                                print('Because没有在 {:.0f}时 {:.0f}分 {:.0f}秒 内发送，需要重新开始发送 ^_^\n'.format(shijian // 3600,
                                                                                         (shijian % 3600) // 60,
                                                                                         (shijian % 3600) % 60))
                            else:
                                print('Because没有在 {:.0f}天 {:.0f}时 {:.0f}分 {:.0f}秒 内发送，需要重新开始发送 ^_^\n'.format(shijian // 86400,
                                                                                             (shijian % 86400) // 3600,
                                                                                             ((
                                                                                                          shijian % 86400) % 3600) // 60,
                                                                                             (((
                                                                                                           shijian % 86400) % 3600) % 60)))
                        time.sleep(1)
                    if kai == False:
                        print()
                        print('\t\t|==|','下面是你本次使用此模式的统计信息','|==|')
                        try:
                            tongJi['总次数'] = tongJi['正确'] + tongJi['超时']
                            tongJi['正确率'] = tongJi['正确'] / tongJi['总次数']
                            tongJi['总时间'] += time.perf_counter() - qishiShiJian
                            for i in tongJi:
                                if i == '暂停时间':
                                    print('------------------------------|==|',i,shijianHuanSuan(tongJi['暂停时间']))
                                    continue
                                elif i == '总时间':
                                    print('------------------------------|==|',i,shijianHuanSuan(tongJi['总时间']))
                                    continue
                                elif i == '正确率':
                                    print('------------------------------|==| {} {:.0f}%'.format(i,tongJi['正确率']*100))
                                    continue
                                print('------------------------------|==|',i,tongJi[i])
                        except:
                            print()
                            print('\t\t!-!    抱歉，无法找到本次的使用记录    !-!')
                            print()
                        print()
                        print('>=<' * 40, end='')
            elif xuanze2 == '2':
                print()
                if tongJi_ZiYou != {'暂停': 0, '暂停时间': 0, '总时间': 0}:
                    print('检测到上次的统计信息未删除，请问是否重置？【1】否   【2】是')
                    while 1:
                        chongzhi_ZiYou = input('请决定:')
                        if chongzhi_ZiYou == '1':
                            break
                        elif chongzhi_ZiYou == '2':
                            tongJi_ZiYou = {'暂停': 0, '暂停时间': 0, '总时间': 0}
                            break
                        else:
                            print('请二选一')
                    print()
                jiesao()
                xuanze3 = ''
                qiaochulai = ''
                qishiShiJian_ZiYou = time.perf_counter()
                while 1:
                    if fabaoqi == '1':
                        with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
                            listener.join()
                    else:
                        with keyboard.Listener(on_press=jianpan_on_press,on_release=jianpan_on_release) as jianpanlistener:
                            jianpanlistener.join()
                    pygame.mixer.music.stop()
                    if zantin:
                        break
                    else:
                        zantin = True
                        print()
                        tongJi_ZiYou['暂停'] += 1
                        print('已经为你暂停发报 ！！！')
                        zanting_ZiYou = time.perf_counter()
                        print('已经开启快速编辑模式，你可以自由复制些什么 !!!')
                        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),
                                                (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x40 | 0x100))
                        os.system('pause')
                        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),
                                                (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
                        print('已关闭快速编辑模式 !!!')
                        print('>===继续发报===<')
                        tongJi_ZiYou['暂停时间'] += time.perf_counter() - zanting_ZiYou
                print()
                print('||你的保存||[>>]')
                if baochun == []:
                    print('  {}你没有保存任何东西 !!!{}'.format('<=>' * 4, '<=>' * 4))
                else:
                    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),
                                            (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x40 | 0x100))
                    tiaoguo = False
                    try:
                        a = open('机密.txt', 'r', encoding='utf-8')
                        b = a.read().split('\n')
                        del b[-1]
                        if b == []:
                            tiaoguo = True
                        a.close()
                    except:
                        tiaoguo = True
                    if tiaoguo == False:
                        jieshu = 0
                        for i in b[::-1]:
                            if i[:1] == '第':
                                jieshu = int(i.split()[1])
                                break
                    jishu = 0
                    daijiaru = []
                    for i in range(len(baochun)):
                        if baochun[i] == '#':
                            jishu += 1
                            if tiaoguo:
                                daijiaru.append('第 ' + str(jishu) + ' 条===')
                                daijiaru.append('密文\t' + baochun[i + 1])
                                daijiaru.append('译文\t' + baochun[i + 2])
                            elif len(baochun) <= len(b):
                                if '密文\t' + baochun[i + 1] not in b:
                                    jieshu += 1
                                    daijiaru.append('第 ' + str(jieshu) + ' 条===')
                                    daijiaru.append('密文\t' + baochun[i + 1])
                                    daijiaru.append('译文\t' + baochun[i + 2])
                            print('第 ' + str(jishu) + ' 条===')
                            print('密文\t' + baochun[i + 1])
                            print('译文\t' + baochun[i + 2])
                    if tiaoguo == False and len(baochun) > len(b):
                        for i in b:
                            if i[0] == '密' and i[3:] not in baochun:
                                jieshu += 1
                                daijiaru.append('第 ' + str(jieshu) + ' 条===')
                                daijiaru.append('密文\t' + baochun[i + 1])
                                daijiaru.append('译文\t' + baochun[i + 2])
                    print()
                    print('不必担心，我不会保存一样的东西 !!!')
                    print('已经开启快速编辑模式，你可以复制上面的资料 !!!\n')
                    print('你想保存在本地吗？我可以帮你把这些保存为  机密.txt  哦~~ %v%')
                    print('【1】 保存   【2】 不保存   【3】 清空 ||你的保存||[>>] 且 不保存并退出')
                    while 1:
                        zanshi = input('请选择:')
                        if zanshi == '1' or zanshi == '2' or zanshi == '3':
                            break
                        else:
                            print('请三选一 !!!')
                    if zanshi == '1':
                        if tiaoguo:
                            a = open('机密.txt', 'w', encoding='utf-8')
                        else:
                            a = open('机密.txt', 'a', encoding='utf-8')
                        for i in daijiaru:
                            a.write(i + '\n')
                        a.close()
                        print('  {}已经为你保存至本地   机密.txt{}'.format('<=>' * 3, '<=>' * 3))
                    elif zanshi == '2':
                        pass
                    else:
                        baochun.clear()
                    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),
                                            (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
                print()
                print('\t\t|==|','下面是你本次使用此模式的统计信息','|==|')
                tongJi_ZiYou['总时间'] += time.perf_counter() - qishiShiJian_ZiYou
                for i in tongJi_ZiYou:
                    if i == '暂停时间':
                        print('------------------------------|==|',i,shijianHuanSuan(tongJi_ZiYou['暂停时间']))
                        continue
                    elif i == '总时间':
                        print('------------------------------|==|',i,shijianHuanSuan(tongJi_ZiYou['总时间']))
                        continue
                    print('------------------------------|==|',i, tongJi_ZiYou[i])
                print()
                print('>=<' * 40, end='')
        else:
            for i in mimabiao:
                print('【' + i + '|' + mimabiao[i] + '】', end=' ')
            print()
            print('>=<' * 40, end='')