import heapq

def solution(scoville, K):
    mix_count = 0
    heapq.heapify(scoville)

    while True:
        min_scoville = heapq.heappop(scoville)

        if min_scoville >= K:
            break

        if not scoville:
            return -1

        second_min_scoville = heapq.heappop(scoville)
        new_scoville = min_scoville + second_min_scoville * 2
        heapq.heappush(scoville, new_scoville)
        mix_count += 1

    return mix_count