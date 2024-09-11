import math
diameter=5.73 #지름
hole_x,hole_y=100,200 #홀
my_x,my_y=100,250 #내공
object_x,object_y=150,200 #목적구
vector=[object_x-hole_x,object_y-hole_y] #홀에서 목적구로의 벡터
len_vector=math.sqrt(vector[0]**2+vector[1]**2) #위 벡터의 길이
unit_vector=list(map(lambda x:x/len_vector,vector)) #벡터의 요소를 각각 길이로 나누어 길이가 1인 벡터를 구함
diameter_vector=list(map(lambda x:x*diameter,unit_vector)) # 길이가 직경인 벡터로 바꿔줌
juhwang=(object_x+diameter_vector[0],object_y+diameter_vector[1]) # 목적구에 벡터를 더해 주황동그라미 위치를 구함
angle=math.atan2(juhwang[0]-my_x,juhwang[1]-my_y) #최종 각도=내 공에서 주황 공으로의 각도
angle=math.degrees(angle)
print(angle)




