import math
def ways(arr,left):
    if arr==[]:
        return 1
    elif len(arr)==1:
        if arr[0]<=left:
            return 2
        else:
            return 1
    elif sum(arr)<=left:
        return (2**len(arr))*math.factorial(len(arr))
    else:
        result=0
        for i in range(len(arr)):
            temp=arr.pop(i)
            result+=ways(arr,left+temp)
            if temp<=left:
                result+=ways(arr,left-temp)
            arr.insert(i,temp)
        # print(arr,left,result)
        return result

T=int(input())
for tc in range(1,1+T):
    N=int(input())
    weight=list(map(int,input().split()))
    result=ways(weight,0)
    print(f'#{tc} {result}')