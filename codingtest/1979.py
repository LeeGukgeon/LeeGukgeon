T = int(input())
for test_case in range(1, T + 1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for i in range(N)]
    result = 0

    for i in range(N):
        lst = [0]
        for j in range(N):
            if arr[i][j] ==0:
                lst.append(0)
            if arr[i][j] ==1:
                lst[-1]+=1
        result += lst.count(K)
    
    for j in range(N):
        lst = [0]
        for i in range(N):
            if arr[i][j] ==0:
                lst.append(0)
            if arr[i][j] ==1:
                lst[-1]+=1
        result += lst.count(K)
    print(f'#{test_case} {result}')