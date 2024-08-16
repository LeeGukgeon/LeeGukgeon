T=int(input())
for tc in range(1,1+T):
    A,B,C,D=map(int,input().split())
    if B==0 and C==0 and 0<A and 0<D:
        print(f'#{tc} impossible')
        continue
    elif 1<abs(B-C):
        print(f'#{tc} impossible')
        continue
    elif B<C:
        print(f'#{tc} ', end='')
        if 0<D:
            for _ in range(D + 1):
                print('1', end='')
            print('0', end='')
            for _ in range(A):
                print('0', end='')
            for _ in range(B):
                print('10', end='')
        else:
            print()
            print('10',end='')
            for _ in range(A):
                print('0',end='')
            for _ in range(B):
                print('01',end='')
            if 0<B:
                print('0',end='')
            print()


    elif C<B:
        print(f'#{tc} ', end='')
        if 0<A:
            for _ in range(A+1):
                print('0', end='')
            print('1',end='')
            for _ in range(D):
                print('1',end='')
            for _ in range(C):
                print('01',end='')
            print()
        else:
            print('01', end='')
            for _ in range(D):
                print('1', end='')
            for _ in range(C):
                print('10', end='')
            if 0<C:
                print('1',end='')
            print()

    elif A==0 and B==0 and C==0:
        print(f'#{tc} ', end='')
        for _ in range(D+1):
            print('1',end='')
        print()
    elif B==0 and C==0 and D==0:
        print(f'#{tc} ', end='')
        for _ in range(A+1):
            print('0',end='')
        print()
    else:
        print(f'#{tc} ', end='')
        print('10',end='')
        for _ in range(A):
            print('0',end='')
        for _ in range(B-1):
            print('10',end='')
        print('1',end='')
        for _ in range(D):
            print('1', end='')
        print()