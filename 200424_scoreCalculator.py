import sys
#sys.stdin = open("input", "r")

N = int(input())
in_lst = list(map(int, input().split()))
rst_n = 0
cnt_n = 0

for i in in_lst:
    if i == 1:
        cnt_n += 1
        rst_n += cnt_n
    else:
        cnt_n = 0

print(rst_n)
