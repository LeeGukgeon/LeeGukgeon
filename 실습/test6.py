# 아래 함수를 수정하시오.
def find_min_max(lst):
    if not lst:
        return None
    min,max = lst[0],lst[0]
    for ele in lst:
        if ele < min:
            min = ele
        if max < ele:
            max = ele
    return (min, max)


result = find_min_max([58,987,6,4,2,8,-9878,89,6,7,0,8])
print(result)  # (1, 7)
