from _collections import deque

'''
출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
'''
# sys.stdin = open("input", "r")

def included(start, targetString):
    countNum = 0

    if len(start) != len(targetString):
        return False

    for a, b in zip(start, targetString):
        if a != b:
            countNum += 1

    if countNum == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    global targetString
    layer = 0
    checkList = [0] * (len(words))
    dQ = deque()
    dist = {begin: 0}
    dQ.append(begin)
    count = 0
    if target not in words:
        return 0

    while dQ:
        tmp = dQ.popleft()

        for i in range(len(words)):
            count += 1
            if checkList[i] == 0 and included(tmp, words[i]):
                checkList[i] = 1
                dQ.append(words[i])
                dist[words[i]] = dist[tmp] + 1

    return dist.get(target, 0)

if __name__ == "__main__":
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    begin = "hit"
    target = "cog"
    print(solution(begin, target, words))
