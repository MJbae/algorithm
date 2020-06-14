import sys
import copy
from itertools import product

'''
핵심 아이디어
1. banned_id의 *를 지운 후 순수 char만으로 이루어진 copyOfBadUser 리스트를 만든다.
2. copyOfBadUser의 각 요소의 순수 char가 포함된 모든 user_id의 항목을 찾아서 candidate 리스트에 삽입한다.
    ex) frd의 모든 순수 char는 user_id 내 frodo, fradi에 포함되므로 candidate[0] = [frodo, fradi]
3. candidate의 조합의 모든 경우를 구한 후 중복된 부분을 제거한다.
4. 중복이 제거된 조합의 경우 중 banned_id의 길이와 같은 조합의 경우를 카운트하여 답을 구한다. 
'''


def solution(normalUser, badUser):
    candidate = [[] * len(badUser)]
    # badUser의 각 요소별로 올 수 있는 userid의 모든 경우를 담은 리스트를 만든다
    for i in range(len(badUser)):
        # BadUser 리스트를 deepcopy한다.
        # deepcopy된 리스트에는 BadUser 리스트 요소의 "*"를 제거하여 저장한다
        copyOfBadUser = copy.deepcopy(badUser)
        copyOfBadUser[i] = copyOfBadUser[i].replace("*", "")

        # badUser 리스트 각 요소에 올 수 있는 모든 경우의 수를 candidate에 담는다.
        tmplist = []
        for k in range(len(normalUser)):
            tmpCnt = 0
            for t in range(len(copyOfBadUser[i])):
                # *를 제외한 badUser 각 char가 normalUser 요소의 일부가 된다면 tmpCnt를 1씩 증가한다.
                if copyOfBadUser[i][t] in normalUser[k]:
                    tmpCnt += 1
            # *를 제외한 badUser의 각 요소의 모든 char가 nomalUser 특정 요소의 일부가 된다면 tmplist에 append한다.
            if tmpCnt == len(copyOfBadUser[i]):
                if len(badUser[i]) == len(normalUser[k]):
                    tmplist.append(normalUser[k])
        candidate.append(tmplist)
    candidate.pop(0)

    #candidate에 있는 요소를 이용해 가능한 모든 조합의 수를 구하고 compareList에 저장한다
    compareList = list(product(*candidate))
    print(compareList)
    resultList = []
    cntNum = 0
    #compareList 내 중복이 되는 부분에 대해 set을 활용하여 중복을 제거하고 체크리스트에 저장한다.
    for i in range(len(compareList)):
        tmpList = list(compareList[i])
        tmpSet = set(tmpList)
        resultList.append(list(tmpSet))

    #resultList 내 모든 요소를 탐색하여 요소 내 중복을 제거한 후, badUser의 길이와 같은 리스트를 카운트한다.
    for j in resultList:
        for k in resultList[resultList.index(j)+1:]:
            if j == k:
                resultList.remove(k)
        if len(j) == len(badUser):
            cntNum += 1

    return cntNum



if __name__ == "__main__":
    normalUser = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    badUser = ["fr*d*", "*rodo", "******", "******"]

    print(solution(normalUser, badUser))
