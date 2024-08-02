import copy
from pprint import pprint
T=int(input())
for tc in range(1,1+T):
    N=int(input())
    Mac=[list(map(int,input().split())) for _ in range(N)]
    core_lst=[]
    unc_core_lst=[]
    for i in range(1,N-1):
        for j in range(1,N-1):
            if Mac[i][j]==1:
                core_lst.append([i,j])
    que=[(Mac,core_lst,unc_core_lst)]
    result=100
    un_num=12
    result_mac =[]



    def search(mac,core_lst,unc_core_lst):
        global que
        global result
        global un_num
        global result_mac
        line = 0
        un_num_temp = len(core_lst)+len(unc_core_lst)
        mac1 = copy.deepcopy(mac)
        mac2 = copy.deepcopy(mac)
        mac3 = copy.deepcopy(mac)
        mac4 = copy.deepcopy(mac)
        for i in range(N):
            for j in range(N):
                if mac[i][j]==2:
                    line+=1
        if un_num < len(unc_core_lst):
            return 0
        if un_num_temp<un_num:
            result=line
            un_num=un_num_temp
            result_mac = mac
        if un_num_temp==un_num:
            if line < result:
                result = line
                result_mac = mac
        if len(core_lst)==0:
            return 0
        # print(mac)
        # print(core_lst)
        # print(unc_core_lst)
        # print((result, un_num))

        up=True
        for i in range(core_lst[0][0]):
            if mac[i][core_lst[0][1]]!=0:
                up = up and False
        right = True
        for i in range(core_lst[0][1]+1,N):
            if mac[core_lst[0][0]][i] != 0:
                right = right and False
        down=True
        for i in range(core_lst[0][0]+1,N):
            if mac[i][core_lst[0][1]]!=0:
                down=down and False
        left=True
        for i in range(core_lst[0][1]):
            if mac[core_lst[0][0]][i]!=0:
                left=left and False
        if up:
            for i in range(core_lst[0][0]):
                mac1[i][core_lst[0][1]]=2
            que.append((mac1,core_lst[1:],unc_core_lst))
        if right:
            for i in range(core_lst[0][1]+1,N):
                mac2[core_lst[0][0]][i]=2
            que.append((mac2,core_lst[1:],unc_core_lst))
        if down:
            for i in range(core_lst[0][0] + 1, N):
                mac3[i][core_lst[0][1]]=2
            que.append((mac3,core_lst[1:],unc_core_lst))
        if left:
            for i in range(core_lst[0][1]):
                mac4[core_lst[0][0]][i]=2
            que.append((mac4,core_lst[1:],unc_core_lst))
        unc_core_lst_c = unc_core_lst+[core_lst[0]]
        que.append((mac,core_lst[1:],unc_core_lst_c))

    for i in range(10000):
        if que==[]:
            break
        search(que[0][0],que[0][1],que[0][2])
        que=que[1:]
    print(f'#{tc} {result}')