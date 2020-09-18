'''
from collections import deque

def solution(n, m, image):
    answer = 0
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                answer += 1
                visited[i][j] = True
                bfs(n, m, i, j, image, visited)

    return answer

def bfs(n, m, x, y, image, visited):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy

            if visitable(n, m, next_x, next_y, visited) and image[next_x][next_y] == image[x][y]:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True

def visitable(n, m, x, y, visited):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

FloodFill 논리
가. 모든 좌표를 하나씩 방문하면서 아래 조건 수행
    1. 방문하지 않은 좌표가 있다면 큐에 해당 좌표 append
    2. 큐가 빌때까지 아래 조건 수행
        가) 큐에 들어있는 좌표 leftpop 수행
        나) leftpop된 좌표에 대해 방문 체크
        다) leftpop된 좌표의 4방위 좌표를 큐에 append

세부논리
가. 변수생성
 - visited (방문여부)
나. images 모든 좌표 방문 이중 반복
    1. 특정 좌표 처음 방문(visited[i][j] == False) + answer += 1
    2. 방문 표시(visited[i][j] == True)
    3. append([i, j])
    4. 큐가 빌때가지 아래 조건 수행(while queue), 인접 좌표 중 같은 색깔의 그림을 모두 찾아내기 위함
        0) 4방위 좌표 생성 및 좌표의 제한 조건 걸기(if 0 <= next_i <= m 등)
        가) 4방위 좌표의 value와 현재좌표의 value를 비교(if image[i][j] == image[next_i][next_j])
        나) 위 조건 참인 경우 방문 표시하고 queue에 좌표값 append
'''
from collections import deque

def solution(n, m, image):
    
    '''
    본문의 경우 출력이 [[False, False, False][False, False, Fasle]]인 반면
    아래의 경우 [False, False, False, False, False, Fasls] 이와 같이 출력됨
    visited = [[False] for _ in range(m) for _ in range(n)]
    '''
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    answer = 0
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False:
                visited[i][j] = True
                queue.append([i, j])
                answer += 1
                
                while queue:
                    DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))
                    now_i, now_j = queue.popleft()
                    
                    '''
                    di, dj를 for문 아래에 선언할 필요 없음
                    for DELTA in DELTAS:
                        di, dj = DELTA
                        next_i = now_i + di
                        next_j = now_j + dj
                    '''
                    for di, dj in DELTAS:
                        next_i = now_i + di
                        next_j = now_j + dj
                    
                        '''
                        continue 문 사용함에 따라 아래 실행문을 들여쓰지 않아도 됨
                        if 0 <= next_i < n and 0 <= next_j < m and visited[next_i][next_j] == False:
                        '''
                        if not(0 <= next_i < n and 0 <= next_j < m and visited[next_i][next_j] == False):
                            continue
                            
                        if image[now_i][now_j] == image[next_i][next_j]:
                            visited[next_i][next_j] = True
                            queue.append([next_i, next_j])
    
    return answer