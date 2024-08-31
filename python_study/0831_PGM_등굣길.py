from collections import deque

def print_board(board):
    for li in board:
        for elem in li:
            print(elem, end=" ")
        print()
    print()

dy = [0, 1]
dx = [1, 0]

def find_path(board, size_x, size_y):
    queue = deque([])

    #y, x, 거리
    queue.append((0, 0))
    board[0][0] = 1

    while board[size_y-1][size_x-1] == 0:
        if not queue:
            break
        next_set = set()
        while queue:
            y, x = queue.popleft()

            for i in range(2):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if ny < 0 or nx < 0 or ny >= size_y or nx >= size_x:
                    continue
                if board[ny][nx] == -1:
                    continue
                
                next_set.add((ny, nx))
                board[ny][nx] += board[y][x]

        
        queue = deque(next_set)


    return board[size_y-1][size_x-1]

    

def solution(m, n, puddles):
    answer = 0
    board = [[0] * m for _ in range(n)]

    for x, y in puddles:
        board[y-1][x-1] = -1
    
    #print_board(board)

    #BFS같이 큐로
    
    cnt = find_path(board, m, n)

    print(cnt)
    answer = cnt % 1000000007
        
    return answer


solution(4, 3, [[3, 3], [4, 2]])