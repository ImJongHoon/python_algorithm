import sys
import itertools
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    half = N // 2

    # 식재료를 인덱스로 표현할거다
    # 식재료의 개수만큼 순차적으로 인덱스를 만들겁니다.
    num_list = [i for i in range(N)]

    def get_synergy_sum(food_list, synergy):
        synergy_pairs = itertools.combinations(food_list, 2)
        synergy_sum = 0
        for synergy_index in synergy_pairs:
            # i,j // j,i 둘다 더한 값이 시너지이기 때문에
            i, j = synergy_index
            synergy_sum += synergy[i][j] + synergy[j][i]
        return synergy_sum


    # A 요리와 B 요리는 식재료를 절반씩 가져간다.
    # 식재료를 절반씩 가져가는 모든 경우의 수를 구해야하죠. nCn//2
    food_comb_list = itertools.combinations(num_list, half)
    res = float('INF')  # 맛의 차이를 저장하는 변수 ( 최소값으로 갱신될 예정)

    for a_food_list in food_comb_list:
        # a 요리에 속하지 않은 레시피를 B요리 레시피 목록에 추가한다.
        # for num in num_list:
        #     if num not in a_food_list:
        #         b_food_list.append(num)
        b_food_list = [num for num in num_list if num not in a_food_list]
        print(a_food_list)
        a_synergy_sum = get_synergy_sum(a_food_list, synergy)
        b_synergy_sum = get_synergy_sum(a_food_list, synergy)

        print(type(a_synergy_sum))

        res = min(res, abs(a_synergy_sum - b_synergy_sum))

    print(f"#{test_case}")
