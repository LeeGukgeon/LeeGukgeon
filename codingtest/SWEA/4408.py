T=int(input())
for tc in range(1,T+1):
    N=int(input())
    start=[0]*N
    end=[0]*N
    for i in range(N):
        start[i],end[i]=map(int,input().split())
        if end[i]<start[i]:
            start[i],end[i]=end[i],start[i]
    corridor=[0]*201
    for i in range(N):
        for j in range((start[i]+1)//2,((end[i]+1)//2)+1):
            corridor[j-1]+=1
    print(f'#{tc} {max(corridor)}')