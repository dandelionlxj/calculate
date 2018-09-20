import re
import random 
def getSignal():  # 获取符号
    signal = ['+', '-', '*', '÷']
    r = random.randint(0, 3)
    return signal[r]

def getNum(i):  # 获取数字
    a = random.randint(1, i)
    b = random.randint(1, i)
    c = change(a, b)
    return c

def change(a, b):
    if (a >= b):
        if (a % b == 0):
            return "|%d|"%(a / b)
        else:
            return "|%d/%d|"%(a,b)
    return "|%d/%d|"%(a,b)

def getChNum():  # 获得字符个数1-3
    a = random.randint(1, 3)  #包括上下限
    return a




def getExample(l):  # 获取表达式
    a = getNum(l)
    for i in range(getChNum()):  # 不包括上限
        c = getSignal()
        f = random.randint(0, 1)
        if (f == 1):
            b = getNum(l)
        else:
            b = random.randint(1, l)
            b = "|%d|" % (b)
        if (f == 0):
            a = "%s%s%s" % (b, c, a)
        else:
            a = "%s%s%s" % (a, c, b)
        e = random.randint(0, 3)
        if (e == 2):
            a = '(' + a + ')'
        last = ''.join(re.split('\|', a))

    return a, last

