T=int(input())
for tc in range(1,1+T):
    N=int(input())
    sequence=list(map(int,input().split()))
    subsequence_len=[1]*N #i번째 원소를 포함하는 최대 증가 부분수열의 길이를 저장
    for i in range(1,N):
        maxlen=1
        for j in range(i): #i번째 원소를 포함하는 최대 증가 부분수열의 길이는
            if sequence[j]<sequence[i]: # i보다 작고, j번째 원소가 i번째 원소보다 작은 경우의 모든 j 에 대하여
                maxlen=max(maxlen,subsequence_len[j]+1) # j번째 원소를 포함하는 최대증가부분수열 +1 의 최댓값이다.
        subsequence_len[i]=maxlen
    print(subsequence_len)
    print(f'#{tc} {max(subsequence_len)}')