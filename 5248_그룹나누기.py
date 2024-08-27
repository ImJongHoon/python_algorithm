from collections import deque

import sys
sys.stdin = open("input.txt", "r")

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        vertex_num, edge_num = map(int, input().split())
        input_arr = list(map(int, input().split()))
        edges = [[] for _ in range(edge_num)]
        
        for i in range(edge_num):
            edges[i].append(input_arr[2*i])
            edges[i].append(input_arr[2*i + 1])
            
        #print(edges)
        
        graph = {v:[] for v in range(1, vertex_num+1)}
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        #print(graph)
        
        visited = set()
        vertexes = deque([])
        group_num = 0;
        
        for start_vertex in range(1, vertex_num+1):
            if start_vertex in visited:
                continue
            
            
            #정점 방문 및 추가
            visited.add(start_vertex)
            group_num += 1
            
            for next_v in graph[start_vertex]:
                vertexes.append((start_vertex, next_v))
                visited.add(next_v)
                
            #print(visited)
            
            while vertexes:
                start_v, end_v = vertexes.popleft()
                
                for next_v in graph[end_v]:
                    if next_v in visited:
                        continue
                    
                    vertexes.append((end_v, next_v))
                    visited.add(next_v)
                
        
        print(f"#{test_case} {group_num}")

if __name__ == "__main__":
    main()