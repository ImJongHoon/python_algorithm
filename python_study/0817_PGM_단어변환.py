from collections import deque

def can_chage(word, cmp_word):
    cnt = 0

    for i in range(len(word)):
        if word[i] != cmp_word[i]:
            cnt += 1
        
        if cnt >= 2:
            return False
    
    return True

def BFS(start_node, target, graph, words):
    queue = deque([])
    visited = [0 for _ in range(len(graph))]
    #이미 한번 변환했다고 계산
    queue.append((start_node, 1))
    visited[start_node] = 1

    while queue:
        node, cnt = queue.popleft()
        if words[node] == target:
            print(words[node], target)
            return cnt
        
        for elem in graph[node]:
            if visited[elem] == 1:
                continue
            queue.append((elem, cnt+1))
            visited[elem] = 1



    return float('inf')

def solution(begin, target, words):
    answer = 0

    #words의 index == 그래프의 정점의 번호
    graph = [[] for _ in range(len(words))]

    for i in range(len(words)):
        word = words[i]
        #그래프 추가
        for end_idx, cmp_word in enumerate(words):
            if cmp_word == word:
                continue
            if len(cmp_word) != len(word):
                continue
            
            if can_chage(word, cmp_word):
                graph[i].append(end_idx)
    
    #print(graph)
    
    #최소 변환이니 BFS로 횟수랑 함께 넣고 풀면 빠를듯.
    #시작을 어디서 해야하는가?
    #시작할 수 있는 애들 인덱스 구하기
    start_idx = []
    for idx, cmp_word in enumerate(words):
        #똑같은 경우는 없겠지?
        if can_chage(begin, cmp_word):
            start_idx.append(idx)

    min_cnt = float('inf')

    for start_node in start_idx:
        #이미 start_node로 한단계 움직인것
        min_cnt = min(min_cnt, BFS(start_node, target, graph, words))
    
    if min_cnt == float('inf'):
        answer = 0
    else:
        answer = min_cnt

    #print(answer)

    return answer


#solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])