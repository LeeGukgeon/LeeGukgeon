def run(idx,sum):
    if out[0]==True:
        return
    if total//2<sum:
        return
    if idx==-1:
        global result
        if total-2*sum<=1:
            out[0]=True
            result=total-2*sum
        elif total-2*sum<result:
            result=total-2*sum
    else:
        run(idx-1,sum+lst[idx])
        run(idx-1,sum)

N=int(input())
lst=[(i+1)**4 for i in range(N)]
out=[False]
total=N*(N+1)*(2*N+1)*(3*(N**2)+3*N-1)//30
result=10000000
run(N-1,0)
print(lst,total,out)
print(result)
