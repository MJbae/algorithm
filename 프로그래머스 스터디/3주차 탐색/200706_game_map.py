'''
핵심논리: BFS 활용하여 탐색함. 매번 next 4방위 값이 유효할때마다 count += 1하여 정답을 찾음
'''
from collections import deque

def validate(n, m, next_row, next_col, checked):
    return 0 <= next_row < n and 0 <= next_col < m and checked[next_row][next_col]
        
def bfs(checked, n, m):
    queue = deque()
    queue.append([0, 0, 1])
    answer = n * m
    
    while queue:
        now_row, now_col, now_count = queue.popleft()
        DELTAS = ((1, 0), (0, -1), (-1, 0), (0, 1))
        
        for d_row, d_col in DELTAS:
            next_row = now_row + d_row
            next_col = now_col + d_col
            next_count = now_count + 1
            
            if not validate(n, m, next_row, next_col, checked):
                continue
            
            # 가장 빠른 방법이 answer에 저장됨
            if next_row == n - 1 and next_col == m - 1:
                answer = next_count
            
            checked[next_row][next_col] = False
            queue.append([next_row, next_col, next_count])
    
    return answer


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    checked = [[False] * m for _ in range(n)]
    for row, map_coordinate in enumerate(maps):
        for col, wall in enumerate(map_coordinate):
            if wall == 0:
                continue
            checked[row][col] = True 
    
    answer = bfs(checked, n, m)
    
    return answer if not checked[n - 1][m - 1] else -1