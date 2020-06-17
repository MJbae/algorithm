import sys
#sys.stdin = open("input", "r")


def DFS(L, s):
    global cnt
    if L == K:
        if sum(rst) % M == 0:
            cnt += 1
    else:
        for i in range(s, N):
            rst[L] = inList[i]
            DFS(L+1, i+1)


if __name__ == "__main__":
    N, K = map(int, input().split())
    inList = list(map(int, input().split()))
    M = int(input())
    rst = [0] * N
    cnt = 0
    DFS(0, 0)
    print(cnt)
