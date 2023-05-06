import sys
#sys.stdin = open("input", "rt")

N = int(input())
nList = [list(map(int, input().split())) for _ in range(N)]
rst = 0


for i in range(N):
    nList[i].append(0)
    nList[i].insert(0, 0)

nList.append([0]*(N+2))
nList.insert(0, [0]*(N+2))

for i in range(1, N+1):
    for j in range(1, N+1):
        maxN = nList[i][j]
        if maxN > max(nList[i-1][j], nList[i][j-1], nList[i][j+1], nList[i+1][j]):
            rst += 1

print(rst)