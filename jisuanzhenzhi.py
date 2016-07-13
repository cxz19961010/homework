import string
INPUT=raw_input("请输入表达式，与使用&，或使用|，非使用～，异或使用^，蕴含使用->,等价使用<->")
fuhao={'~','&','|','~','->','<->'}
fuhao2={'-','&','|','~','>','='}

while 1:
    try:
        k=INPUT.index('<->')
        INPUT=list(INPUT)
        del INPUT[k+1]
        del INPUT[k+2]
        INPUT[k]='='
        INPUT="".join(INPUT)
    except:
        break

while 1:
    try:
        k= INPUT.index('->')
        INPUT=list(INPUT)
        del INPUT[k+1]
        INPUT[k]='>'
        INPUT="".join(INPUT)
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
            zhongzhui.append(True)
        else
            zhongzhui.append(False)
        i=i+1
    else if INPUT2[i]<='z' and INPUT2[i]>='a':

        zhongzhui.append(INPUT2[i])
        i=i+1

    else
        if INPUT2[i]=='~':
            zhongzhui.append(True)
            zhongzhui.append(^)
        else :
            zhongzhui.append(INPUT2[i])
        i=i+1

zhan=[]
houzhui=[]
for i in zhongzhui[]:
    if (i>='a' and i<='z')or (i==True or i==False):
        houzhui.append[i]
    elif i=='(':
        zhan.append[i]
    elif i==')':
        a=zhan.pop();
        while a!='(':
            houzhui.append[a]
    elif zhan==[]:
        zhan.append[i]
    else :
        if zhan[len(zhan)-1]=='(' or zhan[len(zhan)-1]==')':
            zhan.append(i)
        else:
            orderi=fuhao2.index(i)
            ordera=fuhao2.index(zhan[len(zhan)-1])
            if orderi<ordera:
                b=zhan.pop
                while b!='(' and b!=')':
                    try:
                        houzhui.append[b]
                        b=zhan.pop
                    except:
                        zhan.append(i)
bianliang=set()
for i in houzhui:
    if i<='z' && i >='a':
        bianliang.add(i)
bianliang=list(bianliang)
bianliangzhi=[]
def calcularot(houzhui_fuzhihou):
    
    result=[];
    for i in houzhui_fuzhihou:
        if i in {True,False):
            result.append[i]
        else if i=='&':
            a1=

def xunhuan(bianlianghao):
    if bianlianghao<len(bianliang):
        for i in {False,True}:
            bianliangzhi.append(i)
            xunhuan(bianlianghao+1)
            bianliangzhi.pop()
    else:
        value=dict(zip(bianliang,bianliangzhi))
       # houzhui_fuzhihou=copy.copy(houzhui)
        houzhui_fuzhihou=[y for x in houzhui_fuzhihou and y=value.get(x,x)]
        
        calculator(houzhui_fuzhihou)

