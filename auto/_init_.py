import change
import count
import getauto

def main():
    print('给出输出最大的数')
    l=int(input())
    print('生成的题目数')
    m=int(input())
    question=[]
    for i in range(m):
        a=getauto.getExample(l)
        question.append(a[1])
    
    for q in range(len(question) ):
        print(question[q])

main()