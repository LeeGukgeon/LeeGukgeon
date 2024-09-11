T=int(input())
for tc in range(1,1+T):
    N=int(input())
    start=[0]*N
    end=[0]*N
    for i in range(N):
        start[i],end[i]=map(int,input().split())
    container_included=[True]*N
    for i in range(N-1):
        for j in range(i+1,N):
            if start[i]<=start[j] and end[j]<=end[i]:
                container_included[i]=False
            elif start[j]<=start[i] and end[i]<=end[j]:
                container_included[j]=False
    booked_freight=[[] for i in range(24)]
    for i in range(N):
        for j in range(start[i],end[i]):
            if container_included[i]:
                booked_freight[j].append(i)
    idx=0
    while idx<24:
        if len(booked_freight[idx])<=1:
            idx+=1
            continue
        for x in booked_freight[idx]:
            if x!=booked_freight[idx-1][0]:
                container_included[x]=False
                for i in range(24):
                    if x in booked_freight[i]:
                        booked_freight[i].remove(x)
        idx+=1
    print(f'#{tc} {container_included.count(True)}')