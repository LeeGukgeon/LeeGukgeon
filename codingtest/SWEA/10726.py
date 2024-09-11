T=int(input())
for tc in range(1,1+T):
    N,M=map(int,input().split())
    if ((1<<N)-1)&M==((1<<N)-1):
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')
