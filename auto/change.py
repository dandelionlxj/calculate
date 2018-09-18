def ifch(a):  #判断是否为运算符
    if(a=='+' or a=='-' or a=='*' or a=='*' or a=='(' or a==')'):
        return True

def getvalue(op,flag): #判断权值的大小
    if(op=='+' or op=='-'):
        if flag:
            return 3
        else:
            return 2
    elif (op=='*' or op=='*'):
        if flag:
            return 6
        else:
            return 5
    elif(op=='('):
        if flag:
            return 1
        else:
            return 6
    elif (op==')'):
        if flag:
            return 6
        else :
            return 1 

def mid_after(expression): #中缀转后缀
    ex=[]
    now=[]
    i=0
    while(i<len(expression)):
        if (expression[i]=='|'):  #是数字就直接压进ex栈
            index=expression.find('|',i+1)
            num=expression[i+1:index]
            ex.append(num)
            i=index+1
        elif(ifch(expression[i])): #运算符判断优先级 
            if (now==[]):
                now.append(expression[i])
                i+=1
            else:
                if (expression[i]==')') :#若遇到右括号，则一直出栈直到遇到左括号
                    while(expression[i]==')' and now[len(now)-1]is not '('):
                        ex.append(now[len(now)-1])
                        now.pop()
                    now.pop()
                    i+=1
                

            
