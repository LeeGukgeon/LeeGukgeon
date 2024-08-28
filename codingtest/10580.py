T=int(input())
for tc in range(1,1+T):
    N=int(input())
    A=[0]*N
    B=[0]*N
    for i in range(N):
        A[i],B[i]=map(int,input().split())
    result=0
    for i in range(1,N):
        for j in range(i):
            if (A[i]-A[j])*(B[i]-B[j])<0:
                result+=1
    print(f'#{tc} {result}')
