T=int(input())
for tc in range(1,1+T):
    N=int(input())
    room=[list(map(int,input().split())) for i in range(N)]
    connected=[0]*(N**2)
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]
    for r in range(N):
        for c in range(N):
            temp=False
            for i in range(4):
                if 0<=r+dr[i]<N and 0<=c+dc[i]<N:
                    if room[r][c]+1==room[r+dr[i]][c+dc[i]]:
                        temp=True
            connected[room[r][c]-1]=temp
    move=1
    result=0
    result_room=0
    for i in range(N**2-1,-1,-1):
        if connected[i]:
            move+=1
        else:
            move=1
        if result<=move:
            result=move
            result_room=i+1
    print(f'#{tc} {result_room} {result}')



