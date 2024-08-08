from collections import deque
import sys
sys.stdin = open("input.txt", "r")

def main():
    std_num, num = map(int, input().split())

    input_li = [list(map(int, input().split())) for _ in range(num)]
    #그래프 생성
    graph = [[] for _ in range(std_num+1)]

    #진입 차수가 없는 정점은 비교가 큰 쪽
    #진입차수 저장하는 배열
    in_degree = [0] * (std_num+1)

    for li in input_li:
        #1 -> 2, 3 은 진출차수를 저장하는 것. 방향을 거꾸로 저장
        graph[li[1]].append(li[0])
        #진입차수는 거꾸로. 
        in_degree[li[0]] += 1
    
    queue = deque([])
    sorted_order = []

    for node in range(1, std_num+1):
        if in_degree[node] == 0:
            queue.append(node)
            in_degree[node] = -1

    while queue:
        cur_node = queue.popleft()
        sorted_order.append(cur_node)
        # 큐에서 빼주면 진입차수 줄이고, 진입 차수 줄어든 애들 중 0 다시 넣기
        # 키가 작다는 정보가 여러번 있으면 여러번 진입 차수가 줄어들어야 함
        for elem in graph[cur_node]:
            in_degree[elem] -= 1
        
        for node in range(1, std_num+1):
            if in_degree[node] == 0:
                queue.append(node)
                in_degree[node] = -1
    
    for elem in sorted_order[::-1]:
        print(elem, end=" ")

    #print(graph)

if __name__ == "__main__":
    main()