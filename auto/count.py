import re
from fractions import Fraction
from change import ifch

def changtorel(result): #结果假分数变成真分数
    if(re.match('(\d+)/(\d+)',result)):  #若找到分数
        f=Fraction(result)
        a=int(f.numerator)  #分子
        b=int(f.denominator) #分母
        if (a>b):
            c=a//b
            d=a%b
            result=str(c)+"'"+str(d)+'/'+str(b)
    return result

def compute(expression): #计算
    r=[]
    i=0
    while(i<len(expression)):
        ch=expression[i]
        if(not ifch(ch)):  #数字直接进栈
            r.append(ch)
        else:
            a=r.pop
            b=r.pop
            if(ch=='+'):
                result=str(Fraction(a)+Fraction(b))
                r.append(result)
            elif(ch=='-'):
                result=str(Fraction(b)-Fraction(a))
                r.append(result)
            elif(ch=='*'):
                result=str(Fraction(a)*Fraction(b))
                r.append(result)
            elif(ch=='÷'):
                result=str(Fraction(b)/Fraction(a))
                r.append(result)
        i+=1
        result=changtorel(r.pop())
        return result
                