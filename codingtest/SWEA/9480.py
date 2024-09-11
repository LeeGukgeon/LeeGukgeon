def countset(i):
    # print(i,used_words)
    tempset=set()
    for j in range(len(used_words)):
        for a in used_words[j]:
            if a in apb:
                tempset.add(a)
    if len(tempset)==26:
        return 2**(N-i)
    elif i==N:
        return 0
    for j in range(i,N):
        for a in words[j]:
            if a in apb:
                tempset.add(a)
    # print(tempset)
    if len(tempset)!=26:
        return 0
    v1=countset(i+1)
    used_words.append(words[i])
    v2=countset(i+1)
    used_words.remove(words[i])
    # print(v1+v2)
    return v1+v2

T=int(input())
apb=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for tc in range(1,1+T):
    N=int(input())
    words=[input() for _ in range(N)]
    used_words=[]
    print(f'#{tc} {countset(0)}')
