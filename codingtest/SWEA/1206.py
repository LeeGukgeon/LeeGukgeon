for test_case in range(1, 11):
    N = int(input())
    dir = [-2,-1,1,2]
    Build = list(map(int,input().split()))
    result = 0
    for i in range(2,N-2):
        max = 0
        for j in dir:
            if max < Build[i+j]:
                max = Build[i+j]
        if max < Build[i]:
            result += Build[i] - max
    print(f'#{test_case} {result}')
