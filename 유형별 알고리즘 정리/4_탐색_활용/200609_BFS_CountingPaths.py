import sys
from _collections import deque
#sys.stdin = open("input", "r")

dx = [-1, 0 , 1, 0]
dy = [0 , 1, 0 , -1]

def DFS(layer, xNow, yNow):
    global countNum
    if xNow == 6 and yNow == 6:
        countNum += 1
        return
    else:
        for i in range(4):
            xNext = xNow + dx[i]
            yNext = yNow + dy[i]
            if 0 <= xNext <= 6 and 0 <= yNext <= 6:
                if inputList[xNext][yNext] == 0 and checkList[xNext][yNext] == 0:
                    checkList[xNext][yNext] = 1
                    DFS(layer+1, xNext, yNext)
                    checkList[xNext][yNext] = 0


if __name__ == "__main__":
    inputList = [list(map(int, input().split())) for _ in range(7)]
    countNum = 0
    checkList = [[0]*7 for _ in range(7)]
    checkList[0][0] = 1
    DFS(0, 0, 0)
    print(countNum)
