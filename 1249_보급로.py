from collections import deque
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

dy = [-1,0,1,0]
dx = [0,1,0,-1]

visited = []

def print_board(board):
    for li in board:
        print(li)
    print()
    print()
def BFS(board, start_y, start_x, size):
    visited[start_y][start_x] = board[start_y][start_x]
    q = deque([(start_y, start_x)])
    #print(board)

    while q:
        (y, x) = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= size or nx >= size:
                continue
            #print(board[ny][nx])

            if visited[ny][nx] <= visited[y][x] + board[ny][nx]:#가봤자 많으면
                continue
            else:
                q.append((ny, nx))

                visited[ny][nx] = visited[y][x] + board[ny][nx]
                print_board(visited)


    return
def main():
    for test_case in range(1, T + 1):
        num = int(input())
        board = [list(map(int, list(input()))) for _ in range(num)]


        global visited
        visited = [[987654321]*num for _ in range(num)]

        BFS(board, 0, 0, num)

        print(f"#{test_case} {visited[num-1][num-1]}")


if __name__ == "__main__":
    main()