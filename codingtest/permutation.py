N=7
M=4
lst=[i+1 for i in range(N)]
used=[0]*N
c=[-1]*M
cnt=0
def permutation(i):
    if i==M:
        global cnt
        cnt+=1
        print(c)
        # temp=[]
        # for j in range(N):
        #     if used[j]==1:
        #         temp.append(lst[j])
        # print(temp)
    else:
        for j in range(N):
            if not used[j]:
                c[i]=j
                used[j]=1
                permutation(i+1)
                used[j]=0
permutation(0)
print(cnt)