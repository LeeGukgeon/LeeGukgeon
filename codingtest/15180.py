def enq(key):
    global last
    last+=1
    tree[last]=key
    c=last
    p=c//2
    while 1<=p and tree[c]<tree[p]:
        tree[p],tree[c]=tree[c],tree[p]
        c=p
        p=p//2

T=int(input())
for tc in range(1,1+T):
    N=int(input())
    lst=list(map(int,input().split()))
    tree=[0]*(N+1)
    last=0
    for i in range(N):
        enq(lst[i])
    result=0
    while 0<last:
        result+=tree[last//2]
        last=last//2
    print(f'#{tc} {result}')

