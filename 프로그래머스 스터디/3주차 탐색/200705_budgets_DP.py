'''
핵심논리: budgets을 오름차순 정렬 후, budgets 내 요소 중 최대값[budgets[:-1]]부터 시작하여 상한액 조건을 만족하는 경우를 찾음.
가. 상한액이 존재하지 않는 경우(sum(budgets) <= M)
나. 상한액이 존재하는 경우(sum(budgets) > M)
다. 상한액(answer)과 상한액이 적용되는 예산의 개수(nums_of_limit)를 변수로 설정 후, 관계식을 두 개 세움
    1. M - sum(budgets[ : -nums_of_limit ]) <= answer * nums_of_limit
    2. answer >= budgets[-(nums_of_limit+1)]
    3. 위의 두 가지 관계식을 answer를 기준으로 재정리하면 아래와 같이 정리할 수 있음
        - M >= sum(budgets[ : -nums_of_limit+1]) + nums_of_limit+1*budgets[-(nums_of_limit+1 + 1)]
    4. 정리된 식을 만족하는 nums_of_limit을 기준으로 두 개의 관계식으로 answer를 구할 수 있음
    
'''     

def solution(budgets, M):
    answer = 0
    if sum(budgets) <= M:
        return max(budgets)
    
    budgets.sort()
    
    # 예산 중 최저값이 총 예산 보다 작은 경우
    if budgets[0] < M:
        return M // len(budgets)

    for nums_of_limit in range(1, len(budgets)):
        if not(M >= sum(budgets[ : -nums_of_limit]) + nums_of_limit*budgets[-(nums_of_limit + 1)]):
            continue
            
        answer = (M - sum(budgets[ : -nums_of_limit ])) // nums_of_limit 
        if answer >= budgets[-(nums_of_limit+1)]:
            return answer