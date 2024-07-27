T = int(input())

def is_slope(li, size_x)->int:
    free_space = 1

#주어진 input에서 경사가 증가하면 과연 맞는지 따지는 게 아니라,
#진짜 경사가 증가하려면 input에서 값이 증가하는 것과 동시에 그 조건을 만족하는지
#확인해주는 과정을 같이 넣으면 훨씬 코드가 간결해짐
    for i in range(1, len(li)):
        if(abs(li[i-1] - li[i]) >= 2):
            return 0
        if(li[i-1] == li[i]):
            free_space += 1
        elif (li[i-1] < li[i]) and (free_space >= size_x):#경사 증가 하려면
            free_space = 1

        elif li[i-1] > li[i] and (free_space >= 0):#경사 감소
            free_space = -size_x+1 # -1 + 1
        else:
            return 0

    if free_space >= 0:
        #print(li)
        return 1
    else:
        return 0

                
                

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num, size_x = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(num)]

    #테스트할 라인마다 입력
    test_line = [0]*num

    count = 0

    for y in range(num):
        for x in range(num):
            test_line[x] = board[y][x]
        count += is_slope(test_line, size_x)
    for y in range(num):
        for x in range(num):
            test_line[x] = board[x][y]
        count += is_slope(test_line, size_x)
    
    print(f"#{test_case} {count}")


