T=int(input())
for tc in range(1,1+T):
    N,M= map(int,input().split())
    arr=[input() for i in range(N)]
    result=10000
    for i in range(1,N-1):
        for j in range(i+1,N):
            temp=0
            for t in range(N):
                if t<i:
                    temp+=M-arr[t].count('W')
                elif i<=t<j:
                    temp+=M-arr[t].count('B')
                else:
                    temp+=M-arr[t].count('R')
            if temp<result:
                result=temp
    print(f'#{tc} {result}')
