for _ in range(10):
       T,N=map(int,input().split())
       arr1=[0]*100
       arr2=[0]*100
       pair=list(map(int,input().split()))
       for i in range(0,len(pair),2):
              if arr1[pair[i]]==0:
                     arr1[pair[i]]=pair[i+1]
              else:
                     arr2[pair[i]]=pair[i+1]
       stack=[0]
       visited=[False]*100
       visited[0]=True
       while stack:
              v=stack.pop()
              if not visited[arr1[v]]:
                     visited[arr1[v]]=True
                     stack.append(arr1[v])
              if not visited[arr2[v]]:
                     visited[arr2[v]]=True
                     stack.append(arr2[v])
       result=0
       if visited[99]==True:
              result=1
       print(f'#{T} {result}')

