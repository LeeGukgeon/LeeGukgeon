def find_min():
    return N-len(set(E).difference({0}))
T=int(input())
for tc in range(1,1+T):
    N,M=map(int,input().split())
    S=[0]*M
    E=[0]*M
    for i in range(M):
        S[i],E[i]=map(int,input().split())
    Q=int(input())
    result=[1]*Q
    for i in range(Q):
        q=int(input())
        S[q-1]=0
        E[q-1]=0
        result[i]=max(1,find_min())
    print(f'#{tc}',*result)
