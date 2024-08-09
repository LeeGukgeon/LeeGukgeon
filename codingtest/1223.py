for tc in range(1,11):
    N=int(input())
    form=input()
    stack=[]
    result=[]
    for c in form:
        if c.isdigit():
            result.append(c)
        elif c=='+':
            while stack:
                result.append(stack.pop())
            stack.append(c)
        elif c=='*':
            while stack and stack[-1]=='*':
                result.append(stack.pop())
            stack.append(c)
    while stack:
        result.append(stack.pop())
    for c in result:
        if c.isdigit():
            stack.append(int(c))
        elif c=='+':
            v1=stack.pop()
            v2=stack.pop()
            stack.append(v1+v2)
        elif c=='*':
            v1=stack.pop()
            v2=stack.pop()
            stack.append(v1*v2)
    print(f'#{tc} {stack[0]}')
