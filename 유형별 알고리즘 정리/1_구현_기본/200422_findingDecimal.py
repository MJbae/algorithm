import sys
#sys.stdin = open("input", "r")

N = int(input())

ch_lst = [0] * (N+1)
cnt_n = 0

for i in range(2, N+1):
    if ch_lst[i] == 0:
        cnt_n += 1
    for j in range(i, N+1, i):
        ch_lst[j] = 1

print(cnt_n)