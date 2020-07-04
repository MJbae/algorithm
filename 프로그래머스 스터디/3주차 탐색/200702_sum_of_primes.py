'''
주요 논리
가. 에라토스테네스의 체 활용, n 이하의 소수를 primes에 저장
다. itertools의 combination 활용, primes의 3개 요소로 이루어진 조합 구하기
나. 위에서 구한 조합의 합이 n과 같은 경우의 수를 반환
'''
from itertools import combinations


def solution(n):
    answer = 0
    check_prime = [False] * 2 + [True] * (n - 1)
    primes = []

    for index, value in enumerate(check_prime):
        if value:
            primes.append(index)
            for j in range(index * 2, n + 1, index):
                check_prime[j] = False

    combinations_prime = list(combinations(primes, 3))

    for combination in combinations_prime:
        if sum(combination) == n:
            answer += 1

    return answer