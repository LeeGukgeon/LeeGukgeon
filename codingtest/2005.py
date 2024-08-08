T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[1]
    nextarr=[]
    print(f'#{tc}')
    print(1)
    for i in range(1,N):
        nextarr.append(1)
        for j in range(len(arr)-1):
            nextarr.append(arr[j]+arr[j+1])
        nextarr.append(1)
        print(*nextarr)
        arr=nextarr
        nextarr=[]

