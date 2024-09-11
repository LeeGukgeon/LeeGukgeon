def inorder(root):
    if 0 < len(connect[root]):
        inorder(int(connect[root][0]))
    print(tree[root-1][1],end='')
    if 1 < len(connect[root]):
        inorder(int(connect[root][1]))

for tc in range(1,11):
    N=int(input())
    tree=[input().split() for i in range(N)]
    connect=[tree[i][2:] for i in range(N)]
    connect.insert(0,[])
    print(f'#{tc} ',end='')
    inorder(1)
    print()
