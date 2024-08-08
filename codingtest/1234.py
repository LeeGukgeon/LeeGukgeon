for _ in range(1):
    N,password=input().split()
    i=0
    while i<len(password)-1:
        if password[i]==password[i+1]:
            password=password[:i]+password[i+2:]
            print(password)
            if i==0:
                continue
            i-=1
        else:
            i+=1
    print(f'#{_+1} {password}')