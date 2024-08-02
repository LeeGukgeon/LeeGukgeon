T = 10
for tc in range(1,11):
    N = int(input())
    box = list(map(int,input().split()))
    for _ in range(N):
        max1 = box[0]
        min1 = box[0]
        max_idx = 0
        min_idx = 0
        for i in range(100):
            if box[i] <= min1:
                min1 = box[i]
                min_idx = i
            if max1 < box[i]:
                max1 = box[i]
                max_idx = i
        box[max_idx] -=1
        box[min_idx] +=1
        if max1-min1 <= 1:
            break
    max2 = max(box)
    min2 = min(box)
    print(f'#{tc} {max2-min2}')



