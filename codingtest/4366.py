T=int(input())
def f(bin,triple):
    for i in range(len(bin)):
        for j in range(len(triple)):
            for k in range(3):
                if k!=int(triple[j]):
                    if (1<<i)^int(bin_num,2)==int(triple[:j]+str(k)+triple[j+1:],3):
                        return (1<<i)^int(bin_num,2)

for tc in range(1,1+T):
    bin_num=input()
    triple_num=input()
    print(f'#{tc} {f(bin_num,triple_num)}')

