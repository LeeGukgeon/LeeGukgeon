import sys
sys.stdin=open("input.txt","r")

def moving(arr):
    arr[0] += di[arr[2]]
    arr[1] += dj[arr[2]]


for tc in range(int(input())):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    energy = 0
    di, dj = [0, 0, -1, 1], [1, -1, 0, 0]

    while True:
        if all(atom[i][3] == 0 for i in range(N)):  # 모든 원자가 제거되었을 때 종료
            break
        cool = []
        for i in range(N):
            if atom[i][3] != 0:  # 움직일 수 있는 원자만
                moving(atom[i])
                # 경계를 벗어나면 원자 비활성화
                if atom[i][0] > 1000 or atom[i][0] < -1000 or atom[i][1] > 1000 or atom[i][1] < -1000:
                    atom[i][3] = 0
                else:
                    cool.append([i] + atom[i])  # cool에 (인덱스 + 원자 정보) 추가
        # print(cool)
        idx = set()  # 제거할 원자 인덱스 저장
        # 1. 같은 위치에 있을 때 제거
        for i in range(len(cool)):
            for j in range(i + 1, len(cool)):  # i와 j가 같은 값을 비교하는 것 방지
                if cool[i][1] == cool[j][1] and cool[i][2] == cool[j][2]:  # 좌표가 같은 경우
                    idx.add(cool[i][0])
                    idx.add(cool[j][0])
        # print(idx)
        for i in idx:
            energy += atom[i][3]  # 에너지를 더하고
            # print(energy)
            atom[i][3] = 0  # 원자를 비활성화

        # 2. 서로를 지나갈 때 제거
        for i in range(len(cool)):
            for j in range(i + 1, len(cool)):  # i와 j가 다른 원자를 비교하도록 수정
                # 상하 방향에서 지나가는 경우
                if (cool[i][2] == cool[j][2] and
                        ((cool[i][3], cool[j][3]) == (0, 1) and cool[i][1] == cool[j][1] + 1) or
                        ((cool[i][3], cool[j][3]) == (1, 0) and cool[i][1] == cool[j][1] - 1)):

                    idx.add(cool[i][0])
                    idx.add(cool[j][0])

                # 좌우 방향에서 지나가는 경우
                elif (cool[i][1] == cool[j][1] and
                      ((cool[i][3], cool[j][3]) == (2, 3) and cool[i][2] == cool[j][2] + 1) or
                      ((cool[i][3], cool[j][3]) == (3, 2) and cool[i][2] == cool[j][2] - 1)):

                    idx.add(cool[i][0])
                    idx.add(cool[j][0])

        # idx에 있는 원자의 에너지를 더하고 비활성화
        for i in idx:
            energy += atom[i][3]
            atom[i][3] = 0
    print(f'#{tc + 1} {energy}')