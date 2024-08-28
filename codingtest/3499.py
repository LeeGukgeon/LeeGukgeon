T=int(input())
for tc in range(1,1+T):
    N=int(input())
    arr=input().split()
    newarr=[0]*N
    for i in range(N):
        if i%2==1:
            newarr[i]=arr[(N+1)//2+i//2]
        else:
            newarr[i]=arr[i//2]
    print(f'#{tc}',*newarr)