from operator import itemgetter
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    pandp=[[i+1,i+1] for i in range(N)]
    swap=[]
    for _ in range(6):
        # print(pandp)
        # print(swap)
        # print()
        for i in range(N):
            pandp[i][1]+=arr[pandp[i][0]-1]
        temp=[]
        for i in range(N-1):
            for j in range(N-1):
                if pandp[j][1]>pandp[j+1][1]:
                    v=abs(arr[pandp[j][0]-1]-arr[pandp[j+1][0]-1])
                    if v==0:
                        continue
                    d=abs(pandp[j][1]-pandp[j+1][1])
                    t=1-(d/v)
                    temp.append([pandp[j][0],pandp[j+1][0],t])
                    # print([pandp[j][0],pandp[j+1][0],t])
                    pandp[j],pandp[j+1]=pandp[j+1],pandp[j]
        temp=sorted(temp,key=itemgetter(2))
        swap+=temp
        
    result = [10,0]
    for i in range(N):
        know = [0] * N
        know[i]=1
        for s in swap:
            if know[s[0]-1]==1:
                know[s[1]-1]=1
            if know[s[1]-1]==1:
                know[s[0]-1]=1
        if know.count(1)<result[0]:
            result[0]=know.count(1)
        if result[1]<know.count(1):
            result[1]=know.count(1)
    print(*result)





