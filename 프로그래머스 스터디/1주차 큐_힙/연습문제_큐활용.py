# 핵심아이디어: FIFO 방식으로 데이터 처리 시 queue 사용 적절
# 논리 전개
# 1. queue, cur_time 각 server 정의 및 생성
# 2. queue 내 모든 변수가 사라질 때까지 반복
#   1) severs 중 아이디 num이 적은 server부터 처리 시작
#     - queue가 비었으면 break
#     - server['finished_at'] <= cur_time이라면
#       * server['finished_at']에 queue.popleft()
#       * server['jobs_done'] += 1
#     - cur_time 증가
# 3. 반환(servers 중 각 server의 jobs_done matching value)

from collections import deque

def solution(n, exec_times):
    queue = deque(exec_times)

    # finished_at: 서버가 처리 중인 일이 끝나는 시각
    # jobs_done: 서버가 처리한 코드 수
    servers = [{'finished_at': 0, 'jobs_done': 0} for _ in range(n)]
    cur_time = 0

    while queue:
        for server in servers:
            if not queue:
                break
            if server['finished_at'] <= cur_time:
                server['finished_at'] += queue.popleft()

                server['jobs_done'] += 1
        cur_time += 1
    return [server['jobs_done'] for server in servers]