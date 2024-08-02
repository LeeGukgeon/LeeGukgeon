# T = int(input())
# def cal(n,k,lst):
#
#     if k < (n*(n+1))//2:
#         return 0
#     if  13*n-((n*(n+1))//2) < k:
#         return 0
#     next_lst=lst
#     result =0
#
#
# for tc in range(1,T+1):
#     A=[1,2,3,4,5,6,7,8,9,10,11,12]
#     N,K = map(int,input().split())
#     print(f'#{tc} {cal(N,K,A)}')
arr=[1,2,3,4,5,6,7,8,9,10,11,12]
n=len(arr)
sub =[]
cnt = 0
for i in range(1<<n):
    temp = []
    for j in range(n):
        if i&(1<<j):
            temp.append(arr[j])
    sub.append(temp)
for set in sub:
    if len(set)==N and sum(set)==K:
        cnt+=1
print(f'# {cnt}')