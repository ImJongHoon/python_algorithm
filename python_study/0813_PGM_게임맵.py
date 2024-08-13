from collections import deque

visited = []
dist = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def BFS(maps, size_y, size_x):
    global visited
    q = deque([])
    q.append((0,0,1))
    visited[0][0] = 1

    is_arrived = 0
    min_dist = 0

    while q:
        y, x, cur_dist = q.popleft()
        if y == size_y-1 and x == size_x-1:
            is_arrived = 1
            min_dist = cur_dist
            break
            

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= size_y or nx >= size_x:
                continue
            if visited[ny][nx] != 0:
                continue
            if maps[ny][nx] == 0:
                continue

            q.append((ny, nx, cur_dist+1))
            visited[ny][nx] = cur_dist + 1
    
    if is_arrived == 0:
        return -1
    else:
        return min_dist


def solution(maps):
    answer = 0
    global visited
    size_y = len(maps)
    size_x = len(maps[0])
    visited = [[0]*size_x for _ in range(size_y)]

    answer = BFS(maps, size_y, size_x)

    return answer
