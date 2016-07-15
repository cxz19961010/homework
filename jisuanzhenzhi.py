# -*- coding:utf-8 -*-
import string
import sys
fuhao=('~','&','|','^','->','<->')
fuhao2=('*','&','|','^','>','=')
fuhao2=list(fuhao2)

_DEBUG=False
def main():
    if _DEBUG==True:
        import pdb
        pdb.set_trace()
    INPUT=raw_input("请输入表达式，与使用&，或使用|，非使用～，异或使用^，蕴含使用->或>,等价使用<->或=,变量请用单个字母\n>> ")
    INPUT2=[]
    while 1:
        try:
            k=INPUT.index('<->')
            INPUT=list(INPUT)
            del INPUT[k+1]
            del INPUT[k+1]
            INPUT[k]='='
            inputs=''
            for i in INPUT:
                inputs=inputs+str(i)
            INPUT=inputs
        except:
            break

    while 1:
        try:
            k= INPUT.index('->')
            INPUT=list(INPUT)
            del INPUT[k+1]
            INPUT[k]='>'
            inputs=''
            for i in INPUT:
                inputs=inputs+str(i)
            INPUT=inputs
        except:
            break
            
    INPUT=list(INPUT)    
    for i in INPUT:
        if i!=' ':
            INPUT2.append(i)
    zhongzhui=[]
    i=0;
    while i<len(INPUT2):
        if INPUT2[i]>='0' and INPUT2[i]<='9':
            if INPUT2[i]=='0':
                zhongzhui.append(False)
            else:
                zhongzhui.append(True)
            i=i+1
        elif INPUT2[i]<='z' and INPUT2[i]>='a':

            zhongzhui.append(INPUT2[i])
            i=i+1

        else:
            if INPUT2[i]=='~':
                zhongzhui.append(True)
                zhongzhui.append('*')#增加一种新的双目运算符*来代替原单目运算符～(1*n)，其优先级最高
            else :
                zhongzhui.append(INPUT2[i])

            i=i+1
#以上是处理中缀表达式

    zhan=[]
    houzhui=[]
    for i in zhongzhui:
        if (i>='a' and i<='z')or (i==True or i==False):
            houzhui.append(i)
        elif i=='(':
            zhan.append(i)
        elif i==')':
            a=zhan.pop()
            while a!='(':
                houzhui.append(a)
                a=zhan.pop()
        elif zhan==[]:
            zhan.append(i)
        else :
            if zhan[len(zhan)-1]=='(' or zhan[len(zhan)-1]==')':
                zhan.append(i)
            else:
                orderi=fuhao2.index(i)
                ordera=fuhao2.index(zhan[len(zhan)-1])
                if orderi>ordera:
                    b=zhan.pop()
                    while b in fuhao2:
                        try:
                            houzhui.append(b)
                            b=zhan.pop()
                        except:
                            zhan.append(i)
                            break
                    if b=='(' or b==')':
                        zhan.append(b)
                        zhan.append(i)
                

                    
                else :
                    zhan.append(i)
    while 1:
        try:
            a=zhan.pop()
            houzhui.append(a)
        except:
            break

    bianliang=set()
    for i in houzhui:
        if i<='z' and i >='a':
            bianliang.add(i)
    bianliang=list(bianliang)#用来存储表达式中的变量
    bianliangzhi=[]#用来储存变量的值
    results=[]#用嵌套的列表来保存结果,其中元素均为字典
    xunhuan(0,houzhui,bianliang,bianliangzhi,results)
    dict_tihuan={}
    if len(sys.argv)>1 and sys.argv[1]=='-t':

        dict_tihuan=tihuan(INPUT2)

    printf(results,bianliang,INPUT2,dict_tihuan)
def calculator(houzhui_fuzhihou):
    
    result=[];
    for i in houzhui_fuzhihou:
        if i in {True,False}:
            result.append(i)
        elif i=='&':
            a1=result.pop()
            a2=result.pop()
            a=a1&a2
            result.append(a)
        elif i=='|':
            a1=result.pop()
            a2=result.pop()
            a=a1|a2
            result.append(a)
        elif i=='^':
            a1=result.pop()
            a2=result.pop()
            a=(a1+a2)%2
            result.append(a)
        elif i=='*':
            a1=result.pop()
            a2=result.pop()
            a=a1^a2
            result.append(a)
        elif i=='>':
            a1=result.pop()#第二个操作数
            a2=result.pop()#第一个操作数
            if(a2==True and a1==False):
                a=False
            else: 
                a=True
            result.append(a)
        elif i=='=':
            a1=result.pop()
            a2=result.pop()
            a=((a1 ^ a2)+1)%2
            result.append(a) 
    return result.pop()


def xunhuan(bianlianghao,houzhui,bianliang,bianliangzhi,results):
    if bianlianghao<len(bianliang):
        for i in {False,True}:
            bianliangzhi.append(i)
            xunhuan(bianlianghao+1,houzhui,bianliang,bianliangzhi,results)
            bianliangzhi.pop()
    else:
        value=dict(zip(bianliang,bianliangzhi))
       # houzhui_fuzhihou=copy.copy(houzhui)
        houzhui_fuzhihou=[]
        for j in houzhui:
            y=value.get(j,j)
            houzhui_fuzhihou.append(y)
        #houzhui_fuzhihou=[y for x in houzhui_fuzhihou and y=value.get(x,x)]
        key=calculator(houzhui_fuzhihou)
        value["result"]=key
        results.append(value)
        
def tihuan(INPUT2):
    print ("请以a：b格式输入要替换的字符，a为原字符，b为替换字符,输入一次空行结束输入")
    a=raw_input('>> ')
    dict_tihuan={}
    while a!='':
        try :
            a=a.split(':')
            dict_tihuan[a[0]]=a[1]
            a=raw_input('>> ')
        except:
            print 'input error'
    return dict_tihuan

            
def printf(results,bianliangbiao,INPUT2,dict_tihuan):

    for i in INPUT2:
        if (i<='z' and i>='a')or (i<='9'and i>='0'):
            print dict_tihuan.get(i,i),

        elif i=='~':
            print   '┐',
        elif i=='&':
            print '∧',
        elif i=='|':
            print '∨',
        elif i=='^':
            print '⊕',
        elif i=='=':
            print '↔',
        elif i=='>':
            print '→',
        elif i==True:
            print 1,
        elif i==False:
            print 0,
        elif i=='(' or i==')':
            print i,
    print ''
    for j in bianliangbiao:
        print "%4s"%(dict_tihuan.get(j,j)),
    print("   result")

    for i in results:
        for j in bianliangbiao:
            k=i.get(j)
            print "%4d"%k,
        k=i.get("result")
        print "%9d"%k

if __name__=="__main__":
    while 1:
        main()


