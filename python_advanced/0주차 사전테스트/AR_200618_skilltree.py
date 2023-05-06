'''
AR_200618_스킬트리

리뷰내용
1. low level 언어 사용 습관을 high level 언어 스타일에 맞게 변경 필요(민우님 스타일 참고할 것)
   - 내 방식: skill_trees 각 문자열에서 skill의 각각의 문자와 같은 문자가 있다면 인덱스 값을 체크리스트에 저장. 특정 문자가 없다면 MAX_ARRAY_SIZE 줌으로 무의미한 값으로 만듬. 추후 체크리스트에 저장된 인덱스 리스트를 같은 리스트의 정렬된 것과 비교하여 같다면 카운트함
   - 민우님 방식: skill_tree 각 문자열에서 skill의 각 문자가 있는 부분에 해당하는 부분만 추출함. 이를 skill의 문자열과 비교하여 counting함
2. 상수의 경우 별도로 선언하여 사용할 것

독백
내 방식과 민우님 방식을 비교하여 설명을 적어보니, 민우님 방식을 보다 간결하고 명확하게 정리할 수 있음. 
쉽고 명확한 코드를 생각해보자

'''

'''
MAX_ARRAY_SIZE = 100

def solution(skill, skill_trees):
    skillSize = len(skill)
    skillTreesSize = len(skill_trees)
    checkList = [[0] * skillSize for _ in range(skillTreesSize)]
    countNum = 0

    for i in range(skillTreesSize):
        for j in range(skillSize):
            if skill_trees[i].find(skill[j]) == -1:
                checkList[i][j] = MAX_ARRAY_SIZE
            else:
                checkList[i][j] = skill_trees[i].find(skill[j])
        if checkList[i] == sorted(checkList[i]):
            countNum += 1

    return countNum 
'''

def solution(skill, skill_trees):
    answer_count = 0
    
    for skill_tree in skill_trees:
        new_skill_tree = ''.join([each_character for each_character in skill_tree if each_character in skill])
        
        if skill.find(new_skill_tree) == 0:
            answer_count += 1
            
    return answer_count
    
    
    
    
    
    
    
    
    
    
    
    
    
    
