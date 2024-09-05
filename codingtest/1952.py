def find_min(month,total):
    global result
    if month>=12:
        if total<result:
            result=total
        return
    if result<total:
        return
    if use[month]:
        find_min(month+3,total+cost[2])
        find_min(month+1,total+cost[1])
        find_min(month+1,total+use[month]*cost[0])
    else:
        find_min(month+1,total)

T=int(input())
for tc in range(1,1+T):
    cost=list(map(int,input().split()))
    use=list(map(int,input().split()))
    result=cost[3]
    find_min(0,0)
    print(f'#{tc} {result}')