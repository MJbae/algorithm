'''
200618_week1_기능개선

핵심아이디어
작업진도와 속도를 계산하여 각 작업이 완료되면 answer리스트에 결과를 반영함. 결과반영은 각각의 작업에 대해 이전 완료한 작업의 배포일자를
비교하고 이전 작업 보다 일찍 끝나면 answer 리스트 마지막 요소에 1을 더하고, 늦게 끝나면 1을 append한다.  

궁금한점
1. '큐 사용법 튜토리얼'에 따르면 아래와 같이 queue가 빈 경우 while 문을 빠져나오게 설계되었는데
바로 아래 코드에 'if not queue'를 통해 큐의 빈 경우를 중복 체크하는 것으로 보입니다. 중복 체크하는 이유가 있나요?
while queue:
        for server in servers:
            if not queue:
                break
                
2. 본 문제를 큐가 아닌 일반 반복문(주석처리한 부분)으로 풀어봤습니다. for in 구문으로 리스트 값에 접근하면
큐와 같이 FIFO로 문제를 해결할 수 있는 것으로 보입니다. 큐를 썼을 때, 어떤 이점이 있는 지 모르겠습니다.
아니면 제가 큐를 제대로 활용하지 못한 건지 알고 싶습니다.

배운점: 큐의 활용법

시간복잡도 = O(N*M), N = 입력 리스트의 길이(len(pregresses)), M = 배포 날짜 크기(deployment_day)
'''

from collections import deque

def solution(progresses, speeds):
    works_que = deque(zip(progresses, speeds))
    max_deployment_day = 0
    
    answer = []
    
    while works_que:
            if not works_que:
                break
                
            now_progresses, now_speeds = works_que.popleft()
            
            deployment_day = 1
            while True:
                if now_progresses + now_speeds*deployment_day >= 100:
                    if deployment_day > max_deployment_day:
                        max_deployment_day = deployment_day
                        answer.append(1)
                    else:
                        answer[-1] += 1
                    break
                deployment_day += 1
    return answer



'''  
def solution(progresses, speeds):
    answer = []
    max_deployment_day = 0
    
    for now_progresses, now_speeds in zip(progresses, speeds):
        deployment_day = 1
        
        while True:
            if now_progresses + now_speeds*deployment_day >= 100:
                if deployment_day > max_deployment_day:
                    max_deployment_day = deployment_day
                    answer.append(1)
                else:
                    answer[-1] += 1
                break
            deployment_day += 1
        
    return answer
                
'''
