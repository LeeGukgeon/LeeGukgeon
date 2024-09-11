T=int(input())
dec={'0001101':'0','0011001':'1','0010011':'2','0111101':'3','0100011':'4','0110001':'5','0101111':'6','0111011':'7','0110111':'8','0001011':'9'}
for tc in range(1,1+T):
    N,M=map(int,input().split())
    arr=['']*N
    for i in range(N):
        arr[i]=input()
    for i in range(N*M):
        m=i//N
        n=i%N
        if arr[n][M-1-m]=='1':
            break
    code=arr[n][M-m-56:M-m]
    result=''
    for i in range(0,56,7):
        result+=dec[code[i:i+7]]
    verify=0
    for i in range(8):
        if i%2==0:
            verify+=int(result[i])*3
        else:
            verify+=int(result[i])
    if verify%10==0:
        sumv=0
        for i in range(8):
            sumv+=int(result[i])
        print(f'#{tc} {sumv}')
    else:
        print(f'#{tc} 0')


