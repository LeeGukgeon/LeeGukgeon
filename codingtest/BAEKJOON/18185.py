N=int(input())
arr=list(map(int,input().split()))
pos=0
cost=0
while pos<N:
    if arr[pos]==0:
        pos+=1
        continue
    if pos<N-2 and arr[pos] and arr[pos+1] and arr[pos+2]:
        temp=min(arr[pos],arr[pos+1],arr[pos+2])
        cost+=7*temp
        arr[pos]-=temp
        arr[pos+1]-=temp
        arr[pos+2]-=temp
        continue
    elif pos<N-1 and arr[pos] and arr[pos+1]:
        temp=min(arr[pos],arr[pos+1])
        cost +=5* temp
        arr[pos] -= temp
        arr[pos+1]-=temp
        continue
    elif arr[pos]:
        cost+=3*arr[pos]
        arr[pos]=0
        pos+=1
        continue
print(cost)

