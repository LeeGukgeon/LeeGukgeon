T=int(input())
for tc in range(1,1+T):
    N=int(input())
    arr=list(map(int,input().split()))
    uphill=[0]*N
    uphill[0]=1
    for i in range(1,N):
        idx=-1
        maxv=0
        for j in range(i):
            if arr[j]<arr[i] and maxv<uphill[j]:
                idx=j
                maxv=uphill[j]
        if idx==-1:
            rightside=1
        else:
            rightside=uphill[idx]+1
        uphill[i]=rightside
    print(uphill)
    print(f'#{tc} {N-max(uphill)}')

