import heapq
from collections import deque

def solution(healths, items):
    healths.sort()
    items = [(*item, idx) for idx, item in enumerate(items, 1)]
    BUFF, DEBUFF, INDEX = 0, 1, 2
    items.sort(key=lambda x: x[DEBUFF])
    items = deque(items)

    candidates = []
    answer = []

    for health in healths:
        while items and health - items[0][DEBUFF] >= 100:
            item = items.popleft()
            heapq.heappush(candidates, (-item[BUFF], item[INDEX]))
        if candidates:
            answer.append(heapq.heappop(candidates)[1])        

    answer.sort()
    return answer