N=10
lst=[1,2,3,4,5,6,7,8,9,10]
used=[0]*10
fcnt=0
def subset(i):
    global fcnt
    fcnt+=1
    if i==N:
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
