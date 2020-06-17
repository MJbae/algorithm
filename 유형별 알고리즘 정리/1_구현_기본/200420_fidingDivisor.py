import sys
#sys.stdin=open("input", "rt")

N, K = map(int, input().split())

a_list = []

for i in range(1, N+1):
    if N % i == 0:
        a_list.append(i)
    if len(a_list) == K:
        print(a_list[K - 1])
        break

if len(a_list) < K:
    print(-1)

