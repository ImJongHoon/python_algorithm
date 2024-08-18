def DFS(graph, visited, start_graph):
    for vertex in graph[start_graph]:
        if visited[vertex] == 1:
            continue
        visited[vertex] = 1
        DFS(graph, visited, vertex)

    return

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for idx_node, computer in enumerate(computers):
        for idx_child, vertex in enumerate(computer):
            if vertex == 1:
                graph[idx_node + 1].append(idx_child+1)

    for i in range(1, n+1):
        if visited[i] == 0:
            answer += 1
            visited[i] = 1
            DFS(graph, visited, i)

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))