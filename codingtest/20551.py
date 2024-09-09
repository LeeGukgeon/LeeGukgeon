def check(lst):
    A,B,C=map(int,lst)
    if A==0 or B<=1 or C<=2:
        return -1
    if A<B and B<C:
        return 0
    return max(0,B-(C-1))+max(0,A-(C-2))

T=int(input())
for tc in range(1,1+T):
    print(f'#{tc} {check(input().split())}')