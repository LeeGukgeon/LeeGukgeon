for _ in range(10):
    N=int(input())
    arr=[list(map(int,input().split())) for i in range(100)]
    col=arr[99].index(2)
    row=99
    while row!=0:
        if 0<=col-1<100 and arr[row][col-1]==1:
            while 0<=col-1<100 and arr[row][col-1]!=0:
                col-=1
        if 0<=col+1<100 and arr[row][col+1]==1:
            while 0<=col+1<100 and arr[row][col+1]!=0:
                col+=1
        row-=1
    print(f'#{_+1} {col}')