from collections import deque
import sys
sys.stdin = open("input.txt", "r")

#상우하좌 좌상, 우상, 좌하, 우하
dy = [-1, 0, 1, 0, -1, -1, 1, 1]
dx = [0, 1, 0, -1, -1, 1, -1, 1]

def print_board(board):
    for li in board:
        for elem in li:
            print(elem, end=" ")
        print()
    print()
    
def BFS(board, visited, size, start_y, start_x):
    cnt = 0
    queue = deque([])
    
    visited[start_y][start_x] = 1
    queue.append((start_y, start_x))
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= size or nx >= size:
                continue
            if visited[ny][nx] == 1:
                continue
            if board[ny][nx] != 0:
                visited[ny][nx] = 1
                continue
            
            queue.append((ny, nx))
            visited[ny][nx] = 1
    
    return cnt

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        size = int(input())
        input_str = [input() for _ in range(size)]
        
        #2차원 배열 입력하기
        #숫자로.
        board = [[0] * size for _ in range(size)]
        visited = [[0] * size for _ in range(size)]
        for y in range(size):
            for x in range(size):
                if input_str[y][x] == '*':
                    board[y][x] = -1
                    visited[y][x] = 1
                    continue
                
                cnt = 0
                for i in range(8):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or nx < 0 or ny >= size or nx >= size:
                        continue
                    if input_str[ny][nx] != ".":
                        cnt += 1
                
                board[y][x] = cnt
            
        #print_board(board)
        
        #visited를 기준으로
        # 0이 나오는 곳에서 BFS한 횟수 + visited에서 남은 0
        click_cnt = 0
        for y in range(size):
            for x in range(size):
                if board[y][x] == 0 and visited[y][x] != 1:
                    BFS(board, visited, size, y, x)
                    click_cnt += 1
        
        for li in visited:
            for elem in li:
                if elem != 1:
                    click_cnt += 1
                
        
        print(f"#{test_case} {click_cnt}")

if __name__ == "__main__":
    main()