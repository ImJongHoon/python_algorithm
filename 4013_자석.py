from collections import deque
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

MAGNET_NUM = 4

dy = [1, -1]
dx = [4, -4]

def main():
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        num = int(input())
        board = [list(map(int, input().split())) for _ in range(MAGNET_NUM)]
        change = [list(map(int, input().split())) for _ in range(num)]

        print(board)
        print(change)

        for mag_idx, direction in change:
            q = deque([(mag_idx, direction)])
            while q:
                cur_mag, direction = q.popleft()
                if direction == 1:#시계 방향
                    board[cur_mag - 1] = board[cur_mag-1][-1] + board[cur_mag-1][:-1]
                elif direction == -1:#반시계 방향
                    board[cur_mag - 1] = board[cur_mag-1][1:] + board[cur_mag-1][:1]

                print(board[cur_mag-1])

                #다음 좌표
                for i in range(2):
                    #내부에서 추가해주기
                    pass

                board[cur_mag-1]

        #점수 합산
        cnt = 0
        for idx, li in enumerate(board):
            cnt += 2 ** idx

        print(f"#{test_case} {cnt}")

if __name__ == "__main__":
    main()