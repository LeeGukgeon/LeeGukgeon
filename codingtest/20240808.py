# s 문자열에 있는 중위표기를 후위표기로 바꿔서 return
s = '(61+5*(22-80)/2+11)'
def step1():
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []
    result = []
    for c in s:
        print(stack,result)
        if c.isdigit():
            result += c
        # elif c == '(':
        #     stack.append('(')
        elif c==')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            if stack and isp[stack[-1]] >= icp[c]:
                result += stack.pop()
            stack.append(c)

    while stack:
        result += stack.pop()

    return result

def cal(val1, val2, op):
    if op=='+':
        return val1 + val2
    if op == '-':
        return val2 - val1
    if op == '*':
        return val1 * val2
    if op == '/':
        return val2 / val1

# 후위표기식을 입력받아 연산결과를 return 한다.
def step2(s):
    stack = []
    for c in s:
        if c.isdigit():
            stack.append(int(c))
        else: # 연산자인 경우
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(cal(val1, val2, c))

    return stack.pop()


  # 6528-*2/+  => -9
# s = '2+3*4'
# s = '2*3-4*2'
# s = '2+3*4/5'
# s = '2+3*4+5'

post_order = step1()
print(post_order)
result = step2(post_order)
print(result)