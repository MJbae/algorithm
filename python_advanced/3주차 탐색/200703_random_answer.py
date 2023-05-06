# 모범답안 참고하여 개선한 풀이
def solution(answers):
    result = []
    ANSWERS_SIZE = len(answers)
    FIRST_PATTERN = [1, 2, 3, 4, 5]
    SECOND_PATTERN = [2, 1, 2, 3, 2, 4, 2, 5]
    THIRD_PATTERN = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    counts = [0, 0, 0]
    SIZES = [5, 8, 10]

    for idx, answer in enumerate(answers):
        if answer == FIRST_PATTERN[idx % SIZES[0]]:
            counts[0] += 1
        if answer == SECOND_PATTERN[idx % SIZES[1]]:
            counts[1] += 1
        if answer == THIRD_PATTERN[idx % SIZES[2]]:
            counts[2] += 1

    max_count = max(counts)
    for idx, count in enumerate(counts):
        if max_count == count:
            result.append(idx + 1)

    return result




# 모범 답안! 간소화된 부분을 참고하자
'''
def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

'''

# 첫번째 풀이, 간소화할 부분이 굉장히 많다
'''
def solution(answers):
    answer = []
    ANSWERS_SIZE = len(answers)
    FIRST_SIZE = 5
    SECOND_SIZE = 8
    THIRD_SIZE = 10
    FIRST_PATTERN = [1, 2, 3, 4, 5]
    SECOND_PATTERN = [2 ,1, 2, 3, 2, 4, 2, 5]
    THIRD_PATTERN = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    first_count = 0
    second_count = 0
    third_count = 0

    first_loser = FIRST_PATTERN*(ANSWERS_SIZE // FIRST_SIZE) + FIRST_PATTERN[ : ANSWERS_SIZE % FIRST_SIZE]
    second_loser = SECOND_PATTERN*(ANSWERS_SIZE // SECOND_SIZE) + SECOND_PATTERN[ : ANSWERS_SIZE % SECOND_SIZE]
    third_loser = THIRD_PATTERN*(ANSWERS_SIZE // THIRD_SIZE) + THIRD_PATTERN[ : ANSWERS_SIZE % THIRD_SIZE]

    for index, each_answer in enumerate(answers):
        if each_answer == first_loser[index]:
            first_count += 1
        if each_answer == second_loser[index]:
            second_count += 1
        if each_answer == third_loser[index]:
            third_count += 1

    max_count = max(first_count, second_count, third_count)
    if first_count == max_count:
        answer.append(1)
    if second_count == max_count:
        answer.append(2)
    if third_count == max_count:
        answer.append(3)

    return answer
'''