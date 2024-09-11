T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    MAP = [list(input()) for i in range(N)]
    ZEROS = [[0 for i in range(N)] for i in range(N)]
    AROUND = [(0,0),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    for i in range(N):
        temp = 0
        for j in range(N):
            temp = 0
            for n,m in AROUND:
                if ((0<=i+n<N) and (0 <=j+m <N)):
                    if MAP[i+n][j+m] == "*":
                        temp += 1
            ZEROS[i][j] = temp
            temp = 0
    ans = 0
    def makeclick(i,j):
        for n,m in AROUND[1:]:
            if (0<=i+n<N) and (0 <=j+m <N) and ZEROS[i+n][j+m] == 0:
                ZEROS[i+n][j+m] = -1
                MAP[i+n][j+m] = -1
                makeclick(i+n,j+m)
            elif (0<=i+n<N) and (0 <=j+m <N) and MAP[i+n][j+m] == '.':
                MAP[i+n][j+m] = -1

    for i in range(N):
        for j in range(N):
            if ZEROS[i][j] == 0:
                MAP[i][j] = -1
                ZEROS[i][j] = -1
                ans +=1
                makeclick(i,j)
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == '.':
                ans += 1
    print(f'#{test_case} {ans}')
    
                
