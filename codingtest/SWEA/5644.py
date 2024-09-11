from pprint import pprint
T=int(input())
for tc in range(1,1+T):
    M,A=map(int,input().split())
    Amove=list(map(int,input().split()))
    Bmove=list(map(int,input().split()))
    charger=[list(map(int,input().split())) for i in range(A)]
    charger_map=[[[] for i in range(10)] for i in range(10)]
    for i in range(10):
        for j in range(10):
            for idx,x in enumerate(charger):
                if abs(j-(x[0]-1))+abs(i-(x[1]-1))<=x[2]:
                    charger_map[i][j].append(idx)
    # print(charger)
    # pprint(charger_map)
    Aposition=[0,0]
    Bposition=[9,9]
    dir=[[0,0],[-1,0],[0,1],[1,0],[0,-1]]
    result=0
    for t in range(M+1):

        Acan=charger_map[Aposition[0]][Aposition[1]]
        Bcan=charger_map[Bposition[0]][Bposition[1]]
        Acharge=0
        Achargeidx=-1
        Bcharge=0
        Bchargeidx=-1
        secondmax =0
        if Acan:
            for idx in Acan:
                if Acharge<charger[idx][3]:
                    Acharge=charger[idx][3]
                    Achargeidx=idx
        if Bcan:
            for idx in Bcan:
                if Bcharge<charger[idx][3]:
                    Bcharge=charger[idx][3]
                    Bchargeidx=idx
        if Achargeidx==Bchargeidx and Achargeidx!=-1:
            for idx in Acan+Bcan:
                if idx!=Achargeidx and secondmax<charger[idx][3]:
                    secondmax=charger[idx][3]
            Bcharge=secondmax
        result+=Acharge+Bcharge
        # print(Acharge, Bcharge,result,Aposition,Bposition)
        if t<M:
            for i in range(2):
                Aposition[i]+=dir[Amove[t]][i]
                Bposition[i]+=dir[Bmove[t]][i]
    # pprint(charger_map)
    print(f'#{tc} {result}')
