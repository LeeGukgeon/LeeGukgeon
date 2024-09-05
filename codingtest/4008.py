def gukgeon(idx,postoper):
    if idx==N-1:
        # print(visited_operators,postoper)
        global bottom
        global top
        if postoper<bottom:
            bottom=postoper
        if top<postoper:
            top=postoper
        return
    for i in range(4):
        if counts[i]:
            counts[i]-=1
            # print(visited_operators,postoper)
            gukgeon(idx+1,cal(postoper,i,numbers[idx+1]))
            counts[i]+=1
def cal(n,i,m):
    if i==0:
        return n+m
    elif i==1:
        return n-m
    elif i==2:
        return n*m
    elif i==3:
        return int(n/m)

T=int(input())
for tc in range(1,1+T):
    N=int(input())
    counts=list(map(int,input().split()))
    numbers=list(map(int,input().split()))
    top=-100000000
    bottom=100000000
    gukgeon(0,numbers[0])
    print(f'#{tc} {top-bottom}')


