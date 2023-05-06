import sys
#sys.stdin = open("input", "r")

def DFS(x, subSum):
    if totalSum - subSum == subSum:
        print("YES")
        sys.exit(0)
    if subSum > totalSum-subSum:
        return
    if x == n:
        return
    else:
        DFS(x+1, subSum + inputList[x])
        DFS(x+1, subSum)


if __name__ == "__main__":
    n = int(input())
    inputList = list(map(int, input().split()))
    totalSum = sum(inputList)
    DFS(0, 0)
    print("NO")
