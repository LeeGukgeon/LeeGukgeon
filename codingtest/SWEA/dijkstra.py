N=10
adj_mat=[[0,4,6,1e9,1e9,1e9,1e9,1e9,1e9,1e9],
         [1e9,0,1e9,9,8,1e9,1e9,1e9,1e9,1e9],
         [1e9,3,0,1e9,2,3,1e9,1e9,1e9,1e9],
         [1e9,1e9,1e9,0,1e9,1e9,6,1e9,1e9,1e9],
         [1e9,1e9,1e9,2,0,1,3,7,1e9,1e9],
         [1e9,1e9,1e9,1e9,1e9,0,1e9,4,8,1e9],
         [1e9,1e9,1e9,1e9,1e9,1e9,0,1e9,1e9,13],
         [1e9,1e9,1e9,1e9,1e9,1e9,1e9,0,1e9,9],
         [1e9,1e9,1e9,1e9,1e9,1e9,1e9,1e9,0,4],
         [1e9,1e9,1e9,1e9,1e9,1e9,1e9,1e9,1e9,0]]

priority_que=[]
priority_que.append((0,0))
min_len=[1e9]*N
visited=[False]*N
while priority_que:
    minnode=priority_que.pop(0)
    min_len[minnode[0]]=minnode[1]
    visited[minnode[0]]=True
    for x in priority_que:
        if x[0]==minnode[0]:
            priority_que.remove(x)
    for j in range(N):
        if 0<adj_mat[minnode[0]][j]<1e8 and visited[j]==False:
            priority_que.append((j,minnode[1]+adj_mat[minnode[0]][j]))
    priority_que.sort(key=lambda x:x[1])
    print(priority_que)
print(min_len)


