T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    arr=[[0]*N for _ in range(N)]
    arr[0][0]=1
    dir=0
    dxdy =[(0,1),(1,0),(0,-1),(-1,0)]
    now=[0,0]
    for i in range(2,N**2+1):
        if not (0<=now[0]+dxdy[dir][0]<N and 0<=now[1]+dxdy[dir][1]<N):
            dir=(dir+1)%4

        elif arr[now[0]+dxdy[dir][0]][now[1]+dxdy[dir][1]]!=0:
            dir=(dir+1)%4
        arr[now[0]+dxdy[dir][0]][now[1]+dxdy[dir][1]]=i
        now=[now[0]+dxdy[dir][0],now[1]+dxdy[dir][1]]
    print(f'#{test_case}')
    for i in range(N):
        print(*arr[i])  
