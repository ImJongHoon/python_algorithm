import heapq

def solution(scoville, K):
    answer = -1
    heapq.heapify(scoville)

    cnt = 0
    #탈출하면 -1 출력
    while len(scoville) > 1:
        top = heapq.heappop(scoville)
        if top >= K:
            answer = cnt
            break

        second = heapq.heappop(scoville)
        heapq.heappush(scoville, (top + (second*2)))
        cnt += 1

    top = heapq.heappop(scoville)
    
    if top >= K:
        answer = cnt
    #print(answer)
    return answer