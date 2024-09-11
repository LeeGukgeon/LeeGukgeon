T=int(input())
for tc in range(1,1+T):
    N=int(input())
    arr=list(map(int,input().split()))
    a=0
    b=0
    c=0
    result=100
    for i in range(2,30): #당근을 나누는 첫번째 기준을 돌면서
        for j in range(i+1,31): #당근을 나누는 두번째 기준을 돌면서
            for n in range(N): #각 상자에 나뉜 당근 개수 세기
                if arr[n]<i:
                    a+=1
                elif i<=arr[n]<j:
                    b+=1
                elif j<=arr[n]:
                    c+=1
            if a<=N//2 and b<=N//2 and c<=N//2: #주어진 조건에 맞으면서
                if 0<a and 0<b and 0<c: #각 상자에 1개 이상 들어있으면서
                    if max(a,b,c)-min(a,b,c)<result: #당근의 최댓값과 최솟값의 차이가 최소인 값을 저장
                        result=max(a,b,c)-min(a,b,c)
            a=0
            b=0
            c=0
    if result==100: #조건에 맞게 상자에 나눌 수 없으면 -1
        result=-1
    print(f'#{tc} {result}')


