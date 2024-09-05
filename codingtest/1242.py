# import sys
# sys.stdin=open("input.txt","r")

T=int(input())
for tc in range(1,1+T):
    N,M=map(int,input().split())
    arr=['']*N
    for i in range(N):
        arr[i]=input().strip()
    hexa=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    htb={'0':'0000','1':'0001','2':'0010','3':'0011',
         '4':'0100','5':'0101','6':'0110','7':'0111',
         '8':'1000','9':'1001','A':'1010','B':'1011',
         'C':'1100','D':'1101','E':'1110','F':'1111'}
    ctd={'211':0,'221':1,'122':2,'411':3,
         '132':4,'231':5,'114':6,'312':7,
         '213':8,'112':9}
    result_cypher=[]
    arr=list(set(arr)) #중복제거
    for i in range(len(arr)): #한줄씩 읽으면서
        j=M-1 # 한 줄의 제일 뒷 열부터 읽으면서
        while 0<=j:
            if arr[i][j]!='0': #0이 아니면
                # print(i,'번째 행')
                cypher=arr[i][:j+1] # 그 행의 처음부터 j까지를 다 가져와서
                for k in range(16):
                    cypher=cypher.replace(hexa[k],htb[hexa[k]]) #2진수로 변환한 후
                cnt=0 #이번 암호를 해독하고 나서 j를 얼마나 줄여야 할지를 결정하는 변수
                while cypher[-1]!='1': # 변환 후에 제일 오른쪽이 1로 시작할 수 있게 0들을 지워주고
                    cypher=cypher[:-1]
                    cnt+=1
                # print(cypher)
                middle_cypher=[0]*32 #바코드의 길이비율을 나타낸 암호해독 중간단계
                bitlen=0 #비트가 바뀔 때 그 전 비트가 얼마나 길었는지를 나타내는 변수
                prebit='1' #초기의 이전비트
                switch=0 # 비트가 바뀐 횟수
                idx=-1 # 2진수 암호문의 인덱스. 마지막부터 해독
                while switch<31: #31번 비트가 바뀌면 종료
                    if cypher[idx]==prebit: #비트가 이전과 같으면
                        bitlen+=1
                    else: #비트가 이전과 다르면
                        middle_cypher[31-switch]=bitlen #그 전까지의 길이를 저장하고
                        switch+=1 #변수들 초기화
                        bitlen=1
                        prebit=cypher[idx]
                    idx-=1
                    cnt+=1
                scale=min(middle_cypher[1:]) #몇 배율
                middle_cypher=list(map(lambda x:(x//scale),middle_cypher)) # 배율만큼 각 값을 나눠준다.
                # print(middle_cypher)
                middle_cypher_str=''.join(map(str,middle_cypher)) # 문자열로 바꿔주고
                # print(middle_cypher_str)
                decoded=['0']*8
                for l in range(8): # 다시 평문으로 해독해서
                    decoded[l]=ctd[middle_cypher_str[4*l+1:4*l+4]]
                if decoded not in result_cypher: # 이 평문이 처음 보는 평문이면 저장해준다.
                    result_cypher.append(decoded)
                # print(decoded)
                # print()
                j-=(cnt//4)+1
            else:
                j-=1
    # print(result_cypher)
    result=0
    for x in result_cypher: #저장된 평문들이 정상적인지 판단해서 결과값에 더해준다.
        if (3*(x[0]+x[2]+x[4]+x[6])+x[1]+x[3]+x[5]+x[7])%10==0:
            result+=sum(x)
    print(f'#{tc} {result}')
