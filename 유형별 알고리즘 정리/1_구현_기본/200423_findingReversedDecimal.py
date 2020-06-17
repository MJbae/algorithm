import sys
#sys.stdin = open("input", "r")

def reverse(x):
    rst = 0
    while x != 0:
        rst = (rst * 10) + (x % 10)
        x = x//10
    return rst


def isPrime(t):
    if t == 1:
        return False
    if t == 2:
        return True
    for j in range(2, t):
        if t % j == 0:
            return False
    return True


N = int(input())
in_lst = list(map(int, input().split()))

for i in range(N):
    tmp = reverse(in_lst[i])

    if isPrime(tmp):
        print(tmp, end=' ')

