T=int(input())
def issub(a,b):
    if b=='':
        return True
    else:
        if b[0] in a:
            return issub(a[a.index(b[0])+1:],a[1:])
        else:
            return False
for tc in range(1,T+1):
    S,A,B=input().split()
    result=0
    if issub(S,B) or issub(A,B):
        print(f'#{tc}',-1)
        continue

