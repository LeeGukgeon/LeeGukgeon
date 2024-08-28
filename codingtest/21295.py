T=int(input())
square=[0]*100001
third=[0]*100001
forth=[0]*100001
for i in range(100001):
    square[i]=i**2
    third[i]=square[i]*i
    forth[i]=third[i]*i

for tc in range(1,201):
    N,K=map(int,input().split())
    temp=0
    result=''
    if K==1:
        if N%4==0:
            print('0 ',end='')
            print('1001'*(N//4))
        elif N%4==1:
            print('1 1',end='')
            print('1001' * (N // 4))
        elif N%4==2:
            print('1 01',end='')
            print('1001' * (N // 4))
        else:
            print('0 001', end='')
            print('1001' * (N // 4))
    elif K==2:
        for i in range(N):
            if 0<temp:
                result = '0' + result
                temp -= square[N - i]
            else:
                result = '1' + result
                temp += square[N-i]
    elif K==3:
        for i in range(N):
            if 0<temp:
                result = '0' + result
                temp -= third[N - i]
            else:
                result = '1' + result
                temp += third[N-i]
    elif K==4:
        for i in range(N):
            if 0<temp:
                result = '0' + result
                temp -= forth[N - i]
            else:
                result = '1' + result
                temp += forth[N-i]

    print(abs(temp),result)
for i in range(T-200):
    print('0 0')




