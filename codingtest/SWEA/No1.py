def ally(A,B):
    allyofA=[]
    allyofB=[]
    if A==B:
        return -1
    for i in range(len(allylst)):
        if A in allylst[i] and B in allylst[i]:
            return -1
        elif A in allylst[i]:
            allyofA=allylst[i]
        elif B in allylst[i]:
            allyofB=allylst[i]
    if allyofA==[]:
        allyofA.append(A)
    if allyofB==[]:
        allyofB.append(B)
    for i in range(len(allyofA)):
        for j in range(len(hostilelst)):
            if allyofA[i] in hostilelst[j]:
                if hostilelst[j][0] in allyofB or hostilelst[j][1] in allyofB:
                    return -2
    allylst.append(allyofA+allyofB)
    return 1
def attack(A,B,G):
    for i in range(len(allylst)):
        if A in allylst[i] and B in allylst[i]:
            return -1
    for i in range(N):
        for j in range(N):
            if Monarch[i][j]==A:
                Ai,Aj=i,j
    for i in range(N):
        for j in range(N):
            if Monarch[i][j]==B:
                Bi,Bj=i,j            
    if 1<abs(Ai-Bi) or 1<abs(Aj-Bj):
        return -2
    
def recruit(A,Num,Option):
    pass
def destroy():
    pass
T=int(input())
for tc in range(1,1+T):
    N=int(input())
    soldier=[list(map(int,input().split())) for i in range(N)]
    Monarch=[input().split() for i in range(N)]
    allylst=[]
    hostilelst=[]
