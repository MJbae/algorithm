import heapq


def solution(healths, items):
    answer = []

    # item별 id 생성
    item_id = 1
    for item in items:
        item.append(item_id)
        item_id += 1

    # max heap 유지
    for item in items:
        item.insert(0, item[1] * -1)
    healths = [[-health, health] for health in healths]

    heapq.heapify(items)
    heapq.heapify(healths)

    # 체력 유지 가능 조건 하 공격력 최대 산출
    while items:
        now_item = heapq.heappop(items)
        now_health = heapq.heappop(healths)

        if now_health[1] - now_item[2] >= 100:
            answer.append(now_item[3])
        else:
            heapq.heappush(healths, now_health)

    return sorted(answer)
