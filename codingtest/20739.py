T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 가로 탐색

    max_v = 0

    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0 or j == (M-1):
                if cnt > max_v:
                    max_v = cnt
                cnt = 0

    # 세로 탐색
    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0 or i == (N-1):
                if cnt > max_v:
                    max_v = cnt
                cnt = 0


    print(max_v)
