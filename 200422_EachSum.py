import sys
#sys.stdin = open("input", "r")

N = int(input())
in_lst = list(map(int, input().split()))

max_n = -2147000000
max_i = -1
for i in range(N):
    sum_n = 0
    tmp = in_lst[i]
    while tmp != 0:
        sum_n += tmp % 10
        tmp = tmp // 10

    if sum_n > max_n:
        max_n = sum_n
        max_i = i

print(in_lst[max_i])

