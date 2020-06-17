import sys
#sys.stdin=open("input", "rt")

#입력, n개수, n리스트 / m개수, m리스트
nNum = int(input())
nList = list(map(int, input().split()))
mNum = int(input())
mList = list(map(int, input().split()))
ansList = list()
p1 = p2 = 0

#각 리스트의 첫번재 요소 비교하여 ansList에 작은 수를 ansList에 삽입
#ansList에 삽입된 요소는 pop

while p1 != len(nList) and p2 != len(mList):
    if nList[p1] < mList[p2]:
        ansList.append(nList[p1])
        p1 += 1
    else:
        ansList.append(mList[p2])
        p2 += 1

if p1 != len(nList):
    for j in nList[p1:]:
        ansList.append(j)
if p2 != len(mList):
    for j in mList[p2:]:
        ansList.append(j)

#출력 ansList 모든 요소
for i in ansList:
    print(i, end=" ")
