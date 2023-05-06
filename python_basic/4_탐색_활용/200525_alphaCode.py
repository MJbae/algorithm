import sys

#sys.stdin = open("input", "r")


def DFS(layer):
    #print(inList, rstList, layer)
    global countNum
    if len(inList) == 0:
        for j in range(len(rstList)):
            print(chr(rstList[j]+64), end="")
        print()
        countNum += 1
    else:
        tmp1 = inList[0]
        if 1 <= tmp1 <= 26:
            rstList.append(tmp1)
            inList.pop(0)
            DFS(layer + 1)
            inList.insert(0, tmp1)
            rstList.pop()
        else:
            return

        if len(inList) <= 1:
            return
        else:
            tmp2 = inList[0] * 10 + inList[1]
            if 1 <= tmp2 <= 26:
                inList.pop(0)
                inList.pop(0)
                rstList.append(tmp2)
                DFS(layer + 1)
                inList.insert(0, tmp2 % 10)
                inList.insert(0, tmp2 // 10)
                rstList.pop()
            else:
                return


if __name__ == "__main__":
    n = int(input())
    inList = []
    rstList = []
    while 1:
        inList.insert(0, n % 10)
        n = n // 10
        if n == 0:
            break
    # 0이 입력되면 입력종료를 어떻게 구현?
    # 입력 받는 실시간 중 어떻게 처리?
    countNum = 0
    DFS(0)
    print(countNum)
