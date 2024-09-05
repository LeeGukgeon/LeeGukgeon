def isrunortri(lst):
    N=len(lst)
    lst.sort()
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if lst[i]==lst[j] and lst[j]==lst[k]:
                    return True
                if lst[i]+1==lst[j] and lst[j]+1==lst[k]:
                    return True
    return False

T=int(input())
for tc in range(1,1+T):
    arr=list(map(int,input().split()))
    first_player=[arr[2*i] for i in range(6)]
    second_player=[arr[2*i+1] for i in range(6)]
    result=0
    for i in range(4):
        if isrunortri(first_player[:3+i]):
            result=1
            break
        if isrunortri(second_player[:3+i]):
            result=2
            break
    print(f'#{tc} {result}')
