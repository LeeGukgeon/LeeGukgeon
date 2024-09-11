T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr=[list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M]==arr[i][j:j+M][::-1]:
                result=arr[i][j:j+M]
    trp=[[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            trp[i][j]=arr[j][i]
    for i in range(N):
        for j in range(N - M + 1):
            if trp[i][j:j + M] == trp[i][j:j + M][::-1]:
                result = trp[i][j:j + M]
    result=''.join(result)
    print(f'#{tc} {result}')
