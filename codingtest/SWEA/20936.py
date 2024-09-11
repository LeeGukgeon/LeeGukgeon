T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    if arr==sorted(arr):
        print(0)
        print()
    else:
        complete=[0]*N
        notyet=True
        temp=0
        result=[]
        while notyet:
            idx=complete.index(0)
            if arr[idx]==idx+1:
                complete[idx]=1
            else:
                temp = arr[idx]
                result.append(idx+1)
                arr[idx]=0
                while idx+1!=temp:
                    tempidx=arr.index(idx+1)
                    arr[idx]=idx+1
                    complete[idx]=1
                    arr[tempidx]=0
                    result.append(tempidx+1)
                    idx=tempidx
                arr[idx]=idx+1
                temp=0
                result.append(N+1)
                complete[idx]=1
            if not 0 in complete:
                notyet=False
        print(len(result))
        print(*result)








    # if arr==sorted(arr):
    #     print('0')
    # else:
    #     arr=arr+[0]
    #     i=N
    #     arr[-1]=i
    #     i = arr.index(i)
    #     arr[i]=0
    #
    #     while :
    #         arr[]
    #         arr[arr.index(i)] = 0
    #         i=







