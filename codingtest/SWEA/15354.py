def visit(idx):
    if idx==N:
        result=0
        for i in range(N-1):
            result+=arr[visited[i]][visited[i+1]]
        result+=arr[visited[N-1]][visited[0]]
        return result
    result=100000
    for i in range(1,N):
        if i not in visited:
            visited[idx]=i
            temp=visit(idx+1)
            if temp<result:
                result=temp
            visited[idx]=0
    return result
T=int(input())
for tc in range(1,1+T):
    N=int(input())
    arr=[list(map(int,input().split())) for i in range(N)]
    visited=[-1]*N
    visited[0]=0
    print(f'#{tc} {visit(1)}')
