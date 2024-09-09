def find_max(r,c,path,kindofdessert,rotate):
    pathlen=len(path)
    if pathlen==2*N or rotate==4:
        return
    if 4<pathlen and (r,c)==path[0] and rotate==3:
        global result
        if result<pathlen-1:
            result=pathlen-1
    if pathlen==1:
        lastdir=0
    else:
        lastdir=(path[-1][0]-path[-2][0],path[-1][1]-path[-2][1])
    dir=[(1,1),(1,-1),(-1,-1),(-1,1)]
    for i in range(4):
        dr=dir[i][0]
        dc=dir[i][1]
        if 0<=r+dr<N and 0<=c+dc<N:
            if (arr[r+dr][c+dc] not in kindofdessert) or (r+dr,c+dc)==path[0]:
                if lastdir:
                    if dir[(i-1)%4]==lastdir:
                        find_max(r+dr,c+dc,path+[(r+dr,c+dc)],kindofdessert+[arr[r+dr][c+dc]],rotate+1)
                    elif dir[i]==lastdir:
                        find_max(r+dr,c+dc,path+[(r+dr,c+dc)],kindofdessert+[arr[r+dr][c+dc]],rotate)
                else:
                    find_max(r+dr,c+dc,path+[(r+dr,c+dc)],kindofdessert+[arr[r+dr][c+dc]],rotate)

T=int(input())
for tc in range(1,1+T):
    N=int(input())
    arr=[list(map(int,input().split())) for i in range(N)]
    result=-1
    for i in range(N):
        for j in range(N):
            find_max(i,j,[(i,j)],[arr[i][j]],0)
    print(f'#{tc} {result}')