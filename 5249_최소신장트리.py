import heapq
import sys
sys.stdin = open("input.txt", "r")

def prim(last_vertex_num, edges):
    #mst = []
    sum_w = 0
    visited = [0] * (last_vertex_num + 1)
    
    #vertex 기준 자료구조 생성
    graph_vertex = {v: [] for v in range(last_vertex_num+1)}
    #print(graph_vertex)
    
    for start_v, end_v, w in edges:
        #print(start_v, end_v, w)
        graph_vertex[start_v].append((end_v, w))
        graph_vertex[end_v].append((start_v, w))
    
    #그냥 0에서 시작
    visited[0] = 1
    min_heap_edges = [[w, 0, e] for e, w in graph_vertex[0]]
    heapq.heapify(min_heap_edges)
    
    while min_heap_edges:
        weight, start_v, end_v = heapq.heappop(min_heap_edges)
        
        if visited[end_v] == 1:
            continue
        
        visited[end_v] = 1
        #mst.append((start_v, end_v, weight))
        sum_w += weight
        
        #새로 방문한 정점의 모든 인접 간선 처리
        for next_end, next_wegiht in graph_vertex[end_v]:
            if visited[next_end] == 1:
                continue
            heapq.heappush(min_heap_edges, [next_wegiht, end_v, next_end])
    
    return sum_w

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        last_vertex_num, edge_cnt = map(int, input().split())
        
        edges = [list(map(int, input().split())) for _ in range(edge_cnt)]
        #print(edges)
        
        
        #프림 알고리즘 사용
        sum_w = prim(last_vertex_num, edges)
        
        print(f"#{test_case} {sum_w}")

if __name__ == "__main__":
    main()