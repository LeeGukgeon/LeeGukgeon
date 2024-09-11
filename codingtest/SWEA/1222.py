def step1(s):
    return s[0]+s[2:]+'+'
for tc in range(1,11):
    N=int(input())
    exp=input()
    exp_t=step1(exp)
    stack=[]
    for c in exp_t:
        if c.isdigit():
            stack.append(int(c))
        elif c=='+':
            v1=stack.pop()
            v2=stack.pop()
            stack.append(v1+v2)
    print(f'#{tc} {stack[0]}')