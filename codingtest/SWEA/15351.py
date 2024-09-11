T=int(input())
def go(r,c,total):
    global result
    if result<total:
        return
    if r==N-1 and c==N-1:
        if total+arr[N-1][N-1]<result:
            result= total+arr[N-1][N-1]
    if r<N-1:
        go(r + 1, c, total + arr[r][c])
    if c<N-1:
        go(r,c+1,total+arr[r][c])

for tc in range(1,1+T):
    N=int(input())
    arr=[list(map(int,input().split())) for i in range(N)]
    result=10000
    go(0,0,0)
    print(f'#{tc} {result}')