# opposites의 경우 상수표현
# return 부분 한 문장으로 줄이기

def solution(s):
    stack = []
    OPPOSITES = {'(': ')', ')': '(', '{': '}', '}': '{', '[': ']', ']': '['}
    # 상수처럼 사용될 변수는 대문자로 표기함
    # opposites = { '(' : ')', ')' : '(', '{' : '}', '}' : '{', '[' : ']', ']' : '[' }

    # 첫번째 문자가 닫는 괄호일 경우 return false
    if s[0] == ']' or s[0] == ')' or s[0] == '}':
        return False

    # stack의 마지막 괄호와 상반된 괄호가 나온다면 pop하고 아니라면 append
    for char in s:
        if stack and stack[-1] == OPPOSITES[char]:
            stack.pop()
        else:
            stack.append(char)

    # stack에 요소가 남아 있다면 false 비었다면 true
    return not bool(stack)
    '''
    위와 같이 간소화 가능
    if stack:
        return False
    return True
    '''