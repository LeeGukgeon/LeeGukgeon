def find_min(c,probability):
    global result
    if c==N:
        if result<probability:
            result=probability
        return
    if probability<=result:
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            find_min(c+1,probability*percent[i][c]/100)
            visited[i]=False


T=int(input())
for tc in range(1,1+T):
    N=int(input())
    percent=[list(map(int,input().split())) for i in range(N)]
    visited=[False]*N
    result=0
    find_min(0,1)
    print(f'#{tc} {round(result*100,6):.6f}')