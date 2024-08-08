T = int(input())

for test_case in range(1, T+1):
    C, N = input().split()
    C_lst = list(C)
    i = 0 # 인덱스를 초과하지 않게 i를 센다.
    cnt = 0 # N의 횟수를 넘지 않게 cnt를 센다.
    while cnt != int(N) and i < len(C): # cnt가 N의 횟수를 초과하지 않고 인덱스를 초과하지 않는다.
        C_max = max(C_lst[i:]) # 인덱스 i 이후의 최댓값
        C_max_idx = C_lst.index(max(C_lst[i:])) # 인덱스 i 이후의 최댓값 인덱스
        if C_lst[i] == C_max: # 인덱스 i 이후의 최댓값이 인덱스 i의 값과 같으면 다음 인덱스로 넘어간다.
            i += 1
        elif C_lst.count(C_max) == 1: # 인덱스 i 이후의 최댓값이 1개면 인덱스 i의 값과 인덱스 최댓값을 교환한다.
            C_lst[i], C_lst[C_max_idx] = C_lst[C_max_idx], C_lst[i]
            cnt += 1
            i += 1
        else: # 인덱스 i 이후의 최댓값이 2개 이상
            n = 0 # 인덱스 i 이후의 최댓값의 개수를 초과하지 않게 센다.
            n_lst = [] # 인덱스의 최댓값과 바꿀 원소들의 리스트
            while cnt != int(N) and n != C_lst.count(C_max): # cnt가 N의 횟수를 초과하지 않고 인덱스 i 이후의 최댓값의 개수를 초과하지 않는다.
                if C_lst[i] == C_max: # 인덱스 i의 값이 인덱스 i 이후의 최댓값과 같으면 다음 인덱스로 넘어간다.
                    i += 1
                else: # 인덱스 i의 값이 인덱스 i 이후의 최댓값과 같지 않으면
                    n_lst.append(C_lst[i]) # n_lst에 추가한다.
                    n += 1
                    cnt += 1
                    i += 1
            n_lst.sort() # n_lst를 오름차순의로 정렬한다.
            for a in n_lst: # 정렬한 리스트에서 순서대로 가장 뒤쪽에 있는 최대값과 교환한다.
                a_dix = C_lst.index(a)
                C_max_idx = ''.join(C_lst).rindex(C_max)
                C_lst[a_dix], C_lst[C_max_idx] = C_lst[C_max_idx], C_lst[a_dix]
    if len(set(C_lst[-3:])) != 2 and (int(N)-cnt)%2 != 0: # 남은 cnt를 계산하여 홀수인 경우 인덱스 -2, -1의 자리를 바꿔준다.
        C_lst[-1], C_lst[-2] = C_lst[-2], C_lst[-1]
    print(f'#{test_case}', ''.join(C_lst))