T=int(input())
for tc in range(1,1+T):
    N,M=map(int,input().split())
    house=[list(map(int,input().split())) for i in range(N)]
    house_num=0
    house_idx=[]
    for i in range(N):
        for j in range(N):
            if house[i][j]==1:
                house_idx.append([i,j])
    house_num=len(house_idx)
    howfar=[[[0]*house_num for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            for p in range(house_num):
                howfar[i][j][p]=(abs(house_idx[p][0]-i)+abs(house_idx[p][1]-j))
    K=1
    while K*K+(K-1)*(K-1)<house_num*M:
        K+=1
    result=0
    for i in range(N):
        for j in range(N):
            for k in range(1,K+1):
                cnt = 0
                for p in range(house_num):
                    if howfar[i][j][p]<k:
                        cnt+=1
                if k*k+(k-1)*(k-1)<=M*cnt and result<cnt:
                    result=cnt
    print(f'#{tc} {result}')