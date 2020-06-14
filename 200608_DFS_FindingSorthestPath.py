import sys
from collections import deque
#sys.stdin=open("input", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
inputList = [list(map(int, input().split())) for _ in range(7)]
distance = [[0]*7 for _ in range(7)]
dQ = deque()
dQ.append((0, 0))
inputList[0][0] = 1

while dQ:
    xyNow = dQ.popleft()
    for i in range(4):
        xNext = xyNow[0]+dx[i]
        yNext = xyNow[1]+dy[i]
        if 0 <= xNext <= 6 and 0 <= yNext <= 6 and inputList[xNext][yNext]==0:
            inputList[xNext][yNext] = 1
            distance[xNext][yNext] = distance[xyNow[0]][xyNow[1]]+1
            dQ.append((xNext, yNext))

if distance[6][6] == 0:
    print(-1)
else:
    print(distance[6][6])
