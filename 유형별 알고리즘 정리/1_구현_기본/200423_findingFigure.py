import sys
#sys.stdin = open("input", "r")

N, M = map(int, input().split())
cnt_lst = [0] * (N + M + 1)

for i in range(1, N+1):
    for j in range(1, M+1):
        cnt_lst[i+j] += 1

max_n = max(cnt_lst)
for i, v in enumerate(cnt_lst):
    if max_n == v:
        print(i, end=' ')


