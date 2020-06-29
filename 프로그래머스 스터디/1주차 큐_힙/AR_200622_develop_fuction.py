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

문제를 다시 보시면 상단 코드의 어쩌고 저쩌고 코드가 나옴 영역에 queue.popleft()를 하는 부분이 있습니다.
따라서 if not queue는 for문이 처음시작될 때에는 중복체크를 하게 되지만, for문이 두번째 도는 순간부터는 중복 체크가 아니게됩니다.
for문을 돌다보면 더 이상 queue에 원소가 남아있지 않게 될테니깐요.


                
2. 본 문제를 큐가 아닌 일반 반복문(주석처리한 부분)으로 풀어봤습니다. for in 구문으로 리스트 값에 접근하면
큐와 같이 FIFO로 문제를 해결할 수 있는 것으로 보입니다. 큐를 썼을 때, 어떤 이점이 있는 지 모르겠습니다.
아니면 제가 큐를 제대로 활용하지 못한 건지 알고 싶습니다.

본 문제는 push, pop이 동시에 일어나지 않고 pop만 일어나는 문제이니, 사실 list를 사용하셔도 괜찮습니다.
queue로 분류한 것은 논리상 queue 를 써보기 좋은 문제라서 queue로 분류한 것이에요 :)


배운점: 큐의 활용법

시간복잡도 = O(N*M), N = 입력 리스트의 길이(len(pregresses)), M = 배포 날짜 크기(deployment_day)


이 코드는 시간복잡도를 구하기 다소 난처하게 짜여있네요.
일단 이 while문은 최악의 경우 99번 돕니다.(최악의 경우 = 작업 진도가 1이고, 작업 속도도 1일때 while문은 99번 돌음)
아마 말씀하신 M = 배포 날짜 크기(deployment_day) 의 M은 이 99라는 숫자를 의미하신것이겠지요?

앞선 33번째 줄의 while문은 len(speeds) 만큼 도니 말씀하신 것 처럼 O(NxM) 이라고 할 수 있겠네요.




추가 리뷰

다만 다음과 같이 단순한 나눗셈을 이용하면 while문을 이용하지 않고도 deployment_day를 바로 구할 수 있습니다.

deployment_day = ceil((100 - w_progresses) / now_speeds)
따라서 위 코드를 사용하여 while문을 제거하면 때문에 O(M)만큼 걸리는 행위를 O(1)만에 할 수 있게 됩니다.
그럼 전체 코드의 시간복잡도는 O(N)가 될겁니다.

다음 코드는 젠틀맨 님께서 작성한 코드를 아주 최소한으로 수정하여 만든 O(N) 코드입니다.

from collections import deque
from math import ceil

def solution(progresses, speeds):
    works_que = deque(zip(progresses, speeds))
    max_deployment_day = 0
    
    answer = []
    while works_que:
            w_progresses, now_speeds = works_que.popleft()
            
            deployment_day = ceil((100 - w_progresses) / now_speeds)
            if deployment_day > max_deployment_day:
                max_deployment_day = deployment_day
                answer.append(1)
            else:
                answer[-1] += 1
    return answer

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
