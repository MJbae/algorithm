import sys
#sys.stdin = open("input", "r")

def DFS(layer, subTime, subScore):
    global maxSore
    if subTime > m:
        return
    else:
        for j in range(n):
            if checkList[j] == 0:
                checkList[j] = 1
                if maxSore < subScore:
                    maxSore = subScore
                DFS(layer + 1, subTime + inputTime[j], subScore + inputScore[j])
                checkList[j] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    inputScore = []
    inputTime = []
    checkList = [0]*(n)
    for _ in range(n):
        tmp1, tmp2 = map(int, input().split())
        inputScore.append(tmp1)
        inputTime.append(tmp2)
    maxSore = -2147000000
    DFS(0, 0, 0)
    print(maxSore)