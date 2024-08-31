def solution(n, times):
    answer = 0
    #최악의 시간구하기
    
    times.sort()
    #print(max_time)
    
    min_time_point = times[0] * 1
    max_time_point = times[-1] * n
    test_time = 1
    
    while min_time_point <= max_time_point:
        #해당 시간이 걸린다면
        test_time = (min_time_point + max_time_point) // 2
        print(test_time, min_time_point, max_time_point)
        can_people = 0
        for time in times:
            can_people += test_time // time
        
        #시간이 더 여유롭게 주어진 셈
        if can_people >= n:
            max_time_point = test_time - 1
            answer = test_time
        #시간이 여유롭지 않게 주어진셈
        elif can_people < n:
            min_time_point = test_time + 1
        #같으면
            
        
    print(answer)
    return answer

solution(6, [7, 10])