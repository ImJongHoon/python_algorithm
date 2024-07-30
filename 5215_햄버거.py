import sys
sys.stdin = open("input.txt", "r")

T = int(input())

max_score = 0
def DFS(foods, max_cal, cur_cal, cur_score, idx):
    global max_score

    if cur_cal > max_cal:
        return

    if len(foods) <= idx:
        max_score = max(max_score, cur_score)
        return

    temp_score = cur_score + foods[idx][0]
    temp_cal = cur_cal + foods[idx][1]
    DFS(foods, max_cal, temp_cal, temp_score, idx+1)
    DFS(foods, max_cal, cur_cal, cur_score, idx+1)



def main():
    global max_score
    for test_case in range(1, T + 1):
        max_score = 0

        num, max_cal = map(int, input().split())
        foods = [list(map(int,input().split())) for _ in range(num)]
        #print(foods)
        DFS(foods, max_cal, 0, 0,0)
        print(f"#{test_case} {max_score}")


if __name__ == "__main__":
    main()