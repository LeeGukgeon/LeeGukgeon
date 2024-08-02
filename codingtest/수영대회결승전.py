T = int(input())
ans = 0
DIR = [(1,0),(0,1),(-1,0),(0,-1),(0,0)]
queue = []
def BFS(map,x,y,X,Y,t):
    global queue
    # print(queue[0][1:])
    queue = queue[1:]
    global qunum
    qunum += 1
    global MAP
    global ans
    mapcopy = [arr[:] for arr in MAP]
    if x==X and y == Y:
        ans = t
        queue = []
        return -1
    if t%3 ==2:
        for i in range(N):
            for j in range(N):
                if MAP[i][j] == 2:
                    mapcopy[i][j] = 0
    else:
        for i in range(N):
            for j in range(N):
                if MAP[i][j] == 2:
                    mapcopy[i][j] = 1
    mapcopy[x][y] = 0
    for n,m in DIR:
        if (0 <= x+n <N) and (0 <= y+m < N) and mapcopy[x+n][y+m] == 0:
            if (map,x+n,y+m,X,Y,t+1) not in queue:
                queue.append((map,x+n,y+m,X,Y,t+1))
    
    return -1

for tc in range(1,T+1):
    N = int(input())
    MAP = [list(map(int,input().split())) for i in range(N)]
    x,y = map(int,input().split())
    X,Y = map(int,input().split())
    qunum = 0
    queue.append((MAP,x,y,X,Y,0))
    while queue:
        if queue == [] or qunum == 100000:
            break
        BFS(queue[0][0],queue[0][1],queue[0][2],queue[0][3],queue[0][4],queue[0][5])
        
    print(f'#{tc} {ans}')
    