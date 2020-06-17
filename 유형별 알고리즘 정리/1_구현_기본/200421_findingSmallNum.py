import sys
#sys.stdin=open("input", "rt")

T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    aList = list(map(int, input().split()))

    sortedList = aList[s-1:e]
    sortedList.sort()

    print("#%d %d" %(t+1, sortedList[k-1]))