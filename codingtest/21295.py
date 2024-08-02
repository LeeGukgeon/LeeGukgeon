def search(idx,s):
    global abox
    global bbox
    global result
    global result_s
    if idx==N:
        if abs(abox-bbox)<result:
            result=abs(abox-bbox)
            result_s= s
            return 0
        return 0
    next_idx=idx+1
    exc = search(next_idx,s+"0")
    abox+=oset[idx]
    inc = search(next_idx,s+"1")
    abox-=oset[idx]
    return min(inc,exc)
T=int(input())
for tc in range(1,1+T):
    N,K=map(int,input().split())
    oset = [0]*N
    for i in range(N):
        oset[i] = (i+1)**K
    abox=0
    bbox=0
    result = 5e10
    result_s=""
    search(0,"")
    print(f'#{tc} {result}')