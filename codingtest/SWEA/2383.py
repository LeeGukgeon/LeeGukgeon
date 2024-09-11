import sys
sys.stdin = open("input.txt", "r")

def find(idx):
    if idx==len(people):
        # print(towhere)
        global seconds
        seconds=min(seconds,cal_time())
        return
    find(idx+1)
    towhere[idx]=1
    find(idx+1)
    towhere[idx]=0

def cal_time():
    time=0
    dtos_zero_chosen=[dtos_zero[i] for i in range(len(people)) if towhere[i]==0]
    dtos_one_chosen=[dtos_one[i] for i in range(len(people)) if towhere[i]==1]
    dtos_zero_chosen.sort()
    dtos_one_chosen.sort()
    # print(dtos_zero_chosen)
    # print(dtos_one_chosen)
    stair_zero=[]
    stair_one=[]
    idxzero=0
    idxone=0
    while idxzero<len(dtos_zero_chosen) or idxone<len(dtos_one_chosen):
        # print(time,idxzero,idxone,'time,idxzero,idxone')
        # print(stair_zero,'stair_zero')
        # print(stair_one,'stair_one')
        if time==100:
            break
        time+=1
        for i in range(3):
            if time in stair_zero:
                stair_zero.remove(time)
        for i in range(3):
            if time in stair_one:
                stair_one.remove(time)
        for i in range(idxzero,len(dtos_zero_chosen)):
            if dtos_zero_chosen[i]<=time and len(stair_zero)<3:
                stair_zero.append(time+stair[0][2])
                idxzero+=1
        for i in range(idxone,len(dtos_one_chosen)):
            if dtos_one_chosen[i]<=time and len(stair_one)<3:
                stair_one.append(time+ stair[1][2])
                idxone+=1
    if stair_zero:
        time=max(stair_zero)
    if stair_one:
        time=max(max(stair_one),time)
    # print(stair_zero,'최종 0')
    # print(stair_one,'최종 1')
    # print(time,'최종 타임')
    return time+1



T=int(input())
for tc in range(1,1+T):
    N=int(input())
    room=[list(map(int,input().split())) for _ in range(N)]
    people=[]
    stair=[]
    seconds=1e9
    for i in range(N):
        for j in range(N):
            if room[i][j]==1:
                people.append((i,j))
            if 1<room[i][j]:
                stair.append((i,j,room[i][j]))
    dtos_zero=[abs(people[i][0]-stair[0][0])+abs(people[i][1]-stair[0][1]) for i in range(len(people))]
    dtos_one=[abs(people[i][0]-stair[1][0])+abs(people[i][1]-stair[1][1]) for i in range(len(people))]
    towhere=[0]*len(people)
    find(0)
    print(f'#{tc} {seconds}')
