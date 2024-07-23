import sys
sys.stdin = open("input.txt", "r")

SIZE = 100

# 좌 우 상
dy = [0, 0, -1]
dx = [-1, 1, 0]

T = 10

board = []
# visited [][] 곱곱으로 생성시 포인터로 같은 값이 변함
visited = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
def BFS(board, y, x):
    # print(f"y: {y}, x: {x}")
    q = []
    q.append((y,x))

    while len(q) != 0:
        top = q.pop(0)
        for i in range(3):
            ny = top[0] + dy[i]
            nx = top[1] + dx[i]
            #print(f"ny: {ny}, nx: {nx}")

            if ny < 0 or nx < 0 or ny >= SIZE or nx >= SIZE or board[ny][nx] == 0 or visited[ny][nx] == 1:
                continue
            elif ny == 0:
                return nx
            else:
                visited[ny][nx] = 1
                q.append((ny, nx))
                break



for test_case in range(1, T + 1):
    tc = int(input())
    board = [list(map(int, input().split())) for _ in range(SIZE)]

    # 방문처리 초기화
    visited = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

    # print(board)

    # 시작지점 찾기
    start_x = 0
    end_x = -1
    for idx, num in enumerate(board[SIZE - 1]):
        if num == 2:
            start_x = idx

    visited[SIZE - 1][start_x] = 1

    # print(board[SIZE-1][start_x])

    end_x = BFS(board, SIZE - 1, start_x)

    print(f"#{tc} {end_x}")



