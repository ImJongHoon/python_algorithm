def comb(arr, n):
    result = []
#원소가 하나일때까지 내려간거고
    if n == 1:
        return [[i] for i in arr] #n = 1 == 길이가 1
#첫번째 반복문이 어떤 것을 뺴고 선택하는지의 경우에 대해.
    for i in range(len(arr)):#i가 위치
        elem = arr[i]
        for rest in comb(arr[i+1:], n-1):
            #남은 놈이랑 배열을 합치는 코드
            result.append([elem] + rest)
    return result
tall = [input() for _ in range(9)]
#print(comb(tall, 7))
for li in comb(tall, 7):
    temp = list(map(int, li))
    #print(temp)
    if sum(temp) == 100:
        temp.sort()
        for elem in temp:
            print(elem)
        break