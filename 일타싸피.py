import math

SIZE = 5.73

#x, y
my = (1,1)
target_ball = (20, 25)
hole = (50, 50)

m2h = math.sqrt((my[0] - hole[0]) ** 2 + (my[1] - hole[1]) ** 2)
t2h = math.sqrt((target_ball[0] - hole[0]) ** 2 + (target_ball[1] - hole[1]) ** 2)
m2t = math.sqrt((my[0] - target_ball[0]) ** 2 + (my[1] - target_ball[1]) ** 2)

#print(m2h, t2h, m2t)
#print((m2h**2 + t2h**2 - m2t**2) / (2*m2h*t2h))

acos_radian = math.acos((m2h**2 + t2h**2 - m2t**2) / (2*m2h*t2h))

#print(math.degrees(acos_radian))

dist = math.sqrt( m2h**2 + (t2h+SIZE)**2 - math.cos(acos_radian)*2*m2h*(t2h+SIZE) )

print(dist)

#목적구와 내가 치고자하는 위치의 각도차이
print((dist**2 + m2t**2 - SIZE**2) / (2*dist*m2t))
target_radian = math.acos((dist**2 + m2t**2 - SIZE**2) / (2*dist*m2t))

print(math.degrees(target_radian))

#목적구와의 각도 구해서 45도 이상인지 이하인지 판별.
dx = target_ball[0] - my[0]
dy = target_ball[1] - my[1]
tan_radian = math.atan(dy/dx)

print(math.degrees(tan_radian))

print(90 - math.degrees(tan_radian) - math.degrees(target_radian))