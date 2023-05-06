import sys
#sys.stdin = open("input", "r")

def DFS(x):
    if x == n+1:
        for j in range(0, n+1):
            if checkList[j] == 1:
                print(j, end=" ")
        print()
    else:
        checkList[x] = 1
        DFS(x+1)
        checkList[x] = 0
        DFS(x+1)


if __name__ == "__main__":
    n = int(input())
    checkList = [0]*(n+1)
    DFS(1)