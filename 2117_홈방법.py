import sys
sys.stdin = open("input.txt", "r")

def search_home(board, k, start_y, start_x, pay, board_size):
    size = 2 * k - 1
    cnt = 0
    visited = [[0] * board_size for _ in range(board_size)]
    #print("start: ", start_y, start_x)
#다이아몬드 돌기만 생각
    print("size", size)
    for dy in range(size):
        for dx in range(size):
            ny = start_y + dy
            nx = start_x + dx
            #print(ny, nx)
            if ny < 0 or nx < 0 or ny >= board_size or nx >= board_size:
                continue

#다이아몬드 범위 판단

            print("ny열: ", abs(size // 2 - ny), size-abs(size // 2 - ny)+1)
            # if nx >= abs(size // 2 - ny) and nx < size - abs(size // 2 - ny):
            #     visited[ny][nx] = 1
            #     #print((ny, nx), end=" ")
            #     #다이아몬드 범위 내에 몇개 있는지?
            #     if board[ny][nx] == 1:
            #         cnt += 1
    for li in visited:
        for elem in li:
            print(elem, end=" ")
        print()
    print()

                #print(board[y][x], end=" ")
    if k**2 + (k-1)**2 > cnt * pay:
        return True
    else:
        return False



#11시 40분
#다이아몬드 형태의 넓이 == k^2 + (k-1)^2
T = int(input())
def main():
    for test_case in range(1, T + 1):
        num, pay = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(num)]

        house_cnt = 0

        for li in board:
            for elem in li:
                if elem == 1:
                    house_cnt +=1

        result = 0
        i = 1

        #print(pay * house_cnt)
        while i**2 + (i-1)**2 <= pay * house_cnt:
            #print(i)
            size = 2 * i - 1
            #시작 좌표를 정해서 넣기
            for y in range(num + size * 2 - 1):
                for x in range(num + size * 2 - 1):
                    if search_home(board, i, y, x, pay, num):
                        result += 1
            i += 1

        print(f"#{test_case} {result}")

if __name__ == "__main__":
    main()