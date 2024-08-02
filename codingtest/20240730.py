data = [0,4,1,3,1,2,4,1]
MAX = max(data)
result = [0]*len(data)
counts = [0]*(MAX+1)
for x in data:
    counts[x] +=1
print(counts)
for i in range(1,MAX+1):
    counts[i] += counts[i-1]

print(counts)
for x in data:
    counts[x] -= 1
    result[counts[x]] = x
print(result)
