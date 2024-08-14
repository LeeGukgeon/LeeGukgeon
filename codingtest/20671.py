def sortfunc(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if not larger(arr[j][0],arr[j+1][0]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def larger(a,b):
    sa=str(a)
    sb=str(b)
    swap=False
    if len(sb)<len(sa):
        sa,sb=sb,sa
        swap=True
    la=len(sa)
    lb=len(sb)
    for i in range((lb//la)):
        for j in range(1,1+la):
            if sb=='':
                return False^swap
            if int(sa[:j])<int(sb[:j]):
                return True^swap
            if int(sa[:j])>int(sb[:j]):
                return False^swap
        sb=sb[la:]
    if sb=='':
        return False^swap
    return larger(sa,sb)^swap
precallst=[0]*3100
def precal():
    precallst[0]=1
    for i in range(1,3100):
        precallst[i]=precallst[i-1]*10%1000000007
precal()
def following(arr,n):
    currentidx=arr[0][1]
    templst=[[0,0] for i in range(n)]
    resultlst=[0]*3100
    for x in arr[1:]:
        if templst[x[1]][0]==0:
            templst[x[1]][0]=len(str(x[0]))
        else:
            templst[x[1]][1]=len(str(x[0]))
    templst.pop(currentidx)
    nextlst=[0]*3100
    resultlst[templst[0][0]]+=1
    resultlst[templst[0][1]]+=1
    for x in templst[1:]:
        for i in range(3100):
            if resultlst[i]!=0:
                nextlst[i+x[0]]+=resultlst[i]
        for i in range(3100):
            if resultlst[i]!=0:
                nextlst[i+x[1]]+=resultlst[i]
        resultlst=nextlst
        nextlst=[0]*3100
    result=0
    for i in range(3100):
        if resultlst[i]!=0:
            result=(result+resultlst[i]*precallst[i])%1000000007
    result=result*arr[0][0]%1000000007
    return result

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    a=[0]*N
    b=[0]*N
    for i in range(N):
        a[i],b[i]=map(int,input().split())
    for i in range(N):
        a[i]=(a[i],i)
    for i in range(N):
        b[i]=(b[i],i)  
    c=a+b
    c=sortfunc(c) 
    cd=[0]*len(c) #c 의 자리수 리스트
    for i in range(len(c)):
        cd[i]=len(str(c[i][0]))
    print(c)
    print(cd)
    result=0
    if N==1:
        result=a[0][0]+b[0][0]
    else:
        for i,x in enumerate(c):
            a=following(c[i:],N)
            print(a)
            result=(result+a)%1000000007
    print(f'#{tc} {result}')


