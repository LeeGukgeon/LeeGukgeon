T=int(input())
for tc in range(1,1+T):
    A,B,C,D=map(int,input().split())
    print(f'#{tc} {max(0,min(B,D)-max(A,C))}')
