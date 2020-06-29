'''
200617_큐 사용법 튜토리얼

배운점
1. deque 모듈의 기본적인 활용법
2. dictionary 자료형의 아름다운 활용
'''

from collections import deque

def solution(n, exec_times):
    queue = deque(exec_times)

    # finished_at: 서버가 처리 중인 일이 끝나는 시각
    # jobs_done: 서버가 처리한 코드 수
    # servers list에 서버의 수(n)만큼 dictionary 자료형을 대입하여 각 서버의 작업 수와 끝나는 시간을 키값으로 둠
    servers = [{'finished_at': 0, 'jobs_done': 0} for _ in range(n)]
    cur_time = 0

    while queue:
        for server in servers:
            print("도입 ", server, cur_time, queue)
            if not queue:
                break
            if server['finished_at'] <= cur_time:
                server['finished_at'] += queue.popleft()

                server['jobs_done'] += 1
        cur_time += 1
        print("끝 ", servers, cur_time, queue)
    return [server['jobs_done'] for server in servers]


if __name__ == "__main__":
    n = 3
    exec_times = [3, 1, 1, 2, 1, 5]
    print(solution(n, exec_times))
