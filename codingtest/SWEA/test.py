# import sys
# sys.stdin = open('input.txt', 'r')

# 식재료 조합 구하기
def dfs(n, lst):
    # 가지치기 - 이미 mat에 있는 조합이면,
    # 종료조건 - 길이가 되면
    if n == N:
        half_1 = tuple(lst[:N // 2])
        half_2 = tuple(lst[N // 2:])
        if (half_1, half_2) in mat:
            return
        mat.add((half_1, half_2)) # 양쪽 절반을 튜플로 추가
        return

    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            dfs(n+1, lst+[i])
            visit[i] = 0



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    visit = [0] * N # 각 숫자가 한 번씩만 나와야 하니까
    mat = set() # 재료조합
    dfs(0, [])

    # print(mat)

    min_diff = 21e8
    sum_v = 0
    result=1000000
    for (food1, food2) in mat:
        syn1=0
        syn2=0
        for i in range(N // 2):
            for j in range(N // 2):
                syn1+=arr[food1[i]][food1[j]]
                syn2 += arr[food2[i]][food2[j]]
        diff=abs(syn1-syn2)
        if diff<result:
            result=diff
    print(f'#{tc} {result}')