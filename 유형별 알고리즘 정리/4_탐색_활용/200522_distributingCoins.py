import sys
#sys.stdin = open("input", "r")

def DFS(layer, aSum, bSum, cSum):
    global minGap
    if layer == n:
        if aSum == bSum or bSum == cSum or aSum == cSum:
            return
        tmpGap = max(aSum, bSum, cSum) - min(aSum, bSum, cSum)
        if tmpGap < minGap:
            minGap = tmpGap
    else:
        DFS(layer + 1, aSum + coinList[layer], bSum, cSum)
        DFS(layer + 1, aSum, bSum + coinList[layer], cSum)
        DFS(layer + 1, aSum, bSum, cSum + coinList[layer])


if __name__ == "__main__":
    n = int(input())
    coinList = []
    for _ in range(n):
        m = int(input())
        coinList.append(m)
    minGap = 21470000000
    DFS(0, 0, 0, 0)
    print(minGap)


