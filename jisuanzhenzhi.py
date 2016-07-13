import string
INPUT=raw_input("请输入表达式，与使用&，或使用|，非使用～，异或使用^，蕴含使用->,等价使用<->")
fuhao={'~','&','|','~','->','<->'}

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
        i=i+1
        nu_str=[]
        nu_str.append(INPUT2[i])
        while INPUT2[i]>='0' and INPUT2[i]<='9' and i<length:
            nu_str.append(INPUT2[i])
            
        nu=string.atof(nu_str)
        zhongzhui.append(nu)
    else
        zhongzhui.append(INPUT2[i])

        

