T=int(input())
for tc in range(1,1+T):
    N,Q=map(int,input().split())
    L=[0]*Q
    R=[0]*Q
    for i in range(Q):
        L[i],R[i]=map(int,input().split())
    box=[0]*N
    for q in range(Q):
        for i in range(L[q]-1,R[q]):
            box[i]=q+1
    print(f'#{tc}',*box)