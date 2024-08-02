for tc in range(1, 11):
    arr = [list(map(int, input().split())) for _ in range(100)]
    max = arr[0][0]
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[i][j]
        if max < temp:
            max = temp
    for j in range(100):
        temp = 0
        for i in range(100):
            temp += arr[i][j]
        if max < temp:
            max = temp
    temp = 0
    for i in range(100):
        temp += arr[i][i]
    if max < temp:
        max = temp
    temp=0
    for i in range(100):
        temp += arr[i][1 - i]
    if max < temp:
        max = temp
    print(f'#{tc} {max}')
