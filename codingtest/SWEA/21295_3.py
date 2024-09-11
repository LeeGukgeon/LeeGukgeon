def run(idx,sum):
    if out[0]==True:
        return
    if total//2<sum:
        return
    if idx==-1:
        global result
        if total-2*sum<=1:
            for i in range(N):
                result_used[i]=used[i]
            out[0]=True
            result=total-2*sum
        elif total-2*sum<result:
            for i in range(N):
                result_used[i]=used[i]
            result=total-2*sum
    else:
        used[idx]=True
        run(idx-1,sum+lst[idx])
        used[idx]=False
        run(idx-1,sum)
T=int(input())
for i in range(1,1+T):
    N=int(input())
    lst=[(i+1)**3 for i in range(N)]
    out=[False]
    used=[False]*N
    result_used=[False]*N
    total=(N*(N+1)//2)**2
    result=10000000
    run(N-1,0)
    print(lst,total,out)
    print(result)
    for i in range(len(result_used)):
        if result_used[i]:
            print(1,end='')
        else:
            print(0,end='')
    print()
    print()
#N*(N+1)*(2*N+1)*(3*(N**2)+3*N-1)//30