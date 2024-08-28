def postorder(node):
    if value[node].isdigit():
        return int(value[node])
    if value[node]=='+':
        return postorder(children[node][0])+postorder(children[node][1])
    if value[node]=='-':
        return postorder(children[node][0])-postorder(children[node][1])
    if value[node]=='*':
        return postorder(children[node][0])*postorder(children[node][1])
    if value[node]=='/':
        return postorder(children[node][0])/postorder(children[node][1])


for tc in range(1,11):
    N=int(input())
    children=[[0,0] for i in range(N+1)]
    value=[0 for i in range(N+1)]
    for i in range(1,N+1):
        nodeinfo=input().split()
        value[i] = nodeinfo[1]
        if not nodeinfo[1].isdigit():
            children[i]=[int(nodeinfo[2]),int(nodeinfo[3])]
    print(f'#{tc} {int(postorder(1))}')




