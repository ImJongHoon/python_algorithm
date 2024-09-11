def solution(n, results):

    answer = 0
    win_graph = [set() for _ in range(n+1)]
    lose_graph = [set() for _ in range(n+1)]

    graph = [set() for _ in range(n+1)]
    
    for win, lose in results:
        graph[win].add(lose)
        lose_graph[lose].add(win)

    # print(graph)
    # print(lose_graph)
    for _ in range(1, n):
        for st_node in range(1, n+1):
            for ed_node in graph[st_node]:
                lose_graph[ed_node] = lose_graph[ed_node] | lose_graph[st_node]
    
    # print(graph)
    # print(lose_graph)

    for st_node in range(1, n+1):
        for ed_node in lose_graph[st_node]:
            graph[ed_node].add(st_node)

    cnt = 0

    for node in range(1, n+1):
        temp = graph[node] | lose_graph[node]
        if len(temp) == n-1:
            cnt += 1

    answer = cnt

    print(lose_graph)
    print(graph)
    print(answer)

    return answer

arr = []

for i in range(1, 4500):
    arr.append([i, i+1])


#print(arr)
solution(4501, arr)