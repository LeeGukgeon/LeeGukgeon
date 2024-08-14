T=int(input())
for tc in range(1,T+1):
    N=int(input())
    miro=[input() for i in range(N)]
    visited=[[False]*N for i in range(N)]
    Q=[]
    dir=[(0,1),(1,0),(0,-1),(-1,0)]
    result=0
    for i in range(N):
        if '2' in miro[i]:
            start=[i,miro[i].index('2')]
    Q.append(start+[0])
    while Q:
        row,col,move=Q.pop(0)
        visited[row][col]=True
        if miro[row][col]=='3':
            result=move-1
            break
        for dr,dc in dir:
            if 0<=row+dr<N and 0<=col+dc<N and (miro[row+dr][col+dc]=='0' or miro[row+dr][col+dc]=='3') and not visited[row+dr][col+dc]:
                Q.append([row+dr,col+dc,move+1])
    print(f'#{tc} {result}')










