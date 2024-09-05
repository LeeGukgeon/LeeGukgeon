def check(target):
    if target not in A:
        return False
    left=0
    right=N-1
    middle=(left+right)//2
    dir=[]
    while A[middle]!=target:
        if A[middle]<target:
            left=middle+1
            dir.append(1)
        elif A[middle]>target:
            right=middle-1
            dir.append(-1)
        middle=(left+right)//2

    for i in range(len(dir)-1):
        if dir[i]==dir[i+1]:
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt=0
    for i in B:
        if check(i):
            cnt += 1
    print(f'#{tc} {cnt}')