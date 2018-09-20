def ifch(a):  #判断是否为运算符
    if(a=='+' or a=='-' or a=='*' or a=='÷' or a=='(' or a==')'):
        return True

def getvalue(op,flag): #判断权值的大小
    if(op=='+' or op=='-'):
        if flag:
            return 3
        else:
            return 2
    elif (op=='*' or op=='÷'):
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
    last=[]
    first=[]
    i=0
    while(i<len(expression)):
        if (expression[i]=='|'):  #是数字就直接压进ex栈
            index=expression.find('|',i+1)
            num=expression[i+1:index]
            last.append(num)
            i=index+1
        elif(ifch(expression[i])): #运算符判断优先级 
            if (first==[]):
                first.append(expression[i])
                i+=1
            else:
                if (expression[i]==')') :#若遇到右括号，则一直出栈直到遇到左括号
                    while(expression[i]==')' and first[len(first)-1]is not '('):
                        last.append(first[len(first)-1])
                        first.pop()
                    first.pop()
                    i+=1
                elif(getvalue(expression[i],0) > getvalue(first[len(first)-1],1)): #若优先级大于栈顶元素，则入栈
                    first.append(expression[i])
                    i+=1
                else:
                    while (not first==[] and getvalue(expression[i],0) <= getvalue(first[len(first)-1],1)):#优先级小于等于栈顶元素则输出栈顶元素
                        last.append(first[len(first)-1])
                        first.pop()
                    first.append(expression[i])
                    i+=1
    while(not first==[]):
        last.append(first[len(first)-1])
        first.pop()
    return last

            
