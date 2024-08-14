T=int(input())
for tc in range(1,1+T):
    N,M=map(int,input().split())
    N_numbers=list(map(int,input().split()))
    print(f'#{tc} {N_numbers[M%N]}')
