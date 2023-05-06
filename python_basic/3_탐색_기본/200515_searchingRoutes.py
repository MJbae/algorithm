import sys
#sys.stdin = open("input", "r")

def DFS(nodeNum):
    global countNum
    if nodeNum == n:
        countNum += 1
    else:
        for j in range(1, n+1):
            if matrixList[nodeNum][j] ==1 and checkList[nodeNum] == 0:
                checkList[nodeNum] = 1
                DFS(j)
                checkList[nodeNum] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrixList = [[0] * (n+1) for _ in range(n+1)]
    checkList = [0] * (n+1)
    countNum = 0

    for _ in range(m):
        nodeNum, lineNum = map(int, input().split())
        matrixList[nodeNum][lineNum] = 1

    DFS(1)
    print(countNum)