import sys
#sys.stdin = open("input", "r")


def DFS(layer, subSum):
    if layer == k:
        if subSum >= 1:
            resultSet.add(subSum)
    else:
        DFS(layer+1, subSum + inputList[layer])
        DFS(layer+1, subSum - inputList[layer])
        DFS(layer+1, subSum)


if __name__ == "__main__":
    k = int(input())
    inputList = list(map(int, input().split()))
    totalSum = sum(inputList)
    resultSet = set()
    DFS(0, 0)
    result = totalSum - len(resultSet)
    print(result)


