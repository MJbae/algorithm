import sys
#sys.stdin = open("input", "r")

def DFS(layer, sumNum):
    global minCnt
    if layer > minCnt:
        return
    if sumNum > maxNum:
        return
    if sumNum == maxNum:
        if minCnt > layer:
            minCnt = layer
    else:
        for j in range(n):
            DFS(layer+1, sumNum + inputList[j])


if __name__ == "__main__":
    n = int(input())
    inputList = list(map(int, input().split()))
    inputList.sort(reverse=True)
    maxNum = int(input())
    minCnt = 2147000000
    DFS(0, 0)
    print(minCnt)