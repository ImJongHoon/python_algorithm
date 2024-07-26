from collections import deque
import sys
sys.stdin = open("input.txt", "r")

#맨홀에서 시작하는 시간 1
#움직이지 않고 가만히 있을 수 있음 == 한번 갔던 곳은 모두 존재 가능함
#BFS로 방문 처리했던 곳

#타입마다 갈 수 있는 곳이 다르기 때문에
#dyx[타입-1]
dyx = [[(-1, 0), (0, 1), (1, 0), (0, -1)],
       [(-1, 0), (1, 0)],
       [(0, 1), (0, -1)],
       [(-1, 0), (0, 1)],
       [(1, 0), (0, 1)],
       [(1, 0), (0, -1)],
       [(-1, 0), (0, -1)]]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def print_board(board):
    for li in board:
        print(li)
    print()
    print()

visited = []
def BFS(board, start_y, start_x, size_y, size_x, max_time):
    time = 1
    visited[start_y][start_x] = time
    q = deque([(start_y, start_x, time)])
    #print_board(visited)

    #print(q)
    #시간 count?
    while q:
        y, x, cur_time = q.popleft()

        for dy, dx in dyx[board[y][x] - 1]:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or ny >= size_y or nx >= size_x:
                continue
            if board[ny][nx] == 0:
                continue
            if visited[ny][nx] != 0:
                continue
            if cur_time >= max_time:
                continue
            # 다음 파이프에 따라 못 갈 수 있음. 이걸 계산해줘야함!
            # 어디서부터 왔는지에 따라 계산해줘야됨. 번거롭네
            if (-dy, -dx) in dyx[board[ny][nx]-1]:#되돌아갈 수 있다면!
                visited[ny][nx] = cur_time + 1
                q.append((ny, nx, cur_time + 1))
                #print(q)
                #print_board(visited)
            else:
                continue

    return

def main():
    for test_case in range(1, T + 1):
        size_y, size_x, start_y, start_x, max_time = map(int, input().split())

        board = [list(map(int, input().split())) for _ in range(size_y)]
        #print_board(board)

        global visited
        visited = [[0] * size_x for _ in range(size_y)]

        #print(board)
        #print(visited)

        BFS(board, start_y, start_x, size_y, size_x, max_time)

        cnt = 0
        for li in visited:
            for elem in li:
                if elem != 0:
                    cnt += 1

        print(f"#{test_case} {cnt}")


if __name__ == "__main__":
    main()


