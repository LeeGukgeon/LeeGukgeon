def find_min(c,total):
    if c==N:
        if total<result[0]:
            result[0]=total
        return
    if result[0]<total:
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            find_min(c+1,total+cost[i][c])
            visited[i]=False


T=int(input())
for tc in range(1,1+T):
    N=int(input())
    cost=[list(map(int,input().split())) for i in range(N)]
    visited=[False]*N
    result=[99999]
    find_min(0,0)
    print(f'#{tc} {result[0]}')
