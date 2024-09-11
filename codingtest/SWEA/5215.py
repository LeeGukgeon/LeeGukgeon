def find(idx,sumT,sumK):
    # print(idx,sumT,sumK)
    global result
    if L<sumK:
        return
    if idx==N:
        if result<sumT:
            result=sumT
        return
    find(idx + 1, sumT + T[idx], sumK + K[idx])
    find(idx + 1, sumT, sumK)

T=int(input())
for tc in range(1,1+T):
    N,L=map(int,input().split())
    T=[0]*N
    K=[0]*N
    result=0
    for i in range(N):
        T[i],K[i]=map(int,input().split())
    find(0,0,0)
    print(f'#{tc} {result}')