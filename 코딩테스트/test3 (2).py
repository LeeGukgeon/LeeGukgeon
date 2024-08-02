T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    P = int(input())
    C = [0]*P
    for i in range(P):
        C[i] = int(input())
    result = [0]*P
    for j in range(len(C)):
        temp = 0
        for i in range(N):
            if A[i]<=C[j]<=B[i]:
                temp+=1
        result[j] = temp
    print(f'#{test_case}',*result)
