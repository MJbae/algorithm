'''
주요 논리: answer는 target(brown + red)의 약수 중 값의 차이가 가장 작은 두 요소로 볼 수 있음
가. target(brown + red)의 모든 약수를 divisors 리스트에 append함
다. divisors의 크기가 짝수이면 약수 간 차이가 가장 적은 요소 두 개를 반환
나. divisors의 크기가 홀수이면 divisors 요소 중 가장 가운데 값을 두 번 반환
'''

def solution(brown, red):
    target = brown + red
    divisors = []
    answer = []

    for i in range(1, target + 1):
        if target % i == 0:
            divisors.append(i)
    ANSWER_INDEX = len(divisors) // 2

    if len(divisors) % 2 == 0:
        answer.append(divisors[ANSWER_INDEX])
        answer.append(divisors[ANSWER_INDEX - 1])
    else:
        answer.append(divisors[ANSWER_INDEX])
        answer.append(divisors[ANSWER_INDEX])

    return answer