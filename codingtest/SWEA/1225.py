for tc in range(1,11):
    T=int(input())
    data=list(map(int,input().split()))
    data_modified=list(map(lambda x:x-(((min(data)//15)-1)*15),data))
    i=0
    while 0<data_modified[-1]:
        temp=data_modified.pop(0)
        data_modified.append(temp-(i+1))
        i=(i+1)%5
    data_modified[-1]=0
    print(f'#{T}',*data_modified)