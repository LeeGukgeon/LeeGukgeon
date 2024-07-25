# T = int(input())
# for test_case in range(1, T + 1):
N = int(input())
grp = list(map(int,input().split()))
grp_copy = grp[:]
que = [1]
result = [1]
TF = True
while TF:
    TF=False
    Num = grp_copy.count(que[0])
    print(Num)
    for i in range(Num):
        result.append(grp_copy.index(que[0])+2)
        que.append(grp_copy.index(que[0])+2)
        grp_copy[grp_copy.index(que[0])] = 0
        print(grp_copy)
        print(result)
        print(que)
    que=que[1:]
    print(que)
    for i in grp_copy:
        if i != 0:
            TF = True
print(result)