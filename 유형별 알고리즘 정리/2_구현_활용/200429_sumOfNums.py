import sys
#sys.stdin = open("input", "rt")

N, M = map(int, input().split())
aList = list(map(int, input().split()))
rst = 0

for i in range(N):
    for j in range(i+1, N):
        if sum(aList[i:j]) == M:
            rst += 1
            break

print(rst)
