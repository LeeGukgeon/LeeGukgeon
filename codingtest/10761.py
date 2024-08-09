T=int(input())
for tc in range(1,1+T):
    mission=input().split()
    N=int(mission.pop(0))
    movingrobot=mission[0] #이전에 버튼을 누른 로봇과 같은 로봇인지 확인하기 위함.
    position={'O':1,'B':1} #로봇 위치
    t=0
    pretime=0  #다른 로봇이 바로 전에 버튼들을 누르는데 걸린 시간을 저장.
    for i in range(0,2*N,2): #입력값을 순회하면서
        if mission[i]==movingrobot: #이전에 버튼을 누른 로봇과 같은 로봇이면
            length=abs(int(position[mission[i]])-int(mission[i+1])) #움직일 거리를 계산하고
            t+=length+1 #움직이고 버튼까지 누르는데 걸리는 시간을 총 시간에 누적
            pretime+=length+1 # 프리타임에도 누적
            position[movingrobot]=mission[i+1] #현재 로봇의 포지션을 변경
        else:
            movingrobot=mission[i] #이전에 버튼을 누른 로봇과 다른 로봇이면
            length=abs(int(position[mission[i]])-int(mission[i+1])) #움직일 거리를 계산하고
            if pretime<=length: #움직일 거리만큼 미리 움직일 시간이 있었으면
                length=length-pretime #미리 움직인 거리만큼 빼주기
            else:
                length=0
            pretime=0 #초기화
            t += length+1 #움직이고 버튼까지 누르는데 걸리는 시간을 총 시간에 누적
            pretime += length+1 #프리타임에도 누적
            position[movingrobot] = mission[i + 1] #포지션 변경
    print(f'#{tc} {t}')

