T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    MAP = [list(map(int,input().split())) for i in range(N)]
    PLUS = [(0,0)]
    MULTI = [(0,0)]
    for i in range(1,M):
        PLUS.append((0,i))
        PLUS.append((i,0))
        PLUS.append((0,-i))
        PLUS.append((-i,0))
    for i in range(1,M):
        MULTI.append((i,i))
        MULTI.append((i,-i))
        MULTI.append((-i,i))
        MULTI.append((-i,-i))
    print(PLUS)
    print(MULTI)
    temp = 0
    M1 = 0
    M2 = 0
    for i in range(N):
        for j in range(N):
            sum = 0
            for n,m in PLUS:
                if (0 <= i+n < N) and (0 <= j+m < N):
                    sum += MAP[i+n][j+m]
            M1 = max(M1,sum)
    for i in range(N)
        for j in range(N):
            sum = 0
            for n,m in MULTI:
                if (0 <= i+n < N) and (0 <= j+m < N):
                    sum += MAP[i+n][j+m]
            M2 = max(M2,sum)
    M=max(M1,M2)
    print(f'#{tc} {M}')



