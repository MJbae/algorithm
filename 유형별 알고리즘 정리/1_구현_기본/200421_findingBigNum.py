import sys

#sys.stdin = open("input", "r")

N, K = map(int, input().split())
in_lst = list(map(int, input().split()))

lst_s = list()
st_s = set()

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            st_s.add(in_lst[i]+in_lst[j]+in_lst[k])

lst_s = list(st_s)
lst_s.sort(reverse=True)
print(lst_s[K-1])

