import sys
#sys.stdin = open("input", "r")

def DFS(layer, subSum, totalSum):
    global resultNum
    if subSum + (totalNum - totalSum) < resultNum:
        return
    if subSum > c:
        return
    if layer == n:
        if subSum > resultNum:
            resultNum = subSum
    else:
        DFS(layer + 1, subSum + inputList[layer], totalSum + inputList[layer])
        DFS(layer + 1, subSum, totalSum + inputList[layer])


if __name__ == "__main__":
    c, n = map(int, input().split())
    inputList = [0] * n
    resultNum = 0
    for i in range(n):
        inputList[i] = int(input())
    totalNum = sum(inputList)
    DFS(0, 0, 0)
    print(resultNum)