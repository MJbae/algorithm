import sys
#sys.stdin=open("input", "rt")

# 10번 반복문 내 입력 받기, 각 구간 10개에 대해
cardList = list(range(21))

for i in range(10):
    n, m = map(int, input().split())
    # 각 카드 치환, 각 구간에 따라 반복 횟수 유의
    for j in range((m-n+1)//2):
        cardList[n+j], cardList[m-j] = cardList[m-j], cardList[n+j]

# 0번 항목 제외하고 cardList 출력
cardList.pop(0)
for i in cardList:
    print(i, end=" ")
