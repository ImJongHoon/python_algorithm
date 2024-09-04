import sys
sys.stdin = open("input.txt", "r")

min_vector = float("inf")

def DFS(vectors, minus_cnt, cur_minus_cnt, cur_idx, max_size, x, y):
    global min_vector
    #탈출조건: 도달시 비교
    if (cur_idx > max_size -1) and (cur_minus_cnt == minus_cnt):
        #print(x, y)
        min_vector = min(min_vector, (x*x + y*y))

    #가지치기1. 남은 idx를 다해도 minus를 다 입력할 수 없는 경우
    if((max_size - cur_idx - 1) < (minus_cnt - cur_minus_cnt)):
        return

    #가지치기2. cur_minus_cnt가 minus를 넘은 경우
    if cur_minus_cnt > minus_cnt:
        return

    #벡터를 더하는 경우
    DFS(vectors, minus_cnt, cur_minus_cnt, cur_idx+1, max_size, x + vectors[cur_idx][0], y + vectors[cur_idx][1])
    
    #벡터를 빼는 경우
    DFS(vectors, minus_cnt, cur_minus_cnt + 1, cur_idx+1, max_size, x - vectors[cur_idx][0], y - vectors[cur_idx][1])

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        global min_vector
        min_vector = float("inf")

        num = int(input())
        minus_cnt = num // 2

        vectors = [list(map(int, input().split())) for _ in range(num)]

        DFS(vectors, minus_cnt, 0, 0, num, 0, 0)

        print(f"#{test_case} {min_vector}")

if __name__ == "__main__":
    main()