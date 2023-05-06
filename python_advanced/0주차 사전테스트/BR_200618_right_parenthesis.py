def solution(s):
    checkStack = []
    inputListSize = len(s)
    
    #입력 문자열 s의 첫 문자가 )이면 바로 false
    if s[0] != '(':
        return False
    
    #
    for i in range(inputListSize):
        if s[i] == '(':
            checkStack.append(s[i])
        else:
            if len(checkStack) > 0:
                checkStack.pop()
            else:
                return False
    
    if len(checkStack) > 0:
        return False
    else:
        return True