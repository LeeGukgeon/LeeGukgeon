T=int(input())
def rotate(num,dir):
    rotates=[0,0,0,0] #i+1 번째 자석의 회전 방향
    rotates[num]=dir  #회전시키는 자석의 회전 방향 입력
    if magnetism[2][2]!=magnetism[3][6]: #3번 4번 자석 동기화
        if rotates[2]!=0:
            rotates[3]=-rotates[2]
        if rotates[3]!=0:
            rotates[2]=-rotates[3]
    for i in range(3): # 1번2번, 2번3번,3번4번 자석 동기화
        if magnetism[i][2]!=magnetism[i+1][6]:
            if rotates[i] != 0:
                rotates[i+1] = -rotates[i]
            if rotates[i+1] != 0:
                rotates[i] = -rotates[i+1]
    if magnetism[0][2]!=magnetism[1][6]: #1번2번 동기화
        if rotates[0] != 0:
            rotates[1] = -rotates[0]
        if rotates[1] != 0:
            rotates[0] = -rotates[1]
    for i in range(4): # 회전시키기
        if rotates[i]==1:
            magnetism[i].insert(0,magnetism[i].pop())
        elif rotates[i]==-1:
            magnetism[i].append(magnetism[i].pop(0))

for tc in range(1,1+T):
    K=int(input())
    magnetism=[list(map(int,input().split())) for i in range(4)] #자석의 자성정보
    for _ in range(K): #K번
        magnet_num, direction =map(int,input().split())
        rotate(magnet_num-1,direction) #회전시킨다
    result=0
    for i in range(4): #결과 점수 계산
        if magnetism[i][0]==1:
            result+=2**(i)
    print(f'#{tc} {result}')

