from collections import deque
import sys
sys.stdin = open("input.txt", "r")

#상하좌우 좌표 기준이므로 이동과 다름
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

SIZE_Y = 2001
SIZE_X = 2001

T = int(input())

visited = []

def BFS(atom_info):
    global visited
    #초기화
    score = 0
    visited = [[-1] * SIZE_X*2 for _ in range(SIZE_Y*2)]

    # x좌표, y좌표, 이동방향, 보유에너지k, 이동거리
    for li in atom_info:
        li[0] = 2*(li[0] + 1000)
        li[1] = 2*(li[1] + 1000)
        li.append(1)


    q = deque(atom_info)
    #print(len(q))

    while q:
        x, y, direction, point, dist = q.popleft()
        #print(q)

        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx < 0 or ny < 0 or nx >= SIZE_X*2 or ny >= SIZE_Y*2:
            #print(nx, ny)
            continue

        # 같은 자리
        # nx, ny, dist 인 놈을 찾거나, nx ny dist+1 인 놈이 충돌임
        new_q = []
        #print(point)
        is_conflict = 0

        if visited[nx][ny] == dist+1:
            #print(x, y, direction, point, dist)
            #print(q)
            for elem in q:
                if elem[0] == nx and elem[1] == ny and elem[4] == dist+1:
                    #print(f"충돌: {elem}")
                    score += point
                    score += elem[3]
                    is_conflict = 1
                    #print(point)
                    #print(score)
                    continue


                new_q.append(elem)
            q = deque(new_q)
            #print(q)
            #print()


        visited[nx][ny] = dist+1
        if is_conflict == 0:
            q.append([nx, ny, direction, point, dist+1])

    return score

def main():
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        num = int(input())
        #x좌표, y좌표, 이동방향, 보유에너지k
        #원자 최대 1000개
        atom_info = [list(map(int, input().split())) for _ in range(num)]
        #print(atom_info)

        score = BFS(atom_info)

        print(f"#{test_case} {score}")

if __name__ == "__main__":
    main()