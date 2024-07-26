import sys
sys.stdin = open("input.txt", "r")

st=[]
def dfs(cal_arr, idx):
    if(idx >= len(cal_arr)):
        return
    # 방문 === 계산 을 후위순회로 처리.
    # 계산 결과를 반환 받아야 다음 계산에 사용함
    dfs(cal_arr, 2*idx + 1)
    dfs(cal_arr, 2*idx + 2)

    #후위 표기식으로 계산
    if cal_arr[idx] == "+":
        num1 = st.pop()
        num2 = st.pop()
        st.append(str(int(num2) + int(num1)))
    elif cal_arr[idx] == "-":
        num1 = st.pop()
        num2 = st.pop()
        st.append(str(int(num2) - int(num1)))
    elif cal_arr[idx] == "*":
        num1 = st.pop()
        num2 = st.pop()
        st.append(str(int(num2) * int(num1)))
    elif cal_arr[idx] == "/":
        num1 = st.pop()
        num2 = st.pop()
        st.append(str(float(int(num2) / int(num1))))
    else:
        # 피연산자가 왔을 경우
        st.append(cal_arr[idx])
        pass

    return


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    # 수식 배열
    # 완전 이진 트리에만 해당되는 풀이
    cal_arr = [input().split()[1] for _ in range(num)]

    result = dfs(cal_arr, 0)

    print(f"{test_case} {st[-1]}")

    # 수식 배열 0을 채우고 시작했기 때문에
    # 왼쪽자식은 2n+1 오른쪽 자식은 2n+2가 된다

