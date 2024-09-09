def find(idx,total):
    global result
    if idx==N:
        if total==K:
            result+=1
        return
    if K<total:
        return
    if total+sum(sequence[idx:])<K:
        return
    find(idx+1,total+sequence[idx])
    find(idx+1,total)

T=int(input())
for tc in range(1,1+T):
    N,K=map(int,input().split())
    sequence=list(map(int,input().split()))
    result=0
    find(0,0)
    print(f'#{tc} {result}')