'''
핵심아이디어: 야근 피로도 = works 각 요소 제곱하여 더한 값
가. works 각 요소를 n번 깍아서 야근 피로도를 최소화할 것
    1. n번 반복문 실행하면서
    2. works를 max_heap 유지하는 상태에서 max 요소를 1만큼 감소함
나. 위의 과정을 거친 works의 모든 요소를 제곱하여 더한 값이 정답
예외사항
    1. sum(works) > n 이면 answer = 0
'''
import heapq

def solution(no, works):
    answer = 0
    
    if no > sum(works):
        return 0    
    
    # 다음과 같이 -1를 곱해서 절대값 기준 max_heap 유지 가능
    works = [work * -1 for work in works]
    heapq.heapify(works)
    
    for _ in range(no):
        work = heapq.heappop(works)
        heapq.heappush(works, work + 1)
        '''
        이하를 위와 같이 간소화할 수 있음 
        work += 1
        heapq.heappush(works, work)
        '''        
    
    answer = sum(work ** 2 for work in works)
    '''
    이하를 위와 같이 한줄로 정리할 수 있음
    for work in works:
        answer += work * work
    '''
    return answer