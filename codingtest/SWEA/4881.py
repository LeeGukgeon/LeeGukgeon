T=int(input())
def permutation(i,s):
    global result
    if i==N:
        if s<result:
            result=s
            print(c, result)
    elif s>result:
        print('pass')
        pass
    else:
        for j in range(N):
            if not used[j]:
                c[i]=j
                used[j]=1
                permutation(i+1,s+arr[i][j])
                used[j]=0

for tc in range(1,1+T):
    N=int(input())
    arr=[list(map(int,input().split())) for i in range(N)]
    result=100
    lst = [i + 1 for i in range(N)]
    used = [0] * N
    c = [-1] * N
    permutation(0,0)
    print(f'#{tc} {result}')



