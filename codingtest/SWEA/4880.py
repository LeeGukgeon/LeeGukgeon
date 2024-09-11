T=int(input())
def game(v1,v2):
    h1=arr[v1]
    h2=arr[v2]
    if h1==h2:
        return v1
    elif h1-h2%3==1:
        return v1
    else: return v2
def win(a,s):
    half=((len(a)-1)//2)+1
    if len(a)==1:
        return s
    else:
        a1=a[:half]
        v1=win(a1,s)
        a2 = a[half:]
        v2=win(a2,s+half)
        return game(v1,v2)
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    pos=0
    print(f'#{tc} {win(arr,0)+1}')

