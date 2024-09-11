def merge_sort(arr):
    if len(arr)==1:
        return arr
    left=merge_sort(arr[:len(arr)//2])
    right=merge_sort(arr[len(arr)//2:])
    global cnt
    if right[-1]<left[-1]:
        cnt+=1
    lidx=0
    ridx=0
    result=[0]*(len(left)+len(right))
    while lidx<len(left) and ridx<len(right):
        if left[lidx]<right[ridx]:
            result[lidx+ridx]=left[lidx]
            lidx+=1
        else:
            result[lidx+ridx]=right[ridx]
            ridx+=1
    if lidx==len(left):
        for i in range(len(right)-ridx):
            result[lidx+ridx+i]=right[ridx+i]
    if ridx==len(right):
        for i in range(len(left)-lidx):
            result[lidx+ridx+i] =left[lidx+i]
    return result


T=int(input())
for tc in range(1,1+T):
    N=int(input())
    arr=list(map(int,input().split()))
    cnt=0
    arr=merge_sort(arr)
    print(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')