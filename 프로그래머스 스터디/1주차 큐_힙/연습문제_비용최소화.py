import heapq
def solution(no, works):

    if no > sum(works):
        return 0
    
    works = [[-i, i] for i in works]
    heapq.heapify(works)
    
    for _ in range(no):
        work = heapq.heappop(works)[1] - 1
        heapq.heappush(works, [-work, work])

    return sum(value[1] ** 2 for value in works)