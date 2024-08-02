# T = int(input())
def fac(a):
    if a == 1:
        return 1
    else:
        return a*fac(a-1)
    
def com(a,b):
    return fac(a)//(fac(a-b)*fac(b))


def product(lst):
    result = 0
    for i in range(len(lst1)):
        result += lst[i]*i
    return result

def combi(lst,sum):
    result = 0
    que = []
    lst = lst[::-1]
    pro = [0 for i in range(len(lst)+1)]
    temp = []
    que.append(pro)
    while que:
        print(que)
        for i in range(lst):
            if que[0][i] > lst[i]:
                continue
        if product(que[0][:-1]) > sum:
            que = que[1:]
        elif product(que[0][:-1]) == sum:
            result +=1
            que = que[1:]
        elif product(que[0][:-1]) <sum and len(que[0])-1>que[0][-1]:
            que.append(que[0])
            que[0][0][que[0][1]] += 1
            
            print(que)
            
            que[0][0][que[0][1]] -= 1
            que[0][1] += 1
            que.append(que[0])
            que = que[1:]
        else:
            que = que[1:]
    return result
# print(combi([0,4,2],3))
print(com(5,3))



# for test_case in range(1, T + 1):
#     D = int(input())
#     W = list(map(int,input().split()))
#     Q = int(input())
#     Qlst = []
#     Numlst = []
#     for i in range(Q):
#         Qlst.append(list(map(int,input().split())))
#     for i, c in enumerate(W):
#         Numlst.append(i)
    
#     # Numlst.append(0)
#     # Numlst.append(W[1])
#     # Numlst.append(W[2] - (W[0]*(W[0]-1)//2))
#     # 1 1 1 2 2 3 

