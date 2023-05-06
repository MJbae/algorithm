import sys
#sys.stdin = open("input", "r")

def DFS(layer):
    global cntNum
    if layer == m:
        for k in resultList:
            print(k, end=" ")
        print()
        cntNum += 1

    else:
        for j in range(1, n+1):
            resultList[layer] = j
            DFS(layer+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    cntNum = 0
    resultList = [0] * m
    DFS(0)
    print(cntNum)