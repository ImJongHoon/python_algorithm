from collections import deque
from copy import deepcopy
import sys
sys.stdin = open("input.txt", "r")

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

max_core = (float("-inf"), float("-inf"))

def print_board(board):
    for li in board:
        for elem in li:
            print(elem, end=" ")
        print()
    print()

def BFS(core, num, cur_core, cur_dir, board):
    is_connected = 0
    add_wire_length = 0
    
    queue = deque([])
    #y, x, add_wire_length
    queue.append((core[cur_core][0], core[cur_core][1], 0))
    while queue:
        y, x, length = queue.popleft()
        ny = y + dy[cur_dir]
        nx = x + dx[cur_dir]
        
        #끝까지 가면 (방문처리와 같음)
        if ny < 0 or nx < 0 or ny >= num or nx >= num:
            is_connected = 1
            add_wire_length = length
            return(is_connected, add_wire_length)
        
        if board[ny][nx] == 1:
            return(is_connected, add_wire_length)
        
        queue.append((ny, nx, length+1))



def select_core_dir(core, num, cur_core, cur_dir, connected_core, wire, board):
    global max_core
    if len(core) <= cur_core:
        #갯수 길이 계산. 튜플로 만들되 갯수는 그냥, 전선 길이는 음수로 넣기
        max_core = max(max_core, (connected_core, -wire))
        return
    
    #가지치기: 남은 core 수 + 현재 core 수 < 최대 코어수 인 경우
    if max_core[0] > connected_core + (len(core) - (cur_core)):
        return
    
    #프로세서 가능 여부와, 가능시 선 길이, visited 계산

    is_connected, add_wire_length = BFS(core, num, cur_core, cur_dir, board)
        #처리
    if is_connected:
        c_board = deepcopy(board)
        for i in range(1, add_wire_length+1):
            ny = core[cur_core][0] + dy[cur_dir]*i
            nx = core[cur_core][1] + dx[cur_dir]*i
            #print(num, add_wire_length, ny, nx)
            c_board[ny][nx] = 1
            # if ny < 0 or nx < 0 or ny>=num or nx>= num:
            #     print(ny, nx)
            #print_board(c_board)
    
    for dir in range(4):
        #처리
        if is_connected:
            select_core_dir(core, num, cur_core+1, dir, connected_core+1, wire+add_wire_length, c_board)
        else:
            select_core_dir(core, num, cur_core+1, dir, connected_core, wire, board)
            
def main():
    T = int(input())
    for test_case in range(1, T + 1):
        global max_core
        num = int(input())
        board = [list(map(int, input().split())) for _ in range(num)]
        
        #코어는 최대한 많이 연결
        #같은 코어수라면 선은 가장 짧게 연결
        #코어당 4방향 DFS
        #코어 좌표 받기
        core = []
        connected_core = 0
        wire = 0
        
        for y in range(num):
            for x in range(num):
                if board[y][x] == 1:
                    if y == 0 or x == 0 or y == num or x == num:
                        connected_core += 1
                    core.append((y, x))
        
                    
        #코어 갯수만큼 depth, 자식수는 방향수
        for dir in range(4):
            is_connected, add_wire_length = BFS(core, num, 0, dir, board)
            
            if is_connected:
                c_board = deepcopy(board)
                for i in range(1, add_wire_length+1):
                    ny = core[0][0] + dy[dir]*i
                    nx = core[0][1] + dx[dir]*i
                    c_board[ny][nx] = 1
                select_core_dir(core, num, 0, dir, connected_core+1, add_wire_length, c_board)
            else:
                select_core_dir(core, num, 0, dir, connected_core, wire, board)
        
        print(f"#{test_case} {-max_core[1]}")

if __name__ == "__main__":
    main()