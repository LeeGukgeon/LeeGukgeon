# T=int(input())
# for tc in range(1,T+1):
#     sentence=input()
#     i=0
#     while i<len(sentence)-1:
#         if sentence[i]==sentence[i+1]:
#             sentence=sentence[0:i]+sentence[i+2:]
#             if i==0:
#                 continue
#             i-=1
#             continue
#         i+=1
#     print(f'#{tc} {len(sentence)}')        
lst=input().split()
str1,str2=lst[0],lst[1]
str1=list(str1)
str2=list(str2)
print(str1,str2)