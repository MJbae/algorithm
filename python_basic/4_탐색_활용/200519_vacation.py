import sys
sys.stdin = open("input", "r")


def DFS(lyr, sum_m):
    global max_m
    if lyr > N+1:
        return
    if lyr == N+1:
        if sum_m > max_m:
            max_m = sum_m
    else:
        DFS(lyr + pt[l], sum_m + pm[l])
        DFS(lyr + 1, sum_m)


if __name__ == "__main__":
    N = int(input())
    pt = [0]
    pm = [0]
    max_m = -2147000000
    for i in range(1, N+1):
        a, b = map(int, input().split())
        pt.append(a)
        pm.append(b)
    DFS(1, 0)
    print(max_m)

