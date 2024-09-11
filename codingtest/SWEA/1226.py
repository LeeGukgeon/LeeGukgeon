for tc in range(10):
    T=int(input())
    miro=[input() for i in range(16)]
    visited=[[False]*16 for i in range(16)]
    Q=[]
    dir=[(0,1),(1,0),(0,-1),(-1,0)]
    result=0
    for i in range(16):
        if '2' in miro[i]:
            start=[i,miro[i].index('2')]
    Q.append(start+[0])
    while Q:
        row,col,move=Q.pop(0)
        visited[row][col]=True
        if miro[row][col]=='3':
            result=1
            break
        for dr,dc in dir:
            if 0<=row+dr<16 and 0<=col+dc<16 and (miro[row+dr][col+dc]=='0' or miro[row+dr][col+dc]=='3') and not visited[row+dr][col+dc]:
                Q.append([row+dr,col+dc,move+1])
    print(f'#{T} {result}')










