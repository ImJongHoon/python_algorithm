from collections import deque
#스택 사용
#곱셈의 분배 법칙을 떠올려야 함.
#종속과 결합을 구분하는 방법인데, 종속을 먼저 모두 생각하고 결합을 생각하는 것.

def main():
    input_str = list(input())
    #print(input_str)
    # ( 2의 x승, [ 3의 x승
    st = deque()
    calc_st = deque()
    result = 0
    score = 0

    two_cnt = 0
    three_cnt = 0
    #닫는 괄호시 pop,
    #즉 닫는 괄호가 연속해서 오거나 마지막에 st가 남아있으면 out
    is_open = 0
    for elem in input_str:
        if elem == ")":
            if not st or st[-1] != "(":
                result = -1
                break
            if is_open == 1:
                score += 2**two_cnt * 3**three_cnt
            two_cnt -= 1

            st.pop()
            is_open = 0

        elif elem == "]":
            if not st or st[-1] != "[":
                result = -1
                break
            if is_open == 1:
                score += 2**two_cnt * 3**three_cnt
            three_cnt -= 1

            st.pop()
            is_open = 0

        elif elem == "(":#이미 여는 괄호가 남았으면 덧셈, 아님 곱셈
            two_cnt += 1
            is_open = 1

            st.append(elem)

        elif elem == "[":
            three_cnt += 1
            is_open = 1

            st.append(elem)
        #print(st)

    #stack 내부 값이 남았으면
    if st:
        result = -1

    if result == -1:
        score = 0

    print(score)

if __name__ == "__main__":
    main()

