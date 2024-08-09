def runf(r,c):
    # print(maze)
    # print(r,c)
    if maze[r][c]=='3':
        global result
        result=1
    for dr,dc in dir:
        if 0<=r+dr<N and 0<=c+dc<N:
            if maze[r+dr][c+dc]=='0' or maze[r+dr][c+dc]=='3' :
                maze[r][c]='1'
                runf(r+dr,c+dc)

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    maze=[list(input()) for _ in range(N)]
    dir=[[1,0],[0,1],[-1,0],[0,-1]]
    r=0
    c=0
    result=0
    for i in range(N):
        for j in range(N):
            if maze[i][j]=='2':
                r=i
                c=j
    runf(r,c)
    print(f'#{tc} {result}')




