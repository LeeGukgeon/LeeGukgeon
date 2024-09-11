# from pprint import pprint
T=int(input())
def descent(r,c,descent_len,construct,pre_dir):
    # pprint(height)
    # print(r,c,descent_len,pre_dir)
    global result
    # print(result)
    endbool=True
    for i in range(4):
        if 0<=r+dr[i]<N and 0<=c+dc[i]<N and height[r+dr[i]][c+dc[i]]<height[r][c]:
            endbool=False
            descent(r+dr[i],c+dc[i],descent_len+1,construct,i)
    for i in range(4):
        if 0<=r+dr[i]<N and 0<=c+dc[i]<N:
            if construct==1 and height[r][c]<=height[r+dr[i]][c+dc[i]]<height[r][c]+K and abs(i-pre_dir)!=2:
                endbool=False
                temp=height[r+dr[i]][c+dc[i]]
                height[r+dr[i]][c+dc[i]]=height[r][c]-1
                descent(r+dr[i],c+dc[i],descent_len+1,0,i)
                height[r + dr[i]][c + dc[i]]=temp

    if endbool:
        if result<descent_len:
            result=descent_len

for tc in range(1,1+T):
    N,K=map(int,input().split())
    height=[[]for i in range(N)]
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    for i in range(N):
        height[i]=list(map(int,input().split()))
    result=0
    maxv=0
    for i in range(N):
        if maxv<max(height[i]):
            maxv=max(height[i])
    for i in range(N):
        for j in range(N):
            if height[i][j]==maxv:
                descent(i,j,1,1,-100)
    print(f'#{tc} {result}')

