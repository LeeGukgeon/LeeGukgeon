T=int(input())
for tc in range(1,1+T):
    N,M=map(int,input().split())
    container=list(map(int,input().split()))
    weight=list(map(int,input().split()))
    container.sort(reverse=True)
    weight.sort(reverse=True)
    c_idx=0
    w_idx=0
    result=0
    while c_idx<N and w_idx<M:
        if container[c_idx]<=weight[w_idx]:
            result+=container[c_idx]
            c_idx+=1
            w_idx+=1
        else:
            c_idx+=1
    print(f'#{tc} {result}')