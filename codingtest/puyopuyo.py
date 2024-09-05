def isexplode(arr):

def descend(arr):
    for c in range(6):
        idx=11
        for r in range(11,-1,-1):
            if arr[r][c]=='.':
                pass
            else:
                arr[r][c],arr[idx][c]=arr[idx][c],arr[r][c]
                idx+=1
    return



arr=[list(input()) for i in range(12)]
result=0
while True:
    explode_boolean=isexplode(arr)
    explode_exist=False
    for i in range(12):
        for j in range(6):
            if explode_boolean[i][j]:
                explode_exist=True
                arr[i][j]='.'
    if not explode_exist:
        break
    descend(arr)
    result+=1
print(result)


