T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    arr=list(map(int,input().split()))
    result = []
    for _ in range(5):
        result.append(max(arr))
        arr.remove(max(arr))
        result.append(min(arr))
        arr.remove(min(arr))
    print(f'#{test_case}',*result)