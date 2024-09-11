T=int(input())
for tc in range(1,T+1):
    xpr=input().split()
    stack=[]
    for i in range(len(xpr)):
        if xpr[i].isdigit():
            stack.append(int(xpr[i]))
        elif xpr[i]=='+':
            if len(stack)<2:
                print(f'#{tc} error')
                break
            v1=stack.pop()
            v2=stack.pop()
            stack.append(v1+v2)
        elif xpr[i]=='-':
            if len(stack)<2:
                print(f'#{tc} error')
                break
            v1=stack.pop()
            v2=stack.pop()
            stack.append(v2-v1)
        elif xpr[i]=='*':
            if len(stack)<2:
                print(f'#{tc} error')
                break
            v1=stack.pop()
            v2=stack.pop()
            stack.append(v1*v2)
        elif xpr[i]=='/':
            if len(stack)<2:
                print(f'#{tc} error')
                break
            v1=stack.pop()
            v2=stack.pop()
            stack.append(v2//v1)
        elif xpr[i]=='.':
            if len(stack)!=1:
                print(f'#{tc} error')
            else:
                print(f'#{tc} {stack[0]}')