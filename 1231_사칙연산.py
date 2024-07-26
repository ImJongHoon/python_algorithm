import sys
sys.stdin = open("input.txt", "r")

st=[]
def dfs(cal_arr, idx):
    #print(idx)
    if(idx == -2):

        return

    dfs(cal_arr, int(cal_arr[idx][1])-1)
    dfs(cal_arr, int(cal_arr[idx][2])-1)

    #후위 표기식으로 계산
    if cal_arr[idx][0] == "+":
        num1 = st.pop()
        num2 = st.pop()
        st.append(num2 + num1)
    elif cal_arr[idx][0] == "-":
        num1 = st.pop()
        num2 = st.pop()
        st.append(num2 - num1)
    elif cal_arr[idx][0] == "*":
        num1 = st.pop()
        num2 = st.pop()
        st.append(num2 * num1)
    elif cal_arr[idx][0] == "/":
        num1 = st.pop()
        num2 = st.pop()
        st.append(num2 // num1)
    else:
        # 피연산자가 왔을 경우
        st.append(int(cal_arr[idx][0]))

    #print(cal_arr[idx])
    return


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    # 수식 배열
    # 완전 이진 트리에만 해당되는 풀이
    input_arr = [input().split()[1:] for _ in range(num)]

    cal_arr = [[-1 for _ in range(3)] for _ in range(num)]

    for idx_y, li in enumerate(input_arr):
        for idx_x, elem in enumerate(li):
            cal_arr[idx_y][idx_x] = elem

    #print(cal_arr)

    result = dfs(cal_arr, 0)

    print(f"#{test_case} {st[-1]}")

    # 수식 배열 0을 채우고 시작했기 때문에
    # 왼쪽자식은 2n+1 오른쪽 자식은 2n+2가 된다