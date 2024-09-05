T=int(input())
def gukgeon(idx,level):
    if level==N//2:
        global result
        synergy_A=0
        synergy_B=0
        for i in range(N):
            for j in range(N):
                if i!=j and ingradient_used[i]==True and ingradient_used[j]==True:
                    synergy_A+=synergy[i][j]
                elif i!=j and ingradient_used[i]==False and ingradient_used[j]==False:
                    synergy_B+=synergy[i][j]
        if abs(synergy_A-synergy_B)<result:
            result=abs(synergy_A-synergy_B)
        return
    if idx==N:
        return
    ingradient_used[idx]=True
    gukgeon(idx+1,level+1)
    ingradient_used[idx]=False
    gukgeon(idx+1,level)

for tc in range(1,1+T):
    N=int(input())
    synergy=[list(map(int,input().split())) for i in range(N)]
    ingradient_used=[False]*N
    ingradient_used[0]=True
    result=10000000
    gukgeon(1,1)
    print(f'#{tc} {result}')

