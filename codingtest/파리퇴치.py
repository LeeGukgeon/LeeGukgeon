T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    map = [list(map(int,input().split())) for _ in range(N)]
    max_value = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for n in range(M):
                for m in range(M):
                    temp += map[i+n][j+m]
            if max_value < temp:
                max_value = temp
    print(f'#{test_case} {max_value}')