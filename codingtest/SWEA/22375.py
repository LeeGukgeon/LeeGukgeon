T=int(input())
for tc in range(1,1+T):
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    AequalsB=[A[i]==B[i] for i in range(N)]
    result=0
    # print(AequalsB)
    for i in range(N-1):
        if AequalsB[i]!=AequalsB[i+1]:
            result+=1
    if A[0]!=B[0]:
        result+=1
    print(f'#{tc} {result}')