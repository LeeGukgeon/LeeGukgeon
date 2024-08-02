T = int(input())
for test_case in range(1, T + 1):
    N= int(input())
    seq = input()
    max = 0
    temp = 0
    for c in seq:
        if c == '0':
            if max < temp:
                max = temp
                temp = 0
        if c == '1':
            temp+=1
    if max < temp:
        max = temp
    print(f'#{test_case} {max}')
