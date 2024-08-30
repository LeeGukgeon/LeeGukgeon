T=int(input())
for tc in range(1,1+T):
    Num=float(input())
    result=''
    idx=0
    while idx<13 and Num!=0:
        Num=Num*2
        if int(Num)==1:
            result+='1'
        else:
            result+='0'
        Num-=int(Num)
        idx+=1
    if len(result)==13:
        result='overflow'
    print(f'#{tc} {result}')