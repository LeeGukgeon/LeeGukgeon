T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnt = 0
    Color = [0] * N
    MAP = [[1] * 10 for i in range(10)]
    for i in range(N):
        Color[i] = list(map(int, input().split()))
    for c in Color:
        if c[4] == 1:
            for i in range(c[0], c[2] + 1):
                for j in range(c[1], c[3] + 1):
                    if MAP[i][j] % 2 == 1:
                        MAP[i][j] *= 2
        if c[4] == 2:
            for i in range(c[0], c[2] + 1):
                for j in range(c[1], c[3] + 1):
                    if MAP[i][j] % 3 != 0:
                        MAP[i][j] *= 3
    for row in MAP:
        for ele in row:
            if ele % 6 == 0:
                cnt += 1
    print(f'#{test_case} {cnt}')
