
def dfs(input_li, idx):
    #print(idx)
    if idx == -1:
        return
    #print(input_li[idx])
    dfs(input_li, int(input_li[idx][2]) -1)
    print(input_li[idx][1], end="")
    dfs(input_li, int(input_li[idx][3]) -1)

    return

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    input_li = [list(input().split()) for _ in range(num)]

    for li in input_li:
        if len(li) < 4:
            while len(li) < 4:
                li.append(0)
    #print(input_li)
    print(f"#{test_case}", end=" ")
    dfs(input_li, 0)
    print()
    
    #print(input_li)
