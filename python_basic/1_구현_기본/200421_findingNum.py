import sys
#sys.stdin = open("input", "r")

N = int(input())
in_lst = list(map(int, input().split()))
in_lst.insert(0, 0)
res = 0

avg_n = sum(in_lst[1:])/N
if avg_n - round(avg_n) == 0.5:
    avg_n = round(avg_n) + 1
else:
    avg_n = round(avg_n)

prd_lst = []
ch_lst = [0] * (N+1)
for i in range(1, N+1):
    if avg_n - in_lst[i] < 0:
        ch_lst[i] = 1
    prd_lst.append(abs(avg_n - in_lst[i]))
prd_lst.insert(0, 100)

min_n = 2147000000
for i, v in enumerate(prd_lst):
    if v < min_n:
        min_n = v
        res = i
    elif v == min_n:
        if ch_lst[i] == 1 and ch_lst[res] == 0:
            res = i

print(avg_n, res)
