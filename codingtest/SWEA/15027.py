T=int(input())
arr=[0]*400
arr[1]=1
arr[2]=3
def f(n):
    if arr[n]!=0:
        return arr[n]
    for i in range(3,n+1):
        arr[i]=arr[i-1]+2*arr[i-2]
    return arr[n]


for tc in range(1,T+1):
    N=int(input())
    N=N//10
    print(f'#{tc} {f(N)}')
