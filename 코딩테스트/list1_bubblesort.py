# N= 5
# arr = [55, 7, 78, 12, 42]
#
# for i in range(N-1,0,-1):# 각 구간의 끝 인덱스 i
#     for j in range(i): # 각 구간에서 두 개씩 비교할 때 흰쪽 원소의 인덱스 j
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]# 왼쪽 원소가 더 크면 교환
# print(*arr)
#
# N= 5
# arr = [55, 7, 78, 12, 42]
#
# for i in range(N):# 각 구간의 끝 인덱스 i
#     for j in range(N-1-i): # 각 구간에서 두 개씩 비교할 때 흰쪽 원소의 인덱스 j
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]# 왼쪽 원소가 더 크면 교환
# print(*arr)
#
# 9
# 7 4 2 0 0 6 0 7 0
# N = int(input())
# lst = list(map(int,input().split()))
# for i in range(N-1):
#     base_l = lst[i]
#     #base_l 보다 작등ㄴ 길이의 갯수를 센다
#     cnt =0
#     for j in range(i+1,N):
#         if base_l > lst[j]:
#             cnt+=1
#
#     if max_v > cnt:
#
import sys
sys.stdin = open('1206', 'r')
T = 10
for tc in range(1,T+1):
    tc= int(input())
    bld = input()



