def decode(binary,scale):
    code=''
    sentence=''
    for i in range(0, 56 * scale, scale):
        code=code+binary[i]
    for i in range(0,56,7):
        sentence=sentence+ctd[code[i:i+7]]
    result=0
    for i in range(8):
        if i%2==0:
            result+=3*int(sentence[i])
        else:
            result+=int(sentence[i])
    if result%10==0:
        return_v=0
        for i in range(8):
            return_v+=int(sentence[i])
        return return_v
    else:
        return 0

def checkscale(binary):
    binary=binary[-24:]
    double=True
    triple=True
    idx=0
    while idx<24 and double==True:
        if binary[idx]!=binary[idx+1]:
            double=False
        idx+=2
    if double==True:
        return 2
    idx=0
    while idx<24 and triple==True:
        if binary[idx]!=binary[idx+1] or binary[idx+1]!=binary[idx+2]:
            triple=False
        idx+=3
    if triple==True:
        return 3
    return 1

T=int(input())
for tc in range(1,1+T):
    N,M=map(int,input().split())
    arr=['']*N
    for i in range(N):
        arr[i]=input().strip()
    arr=list(set(arr))
    result=0
    htb={'0':'0000','1':'0001','2':'0010','3':'0011',
         '4':'0100','5':'0101','6':'0110','7':'0111',
         '8':'1000','9':'1001','A':'1010','B':'1011',
         'C':'1100','D':'1101','E':'1110','F':'1111'}
    ctd={'0001101':'0','0011001':'1','0010011':'2','0111101':'3',
         '0100011':'4','0110001':'5','0101111':'6','0111011':'7',
         '0110111':'8','0001011':'9'}
    donecode=[]
    print(arr)
    for i in range(len(arr)):
        binary=''
        for x in arr[i]:
            binary=binary+htb[x]
        for x in donecode:
            binary=binary.replace(x,'')
        binary=binary.rstrip('0')
        while binary!='':
            scale=checkscale(binary)
            donecode.append(binary[-56*scale:])
            result+=decode(binary[-56*scale:],scale)
            binary=binary[:-56*scale]
            binary=binary.rstrip('0')
    print(f'#{tc} {result}')