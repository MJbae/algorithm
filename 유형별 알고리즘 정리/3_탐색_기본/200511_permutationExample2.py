import sys
#sys.stdin = open("input", "r")

def DFS(layer):
    global countNum
    if layer == m:
        for j in range(m):
            print(resultList[j], end=" ")
        print()
        countNum += 1
    else:
        for k in range(1, n + 1):
            if checkList[k] == 0:
                checkList[k] = 1
                resultList[layer] = k
                DFS(layer + 1)
                checkList[k] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    checkList = [0] * (n+1)
    resultList = [0] * m
    countNum = 0
    DFS(0)
    print(countNum)