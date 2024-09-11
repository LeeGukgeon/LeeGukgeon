T=int(input())
for tc in range(1,1+T):
    N,M=map(int,input().split())
    pairs=list(map(int,input().split()))
    adj_lst=[[] for i in range(N+1)]
    for i in range(0,2*M,2):
        adj_lst[pairs[i]].append(pairs[i+1])
        adj_lst[pairs[i+1]].append(pairs[i])
    nodes=[False]*N
    teams=0
    while not all(nodes):
        teams+=1
        que=[]
        for i in range(N):
            if not nodes[i]:
                que.append(i+1)
                break
        while que:
            cur_node=que.pop(0)
            nodes[cur_node-1]=True
            for i in adj_lst[cur_node]:
                if not nodes[i-1]:
                    que.append(i)
    print(f'#{tc} {teams}')




