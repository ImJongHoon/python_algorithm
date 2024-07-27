def main():
    num1 = int(input())
    num2 = int(input())
    
    #index == 숫자로 계산하기 위해 +1 크기 배열 선언
    visited = [0 for _ in range(num2+1)]
    prime_li = []
    #n의 루트만큼 검사해도 판단 가능
    for i in range(num2 + 1)[2:]:
        #print(i)
        if visited[i] == 1:
            continue
        
        prime_li.append(i)
        cnt = 1

        while cnt * i <= num2:
            visited[cnt * i] = 1
            cnt += 1
            
    #print(prime_li)
    range_prime = []
    for prime in prime_li:
        if num1 <= prime:
            range_prime.append(prime)

    if not range_prime:
        print(-1)
    else:
        print(sum(range_prime))
        print(range_prime[0])

    #prime_li


if __name__ == "__main__":
    main()