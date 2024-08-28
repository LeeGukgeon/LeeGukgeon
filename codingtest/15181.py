def sum_tree(node):
    if N<node:
        return 0
    if tree[node]!=0:
        return tree[node]
    return sum_tree(2*node)+sum_tree(2*node+1)

T=int(input())
for tc in range(1,1+T):
    N,M,L=map(int,input().split())
    tree=[0]*(N+1)
    for _ in range(M):
        i,x=map(int,input().split())
        tree[i]=x
    print(f'#{tc} {sum_tree(L)}')
