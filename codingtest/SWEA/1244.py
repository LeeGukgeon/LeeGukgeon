T=int(input())
def trade(n):
    if n==0:
        return int(''.join(card))
    idx=0
    while idx<len(card) and card[idx]==card_sorted[idx]:
        idx+=1
    if idx==len(card):
        if sameexist(card):
            return int(''.join(card))
        else:
            if n%2==0:
                return int(''.join(card))
            else:
                card[-1],card[-2]=card[-2],card[-1]
                return int(''.join(card))
    else:
        result=0
        for i in range(idx+1,len(card)):
            if card_sorted[idx]==card[i]:
                card[idx],card[i]=card[i],card[idx]
                # print(card)
                temp=trade(n-1)
                if result<temp:
                    result=temp
                card[i], card[idx] = card[idx], card[i]
        return result
def sameexist(card):
    for i in range(len(card)-1):
        for j in range(i+1,len(card)):
            if card[i]==card[j]:
                return True
    return False
for tc in range(1,1+T):
    card,N=map(int,input().split())
    card=list(str(card))
    card_sorted=sorted(card,reverse=True)
    result=trade(N)
    print(f'#{tc} {result}')

