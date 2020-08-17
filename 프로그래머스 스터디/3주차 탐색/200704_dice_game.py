'''
핵심아이디어
확률 = (모든 경우의 수 - monster 배열 요소에 놓일 경우의 수) / 모든 경우의 수 * 1000

모든 경우의 수 = 순열(S1 모든 경우, S2 모든 경우, S3 모든 경우)
monster 배열 요소 경우의 수 = sum(S1 요소, S2 요소, S3 요소)

'''
from itertools import product
import math

def solution(monster, S1, S2, S3):
    answer = 0
    S1_range = list(range(1, S1 + 1))
    S2_range = list(range(1, S2 + 1))
    S3_range = list(range(1, S3 + 1))
    
    all_cases = list(product(S1_range, S2_range, S3_range))
    monster_case = {case - 1 : 0 for case in monster}
    
    for case in all_cases:
        for key, value in monster_case.items():
            if sum(case) == key:
                monster_case[key] += 1
    
    MONSTER_CASE = sum(monster_case.values())
    ALL_CASE = len(all_cases)        
                
    answer = (ALL_CASE-MONSTER_CASE) / ALL_CASE * 1000
    
    return math.trunc(answer)