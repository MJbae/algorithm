def solution(skill, skill_trees):
    skillSize = len(skill)
    skillTreesSize = len(skill_trees)
    checkList = [[0] * skillSize for _ in range(skillTreesSize)]
    countNum = 0
    
    for i in range(skillTreesSize):
        for j in range(skillSize):
            if skill_trees[i].find(skill[j]) == -1:
                checkList[i][j] = 100
            else:
                checkList[i][j] = skill_trees[i].find(skill[j])
        if checkList[i] == sorted(checkList[i]):
            countNum += 1

    return countNum