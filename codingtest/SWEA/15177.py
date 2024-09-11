T=int(input())
def cal(idx):
    if memo[idx]!=0:
        return memo[idx]
    temp=0
    if idx not in parents:
        memo[idx]=1
        return 1
    for i in range(E):
        if parents[i]==idx:
            temp+=cal(children[i])
    memo[idx]=temp+1
    return temp+1

for tc in range(1,1+T):
    E,N=map(int,input().split())
    arr=list(map(int,input().split()))
    parents=[arr[2*i] for i in range(E)]
    children=[arr[2*i+1] for i in range(E)]
    memo=[0]*(E+2)
    print(f'#{tc} {cal(N)}')
    print(memo)






