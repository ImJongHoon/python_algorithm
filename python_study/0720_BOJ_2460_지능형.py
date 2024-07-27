import sys
NUM = 10
input_li = []
for _ in range(NUM):
    input_li.append([int(x) for x in sys.stdin.readline().split()])
#print(input_li)
people = []
temp = 0
for li in input_li:
    temp = temp - li[0] + li[1]
    people.append(temp)
print(max(people))