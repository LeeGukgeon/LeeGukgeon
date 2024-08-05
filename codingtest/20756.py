T=int(input())
def cal(res,sumv,n):
    if sumv+n in num_lst:
        return res*fac_lst[num_lst.index(sumv+n)]%1000000007
    temp=pow(sumv+n,1000000005,1000000007)
    num_lst.append(sumv+n)
    fac_lst.append(temp)
    result=res*temp%1000000007
    return result
def solve(arr,res,sumv):
    if arr==[]:
        return res
    sum=0
    for i in range(len(arr)):
        temp=arr[i]
        arr.pop(i)
        sum+=solve(arr,cal(res,sumv,temp),sumv+temp)
        arr.insert(i,temp) 
    sum=sum%1000000007
    return sum

def factorial(n):
    if n==1:
        return 1
    return (n*factorial(n-1))%1000000007

for tc in range(1,1+T):
    N=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    S=sum(arr)
    facsum=factorial(S)
    fac_lst=[]
    num_lst=[]
    result=0
    for i in range(N):
        temp=arr[i]
        arr.pop(i)
        result+=solve(arr,facsum,temp)
        arr.insert(i,temp)
    result=result%1000000007
    print(fac_lst)
    print(f'#{tc} {result}')

    