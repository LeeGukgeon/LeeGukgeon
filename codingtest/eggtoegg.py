def run(idx):
    global result
    if idx==N: #마지막 계란(N-1) 깨고 나면 max 값 갱신
        if result<cracked.count(True):
            result=cracked.count(True)
    elif cracked.count(False)==1: #중간에 계란이 한개 남으면 max 값 갱신
        if result!=N:
            result=N-1
    elif cracked[idx]==True: #계란이 깨져있으면 다음으로 넘어감
        run(idx+1)
    else:
        for i in range(N): #N 개의 계란의 인덱스를 돌면서
            if cracked[i]==False and i!=idx: #들고있는 계란 말고 안깨진 계란이면
                S[i]-=W[idx] #치고
                S[idx]-=W[i]
                if S[i]<=0: #깨졌으면 깨졌다고 표시
                    cracked[i]=True
                if S[idx]<=0:
                    cracked[idx]=True
                run(idx+1) #다음 계란 들기
                S[i]+=W[idx] # 안 친 상태로 원상 복구
                S[idx]+=W[i]
                if 0<S[i]: #안 깨진 상태로 원상 복구
                    cracked[i] =False
                if 0<S[idx]:
                    cracked[idx] =False
N=int(input())
S=[0]*N
W=[0]*N
for i in range(N):
    S[i],W[i]=map(int,input().split())
cracked=[False]*N
result=0
run(0)
print(result)