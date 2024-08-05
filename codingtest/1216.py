N=100
for tc in range(1,11):
    T=int(input())
    string=[list(input()) for _ in range(N)]
    maxv=0
    for i in range(N):
        for j in range(N-1):
            temp=1
            for k in range(1,min(j,N-1-j)+1):
                if string[i][j-k]==string[i][j+k]:
                    temp+=2
                else:
                    break
            if maxv < temp:
                maxv=temp
    for i in range(N):
        for j in range(N-1):
            temp=0
            for k in range(min(j+1,N-1-j)):
                if string[i][j-k]==string[i][j+k+1]:
                    temp+=2
                else:
                    break
            if maxv<temp:
                maxv=temp
    for i in range(N):
        for j in range(N):
            temp=1
            for k in range(1,1+min(j,N-1-j)):
                if string[j-k][i]==string[j+k][i]:
                    temp+=2
                else:
                    break
            if maxv < temp:
                maxv=temp
    for i in range(N):
        for j in range(N-1):
            temp=0
            for k in range(min(j+1,N-1-j)):
                if string[j-k][i]==string[j+k+1][i]:
                    temp+=2
                else:
                    break
            if maxv<temp:
                maxv=temp
    print(f'#{T} {maxv}')


