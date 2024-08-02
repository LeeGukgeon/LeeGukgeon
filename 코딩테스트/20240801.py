T = int(input())
for test_case in range(1, T + 1):
    N,M=map(int,input().split())
    arr = [list(map(int,input().split())) for i in range(N)]
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    result=0
    for i in range(N):
        for j in range(M):
            sum=0
            sum+=arr[i][j]
            for k in range(1,arr[i][j]+1):
                for p in range(4):
                    if (0<=i+k*dx[p]<N) and (0<=j+k*dy[p]<M):
                    	sum+=arr[i+k*dx[p]][j+k*dy[p]]
            if result < sum:
                result = sum
    print(f'#{test_case} {result}')