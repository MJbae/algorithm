'''
AR_200618_올바른 괄호문제

리뷰내용
1. 불필요한 주석 제거
2. 반복문 사용 시 인덱스가 불필요하다면 값을 기준으로 순회(index error 예방)
3. 리스트 공백여부 확인 시 len 보다는 if를 권장(PEP 8)
   * PEP 8( Python Enhancement Proposals version 8): Style Guide for Python Code
4. return 값 깔끔하게 줄이기

독백
사전테스트 제출한 코드 전체적으로 'PEP 8'을 따르지 않는다는 내용의 리뷰임
'PEP 8' 개념 새로 접함. 기존 스타일에 익숙하나 개발은 협업을 전제로하므로 더 나은 소통을 위해 PEP 8 적극 수용할 것

'''

def solution(s):
    check_stack = []
    input_size = len(s)

    if s[0] != '(':
        return False

    for bracket in s:
        if bracket == '(':
            check_stack.append(bracket)
        else:
            if check_stack:
                check_stack.pop()
            else:
                return False
    
    return len(check_stack) == 0
