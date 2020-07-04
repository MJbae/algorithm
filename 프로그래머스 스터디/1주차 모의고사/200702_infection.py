'''
주요 논리
가. Queue에 infests 모든 요소를 삽입하는데, infests의 좌표정보 외 날짜 정보도 추가함
나. Queue가 빌때까지 아래 실행문을 반복
    1. Queue에서 leftpop한 값을 기준으로 4방위 값을 생성하여 반복
        가) 4방위 요소가 유효값이고 감염가능한 직원인지 체크함
        나) '가)' 조건에 해당하면 queue에 append하는데 이때 날짜 정보 1일 갱신함

* 데미 FloodFill 풀이와 스텔라 코드를 참고했습니다 :)
'''

from collections import deque


def solution(m, n, infests, vaccinateds):
    checked = [[False] * n for _ in range(m)]
    queue = deque()
    check_count = 0
    answer_day = 0

    for row, col in infests:
        checked[row - 1][col - 1] = True
        check_count += 1
        queue.append([row, col, answer_day])

    for row, col in vaccinateds:
        checked[row - 1][col - 1] = True
        check_count += 1

    while queue:
        now_row, now_col, now_day = queue.popleft()

        DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for d_row, d_col in DELTAS:
            next_row = now_row + d_row
            next_col = now_col + d_col
            next_day = now_day + 1

            if not (0 < next_row <= m and 0 < next_col <= n):
                continue

            if not checked[next_row - 1][next_col - 1]:
                checked[next_row - 1][next_col - 1] = True
                check_count += 1
                answer_day = next_day
                queue.append([next_row, next_col, next_day])

    if check_count < n * m:
        return -1
    return answer_day