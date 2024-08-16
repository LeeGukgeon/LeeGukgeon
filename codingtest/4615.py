T=int(input())
for tc in range(1,1+T):
    N,M=map(int,input().split())
    X=[0]*M
    Y=[0]*M
    C=[0]*M
    for i in range(M):
        X[i],Y[i],C[i]=map(int,input().split())
    dx=[0,0,1,1,1,-1,-1,-1]
    dy=[1,-1,1,0,-1,1,0,-1]
    board=[['N']*N for i in range(N)]
    board[N//2][N//2]='W'
    board[(N//2)-1][(N//2)-1]='W'
    board[(N//2)-1][N//2]='B'
    board[N//2][(N//2)-1]='B'
    for i in range(M):
        if C[i]==1:
            stone='B'
            oppostone='W'
        else:
            stone='W'
            oppostone='B'
        board[X[i] - 1][Y[i] - 1] = stone
        for j in range(8):
            K=1
            while 0<=X[i]-1+K*dx[j]<N and 0<=Y[i]-1+K*dy[j]<N:
                if board[X[i]-1+K*dx[j]][Y[i]-1+K*dy[j]]==oppostone:
                    K+=1
                else:
                    break
            if not (0<=X[i]-1+K*dx[j]<N and 0<=Y[i]-1+K*dy[j]<N):
                continue
            elif board[X[i]-1+K*dx[j]][Y[i]-1+K*dy[j]]==stone:
                for k in range(1,K):
                    board[X[i]-1+k*dx[j]][Y[i]-1+k*dy[j]]=stone
    Black_num=0
    White_num=0
    for i in range(N):
        for j in range(N):
            if board[i][j]=='B':
                Black_num+=1
            elif board[i][j]=='W':
                White_num+=1
    print(f'#{tc} {Black_num} {White_num}')



