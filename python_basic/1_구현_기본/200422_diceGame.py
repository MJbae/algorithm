import sys
#sys.stdin = open("input", "r")

N = int(input())
rst_n = 0
max_n = -2147000000

for i in range(N):
    in_lst = list(map(int, input().split()))

    in_lst.sort(reverse=True)

    if in_lst[0] == in_lst[1] == in_lst[2]:
        rst_n = in_lst[0]*1000 + 10000
    elif in_lst[0] == in_lst[1] or in_lst[1] == in_lst[2]:
        rst_n = in_lst[1]*100 + 1000
    else:
        rst_n = in_lst[0]*100

    if rst_n > max_n:
        max_n = rst_n

print(max_n)

