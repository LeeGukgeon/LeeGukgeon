T=int(input())
for tc in range(1,T+1):
    sentence=input()
    check=[0]*len(sentence)
    result=1
    top=-1
    for s in sentence:
        if s not in ['(',')','{','}']:
            continue
        elif s=='(':
            top+=1
            check[top]=1
            print(check[:10])
        elif s=='{':
            top+=1
            check[top]=2
            print(check[:10])
        elif s==')':
            if check[top]==1:
                check[top]=0
                top-=1
                print(check[:10])
            else:
                result=0
                break
        elif s=='}':
            if check[top]==2:
                check[top]=0
                top-=1
                print(check[:10])
            else:
                result=0
                break
    if top!=-1:
        result=0
    print(f'#{tc} {result}')

