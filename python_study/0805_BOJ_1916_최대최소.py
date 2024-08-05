import heapq

def main():
    vertex_num = int(input())
    edge_num = int(input())

    buses = [list(map(int, input().split())) for _ in range(edge_num)]
    start, end = map(int, input().split())

    graph = [[] for _ in range(vertex_num+1)]

    #그래프 자료구조 저장
    for elem in buses:
        graph[elem[0]].append([elem[1], elem[2]])

    #시작좌표 0
    costs = [float("inf") for _ in range(vertex_num+1)]
    costs[start] = 0

    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        current_cost, current_vertex = heapq.heappop(pq)
        if costs[current_vertex] < current_cost:
            continue

        for next_vertex, next_cost in graph[current_vertex]:
            sum_cost = current_cost + next_cost
            if sum_cost >= costs[next_vertex]:
                continue

            costs[next_vertex] = sum_cost
            heapq.heappush(pq, [sum_cost, next_vertex])

    print(costs[end])


if __name__ == "__main__":
    main()