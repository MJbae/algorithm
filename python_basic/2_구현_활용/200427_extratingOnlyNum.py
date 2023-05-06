import sys
#sys.stdin = open("input", "rt")

N = str(input())
rst = 0

for i in N:
    if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' \
            or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
        rst = rst*10 + int(i)

cnt = 1
for j in range(1, rst//2+1):
    if rst % j == 0:
        cnt += 1

print(rst)
print(cnt)