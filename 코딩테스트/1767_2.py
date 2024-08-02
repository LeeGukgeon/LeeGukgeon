T=int(input())
def solve(idx):
    pass
def check(x,y):
    result = [0,0,0,0]



for tc in range(1,1+T):
    N=int(input())
    Mac=[list(map(int,input().split())) for _ in range(N)]
    core_lst=[]
    for i in range(1,N-1):
        for j in range(1,N-1):
            if Mac[i][j]==1:
                core_lst.append([i,j])
    result=0


    print(f'#{tc} {result}')