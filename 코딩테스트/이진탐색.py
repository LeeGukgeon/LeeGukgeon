T = int(input())
for test_case in range(1, T + 1):
    P,A,B=map(int,input().split())
    la=1
    lb=1
    ca=int((1+P)/2)
    cb=int((1+P)/2)
    ra=P
    rb=P
    acnt=1
    bcnt=1
    result =0
    while ca!=A:
        acnt+=1
        if A<ca:
            ra=ca
            ca=int((la+ra)/2)
        else:
            la=ca
            ca=int((la+ra)/2)

    while cb!=B:
        bcnt+=1
        if B<cb:
            rb=cb
            cb=int((lb+rb)/2)
        else:
            lb=cb
            cb=int((lb+rb)/2)
    if acnt < bcnt:
        result ='A'
    elif bcnt < acnt:
        result ='B'
    print(f'#{test_case} {result}')

        

