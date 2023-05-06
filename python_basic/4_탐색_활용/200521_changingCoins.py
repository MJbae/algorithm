import sys
#sys.stdin = open("input", "r")


def DFS(layer, subSum):
    global countNum
    global count1
    count1 += 1
    if subSum > T:
        return
    if layer == k:
        if subSum == T:
            countNum += 1
        return
    else:
        for j in range(pennyCount[layer]+1):
            DFS(layer + 1, subSum + pennyValue[layer]*j)


if __name__ == "__main__":
    T = int(input())
    k = int(input())
    pennyValue = []
    pennyCount = []
    for i in range(k):
        n, m = map(int, input().split())
        pennyValue.append(n)
        pennyCount.append(m)
    countNum = 0
    count1 = 0
    DFS(0, 0)
    print(countNum)


