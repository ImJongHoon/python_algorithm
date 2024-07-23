from collections import deque #앞에서 데이터를 꺼내도 시간복잡도 1

total_candy = 20
last_person = None
person_queue = deque()

person_queue.append((1, 1))
person_cnt = 1

#마이쮸가 남아있는 동안
while total_candy > 0:
    person, candy_to_receive = person_queue.popleft()

    if total_candy - candy_to_receive <= 0:
        last_person = person
        break
        
    person_cnt += 1
    total_candy -= candy_to_receive
    person_queue.append((person, candy_to_receive+1))
    person_queue.append((person_cnt, 1))

print(f"마지막 마이쮸는 {last_person}번")