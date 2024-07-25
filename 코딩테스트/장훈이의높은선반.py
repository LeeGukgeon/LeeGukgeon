T = int(input()) 
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    H = sorted(list(map(int,input().split())))
    SUM = sum(H)  # 반대로 생각하면 제외된 점원들의 키가 SUM - B 이하이면서 SUM - B 와 가장 가까운 경우를 찾는 것이기 때문에 
    def search(h,b,a): #h는 남은 사람들의 키를 원소로 갖는 리스트, b는 SUM - B, a 는 제외된 점원들의 키의 총합
        print(h,b,a)
        if h == []: #남은 점원이 없다면 b-a (= 선반과 점원들 키의 총합의 차이)를 반환
            return b-a
        HI = h[-1]
        if HI > b - a: #남은 점원들중 가장 키가 큰 사람의 키가 b-a 보다 크다면 그사람을 제외한다면 키의 총합이 선반높이보다 낮아지기 때문에 무조건 포함한다
            h.pop()
            return search(h,b,a)
            
        else:
            hc = h[:]
            h.pop()
            s1 = search(h,b,a+HI) # 남은 점원들 중 키가 가장 큰 점원을 제외하는 경우의 최솟값 
            print(s1)
            hc.pop()
            s2 = search(hc,b,a) #남은 점원들 중 키가 가장 큰 점원을 포함하는 경우의 최솟값
            print(s2)
            if s1 <= s2 : #더 작은 값을 리턴한다.
                return s1
            else:
                return s2
    print(f'#{test_case} {search(H,SUM-B,0)}') #초기값을 입력한다.
        