def solution(N, number):
    answer = 0

    #최솟값이 8보다 크면 반환
    MAX_NUM = 8
    num_set = [set() for _ in range(MAX_NUM)]

    for idx, cur_set in enumerate(num_set, start = 1):
        cur_set.add(int(str(N) * idx))

    for i in range(len(num_set)):
        for j in range(i):
            for operator1 in num_set[j]:
                for operator2 in num_set[i-j-1]:
                    num_set[i].add(operator1 + operator2)
                    num_set[i].add(operator1 - operator2)
                    num_set[i].add(operator1 * operator2)
                    if operator2 != 0:
                        num_set[i].add(operator1 // operator2)
        
        if number in num_set[i]:
            answer = i + 1
            break
        else:
            answer = -1
    return answer

solution(5, 12)