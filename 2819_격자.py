import sys
sys.stdin = open("input.txt", "r")

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

SIZE = 4

def find_num(board, y, x, cnt, num_str, num_set):
    if cnt >= 7:
        #set에 추가
        #print(num_str)
        num_set.add(num_str)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if(ny < 0 or nx < 0 or ny >= SIZE or nx >= SIZE):
            continue
        find_num(board, ny, nx, cnt+1, num_str + board[ny][nx], num_set)

    return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    board = [input().split() for _ in range(SIZE)]

    num_set = set()
    #print(board)

    for y in range(SIZE):
        for x in range(SIZE):
            find_num(board, y, x, 1, board[y][x], num_set)



    print(f"#{test_case} {len(num_set)}")
    pass