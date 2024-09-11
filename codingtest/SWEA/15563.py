T=int(input())
for tc in range(1,1+T):
    battery=list(map(int,input().split()))
    N=battery.pop(0)
    position=0
    cnt=-1
    while True:
        if N-1<=position:
            break
        capacity=battery[position]
        next_position=0
        move_max=0
        for i in range(1,capacity+1):
            if N-1<=position+i:
                next_position=N-1
                break
            temp=i+battery[position+i]
            if move_max<temp:
                move_max=temp
                next_position=position+i
        position=next_position
        cnt+=1
    print(f'#{tc} {cnt}')


