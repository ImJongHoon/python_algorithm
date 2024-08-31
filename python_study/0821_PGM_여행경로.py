from copy import deepcopy

result = []

def DFS(graph, path, tickets, cur_node, visited, cnt):
    global result
    if result != []:
        #print("debug")
        return
    
    # print(path)
    # print(len(tickets))
    
    if len(path) == len(tickets):
        result = path[:]
        #print(result)
        return
    
    for next_node in graph[cur_node]:
        #방문처리를?
        if next_node not in visited[cur_node]:
            continue
        path.append((cur_node, next_node, cnt+1))
        visited[cur_node].remove(next_node)
        #print(path, num)
        DFS(graph, path, tickets, next_node, visited, cnt+1)
        path.remove((cur_node, next_node, cnt+1))
        visited[cur_node].append(next_node)
        

def solution(tickets):
    global result
    answer = []
    #그래프 자료구조 만들기
    #단, 노드를 만들 때, 알파벳 순서로 정렬하기
    
    tickets.sort()
    #print(tickets)
    #티켓을 다 소모해야함. 모든 경로를 다 가야함.
    temp = set()
    for ticket in tickets:
        temp.add(ticket[0])
        temp.add(ticket[1])
        
    tickets_arr = list(temp)
    tickets_arr.sort()
    
    #print(tickets_arr)
    
    node = {}
    reverse_node = {}
    node_num = 0
    for ticket in tickets_arr:
        if ticket in node.keys():
            continue
        node[ticket] = node_num
        reverse_node[node_num] = ticket
        node_num += 1
    #print(node)
        
    #그래프 만들기
    graph = [[] for _ in range(len(node))]
    for ticket in tickets:
        #print(node[ticket[0]], node[ticket[1]])
        graph[node[ticket[0]]].append(node[ticket[1]])
        
    for li in graph:
        li.sort()
        
    #print(graph)
    temp = []
    for y in range(len(tickets)):
        temp.append((node[tickets[y][0]], node[tickets[y][1]]))
    temp.sort()
    #print(temp)
            
    
    #print(graph, [], len(tickets), start_node)
    start_node = node['ICN']
    DFS(graph, [], tickets, start_node, deepcopy(graph), 0)
    
    #print(result)
    
    for path in result:
        answer.append(reverse_node[path[0]])
        
    answer.append(reverse_node[result[-1][1]])
    
    #print(answer)
    
    return answer

#solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
#solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
#solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]])
#solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]])
#solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]])
#solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]])