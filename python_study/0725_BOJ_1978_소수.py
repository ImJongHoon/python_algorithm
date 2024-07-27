# 1978 소수 찾기
def main():
    num = int(input())
    input_li = list(map(int, input().split()))
    #에라토스테네스의 체
    #목록 중 가장 큰 수까지의 숫자 목록을 생성하고,
    #소수 추가 => 배수 제거 => 소수 추가 => 배수 제거
    #를 반복하면서 소수 목록을 생성한다.
    max_num = max(input_li)
    prime_list = set()
    visited = [0 for _ in range(max_num + 1)]
    for idx in range(max_num+1)[2:]:#2부터 시작
        #파이썬은 반복문 도중에 원본 리스트를 훼손해도 반복문에 출력되는 값이 유지된다
        if visited[idx] == -1:
            continue
        #print(num_list[idx])
        prime_list.add(idx)
        cnt = 1
        while idx * cnt <= max_num:
            visited[idx * cnt] = -1
            cnt += 1
    #print(prime_list)
    prime_cnt = 0
    for elem in input_li:
        if elem in prime_list:
            prime_cnt += 1
    print(prime_cnt)
if __name__ == "__main__":
    main()