from collections import deque
import sys
sys.stdin = open("input.txt", "r")

def main():
    T = 10
    for test_case in range(1, T + 1):
        graph = [set() for _ in range(101)]
        visited = [0] * 101
        num, start_v = map(int, input().split())
        input_data = list(map(int, input().split()))


        for i in range(int(num/2)):
            start = i*2
            end = i*2 + 1
            graph[input_data[start]].add(input_data[end])

        queue = deque([])
        next_queue = deque([])

        visited[start_v] = 1
        for end_v in graph[start_v]:
            visited[end_v] = 1
            next_queue.append(end_v)

        temp = []

        while next_queue:
            queue = next_queue
            temp = next_queue.copy()
            next_queue = deque([])
            # print(queue)
            # print(next_queue)
            # print()
            
            while queue:
                start_vertex = queue.popleft()

                for end_v in graph[start_vertex]:
                    if visited[end_v] == 1:
                        continue

                    visited[end_v] = 1
                    next_queue.append(end_v)

        #print(temp)
        result = max(temp)

        #마지막 연락망 이면서 가장 큰 수
        print(f"#{test_case} {result}")

if __name__ == "__main__":
    main()
