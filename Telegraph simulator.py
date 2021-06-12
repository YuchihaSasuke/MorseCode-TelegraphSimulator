import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
import time
import random
import os
from pynput import mouse
from pynput.mouse import Button, Controller
import pygame
from pypinyin import lazy_pinyin
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=256)
pygame.mixer.music.load(r'.\600.wav')
biao='abcdefghijklmnopqrstuvwxyz0123456789?/()-.'
mimabiao={'a': '*-', 'b': '-***', 'c': '-*-*', 'd': '-**', 'e': '*', 'f': '**-*', 'g': '--*', 'h': '****', 'i': '**', 'j': '*---', 'k': '-*-', 'l': '*-**', 'm': '--', 'n': '-*', 'o': '---', 'p': '*--*', 'q': '--*-', 'r': '*-*', 's': '***', 't': '-', 'u': '**-', 'v': '***-', 'w': '*--', 'x': '-**-', 'y': '-*--', 'z': '--**', '1': '*----', '2': '**---', '3': '***--', '4': '****-', '5': '*****', '6': '-****', '7': '--***', '8': '---**', '9': '----*', '0': '-----', '?': '**--**', '/': '-**-*', '(': '-*--*-', ')': '-*--*-', '-': '-****-', '.': '*-*-*-'}
fanmimabiao={'*-': 'a', '-***': 'b', '-*-*': 'c', '-**': 'd', '*': 'e', '**-*': 'f', '--*': 'g', '****': 'h', '**': 'i', '*---': 'j', '-*-': 'k', '*-**': 'l', '--': 'm', '-*': 'n', '---': 'o', '*--*': 'p', '--*-': 'q', '*-*': 'r', '***': 's', '-': 't', '**-': 'u', '***-': 'v', '*--': 'w', '-**-': 'x', '-*--': 'y', '--**': 'z', '*----': '1', '**---': '2', '***--': '3', '****-': '4', '*****': '5', '-****': '6', '--***': '7', '---**': '8', '----*': '9', '-----': '0', '**--**': '?', '-**-*': '/', '-****-': '-', '*-*-*-': '.'}
baochun=[]
scale=50
def jiesao():
    global mima,mogenmima
    if xuanze2=='1':
        if geshu<=0:
            mima='You have no ciphertext to decipher !!!'
            mogenmima='You have no ciphertext to decipher !!!'
        if xuanze3=='1':
            print('password===||  ' + mogenmima + '   ||')
        else:
            print('password===||  ' + mima + '   ||')
        print('=====-----|NvN|Timing begins|NvN|-----=====')
        # print('【Pay attention to spaces】E.g： | ee == * *(One spaces) |\t| e e == *  *(Two spaces) |')
        print('【Left button】 import   【Scroll up】 Exit 【Right click】 Clear  【Move the mouse to the upper left corner】 pause')
        print('If you make a mistake, you can use ****** (ie 6 *) to delete the most recent mistake ')
    else:
        print('Introduction：')
        print('【Pay attention to spaces】E.g： | ee == * *(One spaces) |\t| e e == *  *(Two spaces) |')
        print('【Left button】 import   【Scroll up】 Exit 【Scroll down】 save   【Right key】Clear   【Move the mouse to the upper left corner】 pause')
        print('If you make a mistake, you can use ****** (ie 6 *) to delete the most recent mistake ')
        print('Free reporting area')
        print('=' * 50)
