T=int(input())
for tc in range(1,T+1):
    N,A,B=map(int,input().split())
    result=0
    while 0<N:
        print(N)
        rest=N%B
        if rest==0:
            mogs = N // B
            result+=(B**2)*(mogs*(mogs-1)//2)
            N=0
        elif A<=rest:
            result+=(rest)*(N-rest)
            mogs=N//B
            result+=(B**2)*(mogs*(mogs-1)//2)
            N=0
        elif rest<A:
            result+=A*(N-A)
            N=N-A
    if N<0:
        result=-1
    print(f'#{tc} {result}')





