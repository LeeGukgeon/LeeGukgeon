T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int,input().split())) for i in range(9)]
    result = 1
    aset = {1,2,3,4,5,6,7,8,9}
    for i in range(9):
        lst = []
        for j in range(9):
            lst.append(arr[i][j])
        if set(lst) != aset:
            result = 0
    for j in range(9):
        lst=[]
        for i in range(9):
            lst.append(arr[i][j])
        if set(lst)!=aset:
            result=0
    for a in range(0,9,3):
        for b in range(0,9,3):
            lst = []
            for i in range(3):
                for j in range(3):
                    lst.append(arr[a+i][b+j])
            if set(lst)!=aset:
                result=0
    print(f'#{test_case} {result}')
