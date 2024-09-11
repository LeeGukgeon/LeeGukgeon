for tc in range(1,11):
    N,startnode=map(int,input().split())
    pairs=list(map(int,input().split()))
    graph=[[] for i in range(101)]
    visited=[0]*101
    visited[startnode]=1
    for i in range(0,N,2):
        graph[pairs[i]].append(pairs[i+1])
    q=[]
    q.append((startnode,0))
    result=[0,0]
    while q:
        cur_node,cnt=q.pop(0)
        if result[0]<cnt:
            result[0]=cnt
            result[1]=cur_node
        elif result[0]==cnt and result[1]<cur_node:
            result[1]=cur_node
        for x in graph[cur_node]:
            if not visited[x]:
                visited[x]=1
                q.append((x,cnt+1))
    print(f'#{tc} {result[1]}')






