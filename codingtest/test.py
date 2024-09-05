def charge(now, gauge, cnt): # 현재정류장 위치, 게이지, 횟수
    # print(now,gauge,cnt)
    global min_cnt
    # 가지치기 - cnt가 min_cnt 이상이면 x
    if cnt >= min_cnt:
        return

    if now >= N-1: # 도착했으면 # == 아니고 >=
        min_cnt = min(min_cnt, cnt)
        return # 갱신해주고 리턴
    if gauge==0:
        return
    charge(now+1, oil[now+1], cnt+1) # 충전했음
    charge(now+1, gauge-1, cnt) # 충전 안했음, 게이지는 달아짐





T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    # print(lst) # [5, 2, 3, 1, 1]
    N = lst[0]
    oil = lst[1:]+[0]
    # print(oil) # [2, 3, 1, 1, 0]
    min_cnt = 21e8

    charge(0, oil[0], 0) # 충전하고 출발하므로 0
    print(f'#{tc} {min_cnt}')