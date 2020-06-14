import sys
#sys.stdin = open("input", "r")

minCount = 2147000000


def included(start, targetString):
    #print(start, "_", targetString, "_")
    for k in range(len(start)):
        tmpStart = start
        tmpStart = tmpStart.replace(tmpStart[k], "", 1)
        for m in range(len(targetString)):
            tmpTargetString = targetString
            tmpTargetString = tmpTargetString.replace(tmpTargetString[m], "", 1)
            if tmpStart == tmpTargetString:
                return True
    else:
        return False


def DFS(layer, begin, words, checkList, target):
    global minCount
    if begin == target:
        if minCount > layer:
            minCount = layer
    if layer == len(words):
        return
    else:
        for i in range(len(words)):
            if checkList[i] == 0:
                checkList[i] = 1
                if included(begin, words[i]):
                    DFS(layer + 1, words[i], words, checkList, target)
                checkList[i] = 0


def solution(begin, target, words):
    global minCount
    global targetString
    if target not in words:
        return 0
    checkList = [0] * (len(words))
    DFS(0, begin, words, checkList, target)
    return minCount

if __name__ == "__main__":
    words = ["hhhhh", "hhhht"]
    begin = "hhhit"
    target = "hhhhh"
    print(solution(begin, target, words))
