# a=pow(82240514,-1,1000000007)
# print(a)
b = 889135293*90
print(b%1000000007)
# print((a*25)%1000000007)
# b = 10416667*96
# print(b%1000000007)
# c=82240514*585
# print(c%1000000007)

# print(pow(a*31,1,1000000007))
# # # print((562500004*5)&1000000007)
# # # print((880000010*4)%1000000007)

# # XYXYX=[1]
# # XYYYX=[1]
# # XYXXX=[1]
# # XYXYY=[1]
# XYYXX=[1]
# XYYYY=[1]
# XYXXY=[1]
# XYYXY=[1]
# for i in range(10):
#     XYXXX.append(6*XYXXX[i]+XYYXX[i]+2*XYXYX[i]+XYXXY[i])
#     XYXXY.append(4*XYXXY[i]+XYYXY[i]+2*XYXYY[i]+XYXXX[i])
#     XYXYX.append(4*XYXYX[i]+XYYYX[i]+2*XYXXX[i]+2*XYXYY[i])
#     XYXYY.append(4*XYXYY[i]+XYYYY[i]+2*XYXXY[i]+2*XYXYX[i])
# #     XYYXX.append(4*XYYXX[i]+XYXXX[i]+XYYYX[i]+2*XYYXY[i])
# #     XYYXY.append(4*XYYXY[i]+XYXXY[i]+XYYYY[i]+2*XYYXX[i])
# #     XYYYX.append(4*XYYYX[i]+XYXYX[i]+2*XYYXX[i]+XYYYY[i])
# #     XYYYY.append(6*XYYYY[i]+XYXYY[i]+2*XYYXY[i]+3*XYYYX[i])


# a=6*a + 1*b + 2*c + 0*d + 1*e + 0*f + 0*g + 0*h
# b=1*a + 4*b + 0*c + 2*d + 0*e + 1*f + 0*g + 0*h
# c=2*a + 0*b + 4*c + 2*d + 0*e + 0*f + 1*g + 0*h
# d=0*a + 2*b + 2*c + 4*d + 0*e + 0*f + 0*g + 1*h
# e=1*a + 0*b + 0*c + 0*d + 4*e + 2*f + 1*g + 0*h
# f=0*a + 1*b + 0*c + 0*d + 2*e + 4*f + 0*g + 1*h
# g=0*a + 0*b + 1*c + 0*d + 2*e + 0*f + 4*g + 1*h
# h=0*a + 0*b + 0*c + 1*d + 0*e + 2*f + 3*g + 6*h
# [[6,1,2,0,1,0,0,0],
#  [1,4,0,2,0,1,0,0],
#  [2,0,4,2,0,0,1,0],
#  [0,2,2,4,0,0,0,1],
#  [1,0,0,0,4,2,1,0],
#  [0,1,0,0,2,4,0,1],
#  [0,0,1,0,2,0,4,1],
#  [0,0,0,1,0,2,3,6]]
# # print(XYXYX)
# # result = 0
# # for i in range(len(XYXYX)):
#     result += (XYXYX[i]/32)/10**i
# print(result)
# XYXYX <- XYXYX(4)9 OR XYYYX 8 OR XYXXX(2)10 OR XYXYY(2)9 
# XYYYX <- XYYYX(4) OR XYXYX OR XYYXX(2) OR XYYYY
# XYXXX <- XYXXX(6) OR XYYXX OR XYXYX(2) OR XYXXY
# XYXYY <- XYXYY(4) OR XYYYY OR XYXXY(2) OR XYXYX(2)
# 8 XYYXX <- XYYXX(4) OR XYXXX OR XYYYX OR XYYXY(2)
# 12 XYYYY <- XYYYY(6) OR XYXYY OR XYYXY(2) OR XYYYX(3)
# 8 XYXXY <- XYXXY(4) OR XYYXY OR XYXYY(2) OR XYXXX
# 8 XYYXY <- XYYXY(4) OR XYXXY OR XYYYY OR XYYXX(2)
# print(62130*9)
# print(3806169373/420319877)
# # 1 11 88 669 5127
# # 0 0 1 20 268 3081
# print((1/32)/(1-(9.055411321/10)))