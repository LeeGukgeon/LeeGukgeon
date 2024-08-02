num = 112345
def isrun(a,b,c):
    if a==b and b==c:
        return True
    else:
        return False
def istripet(a,b,c):
    if a!=b and a!=c and b!=c and max((a,b,c))-min((a,b,c))==2:
        return True
    else: False

def isrunortripet(a,b,c):
    return isrun(a,b,c) or istripet(a,b,c)
def isbaby(num):
    print(num)
    card = [0]*6
    for i in range(6):
        card[i] = num%10
        num = num//10
    com = [(1,2,3,4,5,6),(1,2,4,3,5,6),(1,2,5,3,4,6),(1,2,6,3,4,5),(1,3,4,2,5,6),(1,3,5,2,4,6),(1,3,6,2,4,5),(1,4,5,2,3,6),(1,4,6,2,3,5),(1,5,6,2,3,4)]
    for i in com:
        if isrunortripet(card[i[0]-1],card[i[1]-1],card[i[2]-1]) and isrunortripet(card[i[3]-1],card[i[4]-1],card[i[5]-1]):
            return True
    return False
print(isbaby(num))