T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case} ',end = "")
    A_len ,B_len = map(int,input().split())
    A = sorted(list(map(int,input().split())),reverse=True)
    B = sorted(list(map(int,input().split())),reverse=True)
    A.extend([0])
    B.extend([0])
    ans = 0
    def AB(a,b): 
        global ans
        if a[0] > b[0] and b[1]+b[2] <= a[0] :
            print(a)
            print(b)

            return 0
        elif a[0] >= b[0]+b[1]:
            print(a)
            print(b)

            return 0
        elif a[0] + a[1] > b[0] + b[1]:
            print(a)
            print(b)

            return 0
        # elif a[0] + a[1] <= b[0]:
        #     print(a)
        #     print(b)

        #     return 1
        # elif b[0] > a[0]+a[1] and a[1]+a[2] <= b[0]:
        #     return 1
        # elif b[0] >= a[0]+a[1]+a[2]:
        #     return 1
        # elif b[0] +b[1] > a[0]+a[1]+a[2]:
        #     return 1
        # elif b[0]+b[1] <= a[0]+a[1]:
        #     return 0
        else:
            

            a[1] += a[0]
            a=a[1:]
            ans +=1
            print(a)
            print(b)
            AB(b,a)
            return 0
    AB(A,B)
    if ans%2 == 0:
        print("Takeover Incorporated")
    else:
        print("Buyout Limited")

    