def jingdutiao(a=0.01,b='>'):
    print("Start loading".center(scale // 2, "-"))
    start = time.perf_counter()
    for i in range(scale + 1):
        r = b * i
        y = ' ' * (scale - i)
        p = (i / scale) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}{}]{:.2f}s".format(p, r, y, dur), end="")
        time.sleep(a)
    print("\n" + "Loaded".center(scale // 2, '-'))
def on_move(x, y):
    global zantin
    if x<5 and y<5:
        zantin=False
        return False
def on_scroll(x, y, dx, dy):
    global qiaochulai,kai
    try:
        if dy>0:
            if xuanze2=='1':
                kai=False
            return False
        else:
            if xuanze2=='2' and qiaochulai.strip() !='' and qiaochulai.strip() not in baochun:
                baochun.append('#')
                baochun.append(qiaochulai.strip())
                baochun.append(jieshi.strip())
                print(' {}Saved successfully !!!{}'.format('<=>' * 6, '<=>' * 6))
                print('  {}Don’t worry, I won’t save the same thing !!!{}'.format('<=>' * 2, '<=>' * 2))
    except:
        pass
def on_click(x, y, button, pressed):
    global atime, btime, qiaochulai,jieshi,xuanze7
    try:
        if pressed:
            try:
                if xuanze7=='1':
                    pygame.mixer.music.load(r'.\600.wav')
                    pygame.mixer.music.stop()
                    xuanze7=0
            except:
                pass
            if xuanze3=='3' or xuanze3=='1' and xuanze8=='2':
                if button==button.middle:
                    qiaochulai+=' '
            if button==button.left:
                pygame.mixer.music.play(-1)
                atime = time.perf_counter()
                if time.perf_counter() - btime > 0.3:
                    qiaochulai += ' '
                if xuanze2=='2' or xuanze3=='1' and xuanze8=='3' or xuanze3=='4':
                    if time.perf_counter() - btime > 0.7:
                        qiaochulai += ' '
        else:
            if xuanze2 == '1' and time.perf_counter() - timea - bushijian > shijian:
                return False
            elif button==button.left:
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
                    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),(0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
                    jiesao()
                    print('='*50)
                    print('\rYour message=>|' + qiaochulai)
                    print('='*50)
                    daojishi=int(shijian - ((time.perf_counter() - timea) - bushijian))
                    if daojishi<60:
                        print('You have a total of {} second !!!'.format(shijian))
                        print('Left {} second !!!'.format(daojishi))
                    elif daojishi<3600:
                        print('You have a total of {} seconds {}minute !!!'.format(shijian // 60,shijian % 60))
                        print('Left {} seconds {}minute !!!'.format(daojishi // 60,daojishi % 60))
                    elif daojishi < 86400:
                        print('You have a total of {} seconds {}minute {}hour !!!'.format(shijian // 3600,(shijian % 3600) // 60,(shijian % 3600) % 60))
                        print('Left {} seconds {}minute {}hour !!!'.format(daojishi // 3600,(daojishi % 3600) // 60,(daojishi % 3600) % 60))
                    else:
                        print('You have a total of {} seconds {}minute {}hour {}day !!!'.format(shijian // 86400, (shijian % 86400) // 3600, ((shijian % 86400) % 3600) // 60, (((shijian % 86400) % 3600) % 60)))
                        print('Left {} seconds {}minute {}hour {}day !!!'.format(daojishi // 86400, (daojishi % 86400) // 3600, ((daojishi % 86400) % 3600) // 60, (((daojishi % 86400) % 3600) % 60)))
                    print('-'*15)
                    if qiaochulai.strip() == mogenmima.strip():
                        return False
                else:
                    jieshi=''
                    if qiaochulai.strip()!='':
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
                                    if zanshi[q]=='-*--*-':
                                        if '(' not in jieshi:
                                            jieshi+='('
                                        elif ')' not in jieshi:
                                            jieshi+=')'
                                        elif len(jieshi.split('('))>len(jieshi.split(')')):
                                            jieshi+=')'
                                        elif len(jieshi.split('('))==len(jieshi.split(')')):
                                            jieshi+='('
                                    elif zanshi[q]=='******':
                                        jieshi=jieshi.strip()[:-1]
                    os.system('cls')
                    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),(0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
                    jiesao()
                    print('\rYour message=>|' + qiaochulai)
                    print('=' * 50)
                    print('Explanation》' + jieshi)
                    print('-' * 50)
            elif button == button.right:
                qiaochulai=''
                jieshi=''
                os.system('cls')
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),(0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
                jiesao()
    except:
        pass
def qianxi():
    global timea,bianmaqian,qiaochulai,mima,mogenmima,bushijian
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
    timea=time.perf_counter()
    print()
    qiaochulai = ''
    while 1:
        with mouse.Listener(on_move=on_move,on_click=on_click, on_scroll=on_scroll) as listener:
            listener.join()
        pygame.mixer.music.stop()
        if kai==False:
            bushijian = 0
            return
        if time.perf_counter() - timea - bushijian > shijian:
            bushijian = 0
            return 1
        elif qiaochulai.strip()==mogenmima.strip():
            bushijian = 0
            print()
            print('The right key! ! ! Sent successfully ！！！')
            break
        else:
            print()
            timeb=time.perf_counter()
            print('Has been suspended for you ！！！')
            print('Quick edit mode has been turned on, what you can copy freely !!!')
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x40 | 0x100))
            input('【Enter】 continue...NoN')
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
            bushijian+=time.perf_counter()-timeb
            print('Quick edit mode turned off !!!')
            print('>===Continue to report===<')
def ashichang(xuanze,kaiguan=True):
    print()
    print('PS: You don’t need to care about the 24 hours and 60 minutes and 60 seconds rules')
    print('    Enter directly to enter 0')
    print('If you press Enter directly, the default time is one minute')
    if kaiguan:
        if xuanze=='1':
            print('How long do you need to solve one ？？？')
            print('Next you need to enter hours|minutes|seconds respectively')
        elif xuanze=='2':
            liebiao=[]
            print('You need to enter two rounds of hours|minutes|seconds')
            print('One round is the minimum value of random duration, and the other round is the maximum value of random duration')
            print('If the values entered in the two rounds are the same, it is equivalent to a fixed duration')
            print('Size in no particular order\n')
            print('|<=>first round<=>|\n')
        else:
            liebiao=[]
            print('You need to enter the hours|minutes|seconds and then the tolerance (that is, the value of increasing and decreasing)')
            print('If the tolerance is zero, it will not change')
        print('=' * 12)
    while 1:
        shichang = 0
        for i in ['hour', 'minute', 'second']:
            if i == 'hour':
                zanshi = 3600
            elif i == 'minute':
                zanshi = 60
            else:
                zanshi = 1
            while 1:
                xuanze = input('Please decide(' + i + '): ')
                if set(xuanze) <= {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                    if xuanze != '':
                        shichang += int(xuanze) * zanshi
                    print('=' * 12)
                    break
                else:
                    print('Sorry i can‘t recognize how long you want……AvA')
        if shichang==0:
            shichang=60
            print('You chose the default one minute !!!')
        if kaiguan:
            if xuanze4=='1':
                break
            elif xuanze4=='2' or xuanze4=='3' or xuanze4=='4':
                liebiao.append(shichang)
                if len(liebiao)==1:
                    print()
                    if xuanze4=='2':
                        print('|<=>second round<=>|\n')
                    else:
                        print('|<=>Now decide the tolerance<=>|\n')
                elif len(liebiao)==2:
                    if xuanze4=='2':
                        shichang=[min(liebiao),max(liebiao)]
                    elif xuanze4=='3':
                        shichang=[liebiao[0]-liebiao[1],liebiao[1]]
                    else:
                        shichang=[liebiao[0]+liebiao[1],-liebiao[1]]
                    break
        else:
            break
    return shichang
def achangdu():
    print()
    print('What is the length of the initial ciphertext you want ？？？')
    print('If you press enter directly, the default length is 20')
    if xuanze5=='2':
        liebiao=[]
        print('You need to enter two ciphertext lengths one after the other')
        print('One is the minimum ciphertext length, and the other is the maximum ciphertext length')
        print('If the value entered twice is the same, it is equivalent to a fixed length')
        print('Size in no particular order\n')
        print('|<=>First<=>|\n')
    elif xuanze5=='3' or xuanze5=='4':
        liebiao=[]
        print('You need to enter the initial ciphertext length first and then enter the tolerance (that is, the value of increasing and decreasing)')
        print('If the tolerance is zero, it will not change')
    while 1:
        changdu = 20
        zanshi = input('Please decide: ')
        if set(zanshi) <= {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            if zanshi == '':
                print('You have chosen the default 20 lengths !!!')
            elif zanshi != '':
                changdu = int(zanshi)
            if xuanze5 == '1':
                break
            elif xuanze5=='2' or xuanze5=='3' or xuanze5=='4':
                liebiao.append(changdu)
                if len(liebiao) == 1:
                    print()
                    if xuanze5 == '2':
                        print('|<=>the second<=>|\n')
                    else:
                        print('|<=>Now decide the tolerance<=>|\n')
                elif len(liebiao) == 2:
                    if xuanze5=='2':
                        changdu = [min(liebiao), max(liebiao)]
                    elif xuanze5=='3':
                        changdu=[liebiao[0]-liebiao[1],liebiao[1]]
                    else:
                        changdu=[liebiao[0]+liebiao[1],-liebiao[1]]
                    break
        else:
            print('I can’t recognize how long you are... yeah yeah')
    return changdu
def chongdie(q):
    global shuchu
    for w in range(len(q)):
        if q[w]==' ' or w!=0 and q[w] == '*' and (q[w - 1] == '*' or q[w - 1] == '-') or w!=0 and q[w] == '-' and (q[w - 1] == '*' or q[w - 1] == '-'):
            continue
        zanshi=q[w]
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
                if w!=0:
                    shuchu=shuchu.strip()
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
        if i=='':
            continue
        zanshi=i.strip().split(w)
        for q in zanshi:
            q=q.strip()
            if q==' ':
                continue
            try:
                if q=='-':
                    raise 0
                shuchu += mimabiao[q]
                shuchu+=' '
            except:
                try:
                    if zanshi.index(q)!=0:
                        shuchu=shuchu.strip()
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
        shuchu+=' '
if __name__=="__main__":
    print()
    bushijian=0
    while 1:
        zantin=True
        kai=True
        print('Welcome to use Morse code series ！！!')
        print('Please use English input method !!!')
        print('There are several ways to play in this series:\n')
        print('【1】Morse code translator 【2】True telegram 【3】Morse Code Table 【Enter key】Exit the program')
        while 1:
            xuanze1=input('please choose:')
            if xuanze1=='' or xuanze1=='1' or xuanze1=='2' or xuanze1=='3':
                break
            else:
                print('Sorry, I only think of the above 4 options at the moment @v@')
        if xuanze1=='':
            break
        elif xuanze1=='1':
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x40 | 0x100))
            print()
            print('Quick edit mode is enabled !!!')
            print('This option is the mutual conversion of ciphertext and translation')
            print('PS: Support Chinese input and ciphertext translation mixed input oh~~~')
            print('           |->The symbols still need to be in English')
            print('If your "between letters" and "between words" are perfect, there should be no problems after conversion.')
            print('Even if a few intervals are pressed more or less, don’t worry, I have done some division processing, and I can help you avoid some errors, but please control the two intervals perfectly.^H^')
            print('【Enter directly】Exit\n')
            tiaoshu=0
            while 1:
                tiaoshu+=1
                print('<=>' * 10, end='')
                print('【{}】'.format(tiaoshu))
                zuanhuanwenben = input('[=]>please import:')
                if zuanhuanwenben == '':
                    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),(0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
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
                                print('||After conversion|>>' + shuchu)
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
                print('||After conversion|>>' + shuchu)
        elif xuanze1=='2':
            print()
            print('【1】Scene mode   【2】Free mode')
            while 1:
                xuanze2=input('please choose:')
                if xuanze2=='1' or xuanze2=='2':
                    break
                else:
                    print('Please choose one of the two !!!')
            if xuanze2=='1':
                print()
                print('Interval refers to the interval between texts, such as aa without interval a a with interval')
                print('And the input interval is also the interval between texts')
                print('【1】Simple: you only need to copy the ciphertext, you can choose not to manually enter the interval automatically')
                print('【2】Normal: no need to enter the interval')
                print('【3】Difficulty: Enter the interval manually (click the middle mouse button)')
                print('【4】Real: Automatically enter the interval, you need to grasp the time')
                while 1:
                    xuanze3=input('please choose:')
                    if xuanze3=='1' or xuanze3=='2' or xuanze3=='3' or xuanze3 == '4':
                        break
                    else:
                        print('Please choose one of four !')
                if xuanze3=='1':
                    print()
                    print('【1】No need to enter the interval 【2】Manually enter the interval 【3】Automatically enter the interval')
                    while 1:
                        xuanze8=input('please choose:')
                        if xuanze8=='1' or xuanze8=='2' or xuanze8=='3':
                            break
                        else:
                            print('Please choose one of three !')
                print()
                print('【1】 Fixed duration: the duration of each ciphertext is equal')
                print('【2】 Random duration: The duration of each ciphertext is randomly generated')
                print('【3】 Increasing duration: Each time a ciphertext is solved, the prescribed duration will become longer')
                print('【4】 Decrease duration: Each time a ciphertext is solved, the prescribed duration will become shorter')
                while 1:
                    xuanze4=input('please choose: ')
                    if xuanze4 == '1' or xuanze4 == '2' or xuanze4 == '3' or xuanze4=='4':
                        break
                    else:
                        print('Please choose one of four !')
                shichang=ashichang(xuanze4)
                print()
                print('【1】 Fixed length: the number of each ciphertext password is equal')
                print('【2】 Random length: The number of each ciphertext password is randomly generated')
                print('【3】 Increasing length: Each time a ciphertext is solved, the number of passwords becomes longer')
                print('【4】 Decrease length: Each time a ciphertext is solved, the specified number of passwords becomes shorter')
                while 1:
                    xuanze5=input('please choose: ')
                    if xuanze5 == '1' or xuanze5 == '2' or xuanze5 == '3' or xuanze5 == '4':
                        break
                    else:
                        print('Please choose one of four !')
                changdu=achangdu()
                print()
                print('Do you wish to have a boss ？？？')
                print('【1】 Hope 【2】 Don’t want')
                while 1:
                    xuanze6=input('Please answer:')
                    if xuanze6=='1' or xuanze6=='2':
                        break
                    else:
                        print('Please choose one of the two !')
                if xuanze6 == '1':
                    print()
                    print('How often does your boss ask you to send a ciphertext ???')
                    dendai = ashichang(xuanze6, False)
                    print()
                    print('Do you want to remind you after your boss sends you a telegram')
                    print('【1】 Hope 【2】 Don‘t want')
                    while 1:
                        xuanze7=input('Please decide:')
                        if xuanze7=='1' or xuanze7=='2':
                            if xuanze7=='1':
                                print('The alert tone has been set for you')
                            break
                        else:
                            print('Please choose one of the two !')
                    print('Now, waiting for your boss to delegate work to you !!!')
                while kai:
                    if xuanze6 == '1':
                        suiji = random.randint(0, dendai)
                        tt = time.perf_counter()
                        while 1:
                            print(' ' * 60, end='')
                            dendaishichang=int(time.perf_counter() - tt)
                            if dendaishichang<60:
                                zanshi = '\r||<=>' + '.' * (dendaishichang % 7) + 'You waited ' + str(dendaishichang) + ' seconds ' + ('.' * (dendaishichang % 7) + '<=>||')
                            elif dendaishichang<3600:
                                zanshi = '\r||<=>' + '.' * (dendaishichang % 7) + 'You waited ' + '{} seconds {}minute'.format(dendaishichang//60,dendaishichang%60) + ('.' * (dendaishichang % 7) + '<=>||')
                            elif dendaishichang<86400:
                                zanshi = '\r||<=>' + '.' * (dendaishichang % 7) + 'You waited ' + '{} seconds {}minute {}hour'.format(dendaishichang // 3600, (dendaishichang % 3600) // 60, (dendaishichang % 3600) % 60) + ('.' * (dendaishichang % 7) + '<=>||')
                            else:
                                zanshi = '\r||<=>' + '.' * (dendaishichang % 7) + 'You waited ' + '{} seconds {}minute {}hour {}day'.format(dendaishichang//86400,(dendaishichang%86400)//3600,((dendaishichang%86400)%3600)//60,(((dendaishichang%86400)%3600)%60)) + ('.' * (dendaishichang % 7) + '<=>||')
                            print(zanshi, end='\r')
                            if time.perf_counter() - tt > suiji:
                                print()
                                if xuanze7==0:
                                    xuanze7='1'
                                if xuanze7=='1':
                                    pygame.mixer.music.load(r'.\W48.wav')
                                    pygame.mixer.music.play(-1)
                                break
                            time.sleep(1)
                    if xuanze4 == '1':
                        shijian=shichang
                    elif xuanze4 == '2':
                        shijian = random.randint(shichang[0], shichang[1])
                    else:
                        shichang[0] += shichang[1]
                        shijian=shichang[0]
                    if xuanze5 == '1':
                        geshu=changdu
                    elif xuanze5 == '2':
                        geshu = random.randint(changdu[0], changdu[1])
                    else:
                        changdu[0] += changdu[1]
                        geshu=changdu[0]
                    jingdutiao()
                    bianmaqian = ''
                    if qianxi():
                        print()
                        if shijian<=0:
                            print('You don’t have time to decipher this time !!!')
                        else:
                            if shijian<60:
                                print('Because it was not sent within {} seconds, you need to start sending again ^_^\n'.format(shijian))
                            elif shijian<3600:
                                print('Because it was not sent within {} seconds {}minute, you need to start sending again ^_^\n'.format(shijian // 60,shijian % 60))
                            elif shijian<86400:
                                print('Because it was not sent within {} seconds {}minute {}hour, you need to start sending again ^_^\n'.format(shijian // 3600,(shijian % 3600) // 60,(shijian % 3600) % 60))
                            else:
                                print('Because it was not sent within {} seconds {}minute {}hour {}day, you need to start sending again ^_^\n'.format(shijian // 86400, (shijian % 86400) // 3600, ((shijian % 86400) % 3600) // 60, (((shijian % 86400) % 3600) % 60)))
                        time.sleep(1)
                    if kai==False:
                        print()
                        print('>=<' * 40, end='')
            elif xuanze2=='2':
                print()
                jiesao()
                xuanze3=''
                qiaochulai = ''
                while 1:
                    with mouse.Listener(on_move=on_move,on_click=on_click, on_scroll=on_scroll) as listener:
                        listener.join()
                    pygame.mixer.music.stop()
                    if zantin:
                        break
                    else:
                        zantin=True
                        print()
                        print('Has been suspended for you ！！！')
                        print('Quick edit mode has been turned on, what you can copy freely !!!')
                        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),(0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x40 | 0x100))
                        input('【Enter】 continue...NoN')
                        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),(0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
                        print('Quick edit mode turned off !!!')
                        print('>===Continue to report===<')
                print()
                print('||Your save||[>>]')
                if baochun==[]:
                    print('  {}You didn‘t save anything !!!{}'.format('<=>' * 4, '<=>' * 4))
                else:
                    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),(0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x40 | 0x100))
                    tiaoguo=False
                    try:
                        a = open('secret.txt', 'r', encoding='utf-8')
                        b=a.read().split('\n')
                        del b[-1]
                        if b == []:
                            tiaoguo=True
                        a.close()
                    except:
                        tiaoguo=True
                    if tiaoguo==False:
                        jieshu=0
                        for i in b[::-1]:
                            if i[:1] == 'number':
                                jieshu = int(i.split()[1])
                                break
                    jishu=0
                    daijiaru=[]
                    for i in range(len(baochun)):
                        if baochun[i]=='#':
                            jishu += 1
                            if tiaoguo:
                                daijiaru.append('number ' + str(jishu) + ' Article===')
                                daijiaru.append('Ciphertext\t' + baochun[i + 1])
                                daijiaru.append('Translation\t' + baochun[i + 2])
                            elif len(baochun)<=len(b):
                                if 'Ciphertext\t'+baochun[i+1] not in b:
                                    jieshu+=1
                                    daijiaru.append('number ' + str(jieshu) + ' Article===')
                                    daijiaru.append('Ciphertext\t'+baochun[i+1])
                                    daijiaru.append('Translation\t'+baochun[i+2])
                            print('number '+str(jishu)+' Article===')
                            print('Ciphertext\t'+baochun[i+1])
                            print('Translation\t'+baochun[i+2])
                    if tiaoguo==False and len(baochun) > len(b):
                        for i in b:
                            if i[0]=='C' and i[3:] not in baochun:
                                jieshu += 1
                                daijiaru.append('number ' + str(jieshu) + ' Article===')
                                daijiaru.append('Ciphertext\t' + baochun[i + 1])
                                daijiaru.append('Translation\t' + baochun[i + 2])
                    print()
                    print('Don’t worry, I won’t save the same thing !!!')
                    print('Quick edit mode has been turned on, you can copy the above data !!!\n')
                    print('Do you want to save it locally? I can help you save these as secret.txt oh~~ %v%')
                    print('【1】 save   【2】 do not save   【3】 Empty ||Your save||[>>] 且 Don’t save and exit')
                    while 1:
                        zanshi=input('please choose:')
                        if zanshi=='1' or zanshi=='2' or zanshi=='3':
                            break
                        else:
                            print('Please choose one of three !!!')
                    if zanshi=='1':
                        if tiaoguo:
                            a = open('secret.txt', 'w', encoding='utf-8')
                        else:
                            a = open('secret.txt', 'a', encoding='utf-8')
                        for i in daijiaru:
                            a.write(i + '\n')
                        a.close()
                        print('  {}Has been saved to the local secret.txt for you{}'.format('<=>' * 3, '<=>' * 3))
                    elif zanshi=='2':
                        pass
                    else:
                        baochun.clear()
                    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),(0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))
                print('>=<' * 40, end='')
        else:
            for i in mimabiao:
                print('【'+i+'|'+mimabiao[i]+'】',end = ' ')
            print()
            print('>=<' * 40, end='')