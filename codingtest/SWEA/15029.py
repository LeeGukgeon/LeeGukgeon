T=int(input())
for tc in range(1,1+T):
    V,E=map(int,input().split())
    start=[0]*E
    end=[0]*E
    for i in range(E):
        start[i],end[i] = map(int,input().split())
    S,G=map(int,input().split())
    result=0
    stack=[]
    visited=[]
    stack.append(S)
    while stack:
        v=stack.pop()
        visited.append(v)
        if v==G:
            result=1
            break
        for i in range(E):
            if start[i]==v:
                if end[i] not in visited:
                    stack.append(end[i])
    print(f'#{tc} {result}')





