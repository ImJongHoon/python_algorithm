import math

start = (1,1)
end = (2,2)

dx = abs(end[0] - start[0])
dy = abs(end[1] - start[1])

dist = math.sqrt(dx**2 + dy**2)

radian = math.atan(dy/dx)

print(dist, math.degrees(radian))