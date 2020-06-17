import sys
#sys.stdin = open("input", "rt")

T = int(input())

for t in range(T):
    inputString = (input())
    inString = list(inputString.lower())

    if len(inString) % 2 == 1:
        del inString[len(inString)//2]
        cnt = 0
        for i in range(0, len(inString)//2):
            if inString[i] == inString[-1-i]:
                cnt += 1
        if cnt == len(inString)//2:
            print("#%d YES" % (t+1))
        else:
            print("#%d NO" % (t+1))
    else:
        cnt = 0
        for i in range(0, len(inString)//2):
            if inString[i] == inString[-1 - i]:
                cnt += 1
        if cnt == len(inString) // 2:
            print("#%d YES" % (t+1))
        else:
            print("#%d NO" % (t+1))
