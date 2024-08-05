# s1 = 'abc'
# s2 = 'abc'
# print(s1 is s2)
#
# print('a' < 'aa')
# print('a' > 'ab')
# print('aac' < 'abc')
# print('ab' < 'aac')
# ord()
#

def trans(s):
    if s == "ZRO":
        return 0
    if s == "ONE":
        return 1
    if s == "TWO":
        return 2
    if s == "THR":
        return 3
    if s == "FOR":
        return 4
    if s == "FIV":
        return 5
    if s == "SIX":
        return 6
    if s == "SVN":
        return 7
    if s == "EGT":
        return 8
    if s == "NIN":
        return 9


def trans_inv(s):
    if s == 0:
        return "ZRO"
    if s == 1:
        return "ONE"
    if s == 2:
        return "TWO"
    if s == 3:
        return "THR"
    if s == 4:
        return "FOR"
    if s == 5:
        return "FIV"
    if s == 6:
        return "SIX"
    if s == 7:
        return "SVN"
    if s == 8:
        return "EGT"
    if s == 9:
        return "NIN"


T = int(input())
for tc in range(1, T + 1):
    a, l = input().split()
    string = input()
    l = int(l)
    lst = []
    result = ""
    for i in range(l):
        lst.append(trans(string[4 * i:4 * i + 3]))
    lst.sort()
    for i in lst:
        result=result+trans_inv(i)+" "
    result=result.rstrip()
    print(f'#{tc}')
    print(result)
