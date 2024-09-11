T=int(input())
def traversal(root):
    global idx
    if root*2<=N:
        traversal(root*2)
    idx+=1
    arr[root]=idx
    if root*2+1<=N:
        traversal(root*2+1)

for tc in range(1,1+T):
    N=int(input())
    arr=[0]*(N+1)
    idx=0
    traversal(1)
    print(f'#{tc} {arr[1]} {arr[N//2]}')
