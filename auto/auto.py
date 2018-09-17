# import math
# from fractions import Fraction

# def zhenfenshu(a):
#     x=int(math.floor(a))
#     z=int((a-x)*10)
#     if z==0:
#         b=a
#     else:
#         y=Fraction(z,10)
#         b=str(x)+"'"+str(y)
#     return (b)

# print(zhenfenshu(3/4))
from random import randint
def macbys(x,y): #最大公约数
    if x==y:
        return x
    if x>y:
        if x%y==0: return y
    else :
        if y%x ==0: return x
    
    temp=y
    while (x%y) !=0:
        temp=x%y
        x,y=y,temp     
    return temp

def mingbs(x,y): #最小公倍数
    if x==y:
        return x 
    if x%y==0: return x
    if y%x==0: return y

    temp=macbys(x,y)
    return x*y/temp

def randomFraction(range):  #生成随机真分数
    a=randint(1,range)
    b=randint(1,a-1)
    if randint(0,1)==0:
        return str(b) + '/' +str(a)
    else:
        c=randint(1,range)
        return str(c) +"'"+str(b) + '/' +str(a)

def fractionadd(a,b):  #分数相加
    if a[1]=b[1]:
        return [a[0]+b[0],a[1]]
    mcd=mingbs(a[1],b[1])
    x=mcd/a[1]
    y=mcd/b[1]
    return [a[0]*x+b[0]*y,mcd]

def fractionsubtraction(a,b): #分数相减
     if a[1]=b[1]:
        return [a[0]+b[0],a[1]]
    mcd=mingbs(a[1],b[1])
    x=mcd/a[1]
    y=mcd/b[1]
    return [a[0]*x-b[0]*y,mcd]

def fractionmutiply(a,b): #分数相乘
    return [a[0]*b[0],a[1]*b[1]]

def fractiondivision(a,b): #分数相除
    return [a[0]*b[1],a[1]*b[0]]

