T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    C=list(map(int,input().split()))
    que=[i for i in range(N)]
    i=0
    order=N
    boolean=True
    latest=0
    while boolean:
        temp = False
        for x in C:
            temp=temp or x
        boolean=temp
        if not boolean:
            break
        if que[i]==-1:
            pass
        elif 1<C[que[i]]:
            C[que[i]]=C[que[i]]//2
        elif C[que[i]]==1 and order<M:
            latest=que[i]
            C[que[i]]=0
            que[i]=order
            order+=1
        elif C[que[i]]==1 and order==M:
            latest=que[i]
            C[que[i]] = 0
            que[i]=-1
        i = (i + 1) % N
    print(f'#{tc} {latest+1}')









