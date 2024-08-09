N=12
M=3
lst=[i+1 for i in range(N)]
used=[0]*N
fcnt=0

def subset(i):

    if i==N and sum(used)!=M:
        pass
    elif sum(used)==M:
        global fcnt
        fcnt += 1
        temp=[]
        for i in range(N):
            if used[i]:
                temp.append(lst[i])
        print(temp)
    else:
        used[i]=1
        subset(i+1)
        used[i]=0
        subset(i+1)

subset(0)
print(fcnt)