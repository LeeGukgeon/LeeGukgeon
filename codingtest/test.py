T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    seconds = list(map(int, input().split()))
    seconds.sort()

    i = 0
    t = 0
    boong = 0
    flag = True
    while i < N:
        print(t, boong, seconds[i])
        t += M
        if seconds[i] < t and boong == 0:
            flag = False
            break
        else:
            boong += K
        boong -= 1
        i += 1


    if flag:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')