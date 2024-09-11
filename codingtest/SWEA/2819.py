def find_numbers(r,c,numberstr):
    if len(numberstr)==7:
        numbers.add(numberstr)
        return
    for i in range(4):
        if 0<=r+dr[i]<4 and 0<=c+dc[i]<4:
            find_numbers(r+dr[i],c+dc[i],numberstr+fourbyfour[r][c])

T=int(input())
for tc in range(1,1+T):
    fourbyfour=[input().split() for i in range(4)]
    numbers=set()
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]
    for i in range(4):
        for j in range(4):
            find_numbers(i,j,'')
    print(f'#{tc} {len(numbers)}')


