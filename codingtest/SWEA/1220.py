for tc in range(1,11):
    N=int(input())
    table=[list(map(int,input().split())) for i in range(N)]
    pre=0
    cnt=0
    for j in range(N):
        for i in range(N):
            if table[i][j]!=0:
                if pre==1 and table[i][j]==2:
                    cnt+=1
                pre=table[i][j]
        pre=0
    print(f'#{tc} {cnt}')