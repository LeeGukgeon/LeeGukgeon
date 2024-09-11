from collections import deque

T=int(input())
for tc in range(1,1+T):
    N,M=map(int,input().split())
    visited=[0]*1000001
    visited[N]=1
    result=21e8
    q = deque()
    q.append((N,0))
    while q:
        v, c = q.popleft()
        if v == M:
            result = c
            break
        choose = [v + 1, v - 1, v * 2, v - 10]
        for x in choose:
            if 0<x<=1000000 and not visited[x]:
                q.append((x,c+1))
                visited[x] = 1
    print(f'#{tc} {result}')

