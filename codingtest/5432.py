T=int(input())
for tc in range(1,T+1):
    parentheses=input()
    i=0
    cnt=0
    result=0
    while i<len(parentheses):
        if parentheses[i]=='(' and parentheses[i+1]==')':
            result+=cnt
            i+=2
        elif parentheses[i]=='(':
            cnt+=1
            i+=1
        elif parentheses[i]==')':
            cnt-=1
            i+=1
            result+=1
    print(f'#{tc} {result}')





