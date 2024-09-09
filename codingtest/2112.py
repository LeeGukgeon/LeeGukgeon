import copy
def find_min(r,cnt):
    if check():
        global result
        if cnt<result:
            result=cnt
    if r==D or cnt==K:
        return

    find_min(r+1,cnt)
    film[r],templst1[r]=templst1[r],film[r]
    find_min(r+1,cnt+1)
    film[r], templst1[r] = templst1[r], film[r]
    film[r], templst2[r] = templst2[r], film[r]
    find_min(r+1,cnt+1)
    film[r], templst2[r] = templst2[r], film[r]

def check():
    for j in range(W):
        temp=1
        maxv=0
        for i in range(1,D):
            if film[i][j]==film[i][j-1]:
                temp+=1
            else:
                temp=1
            if maxv<temp:
                maxv=temp
        if maxv<K:
            return False
    return True


T=int(input())
for tc in range(1,1+T):
    D,W,K=map(int,input().split())
    film=[list(map(int,input().split())) for i in range(D)]
    templst1=[[0 for i in range(W)] for j in range(D)]
    templst2=[[1 for i in range(W)] for j in range(D)]
    result=100
    find_min()
    print(f'#{tc} {result}')
