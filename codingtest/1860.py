T=int(input())
for tc in range(1,T+1):
    N,M,K=map(int,input().split())
    cus=list(map(int,input().split()))
    cus.sort()
    result=0
    for i in range(N):
        bread=K*(cus[i]//M)
        if bread<(i+1):
            result=1
    if result==0:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')

