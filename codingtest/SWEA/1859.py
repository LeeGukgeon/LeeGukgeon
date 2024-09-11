T=int(input())
for tc in range(1,T+1):
    N=int(input())
    price=list(map(int,input().split()))
    tempmax = price[N-1]
    result=0
    for i in range(1,N):
        if tempmax<price[N-i-1]:
            tempmax=price[N-i-1]
        else:
            result+=(tempmax-price[N-i-1])
    print(f'#{tc} {result}')





