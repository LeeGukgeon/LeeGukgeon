def quick_sort(arr,s,e):
    if s==e:
        return
    if e<s:
        return
    p=arr[s]
    j=e
    for i in range(s+1,e+1):
        while p<arr[j]:
            j-=1
        if i<j and p<arr[i]:
            arr[i],arr[j]=arr[j],arr[i]
            j-=1
    arr[s],arr[j]=arr[j],arr[s]
    quick_sort(arr,s,j-1)
    quick_sort(arr,j+1,e)

arr=list(map(int,input().split()))
quick_sort(arr,0,len(arr)-1)
print(arr[500000])