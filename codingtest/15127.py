T=int(input())
for tc in range(1,T+1):
    V,E=map(int,input().split())
    connect_lst=[[] for i in range(V+1)]
    for i in range(E):
        temp1,temp2=map(int,input().split())
        connect_lst[temp1].append(temp2)
        connect_lst[temp2].append(temp1)
    S,G=map(int,input().split())
    Q=[] #queue
    result=0
    visited=[False]*(V+1)
    Q.append([S,0])
    while Q:
        v=Q.pop(0)
        v1,v2=v[0],v[1]
        visited[v1]=True
        if v1==G:
            result=v2
            break
        for x in connect_lst[v1]:
            if not visited[x]:
                Q.append([x,v2+1])
    print(f'#{tc} {result}')