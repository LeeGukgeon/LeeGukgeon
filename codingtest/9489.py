T = int(input())
def get_max(arr):
    maxv=0
    temp=0
    for i in range(len(arr)):
        if arr[i]==0:
            if maxv<temp:
                maxv=temp
                temp=0
        if arr[i]==1:
            temp+=1
    if maxv<temp:
        maxv=temp
    return maxv

for test_case in range(1, T + 1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(N)]
    result=0
    for i in range(N):
        getmax=get_max(arr[i])
        if result<getmax:
            result=getmax
    for j in range(M):
        lst=[]
        for i in range(N):
            lst.append(arr[i][j])
        getmax=get_max(lst)
        if result<getmax:
            result=getmax
    print(f'#{test_case} {result}')
        

