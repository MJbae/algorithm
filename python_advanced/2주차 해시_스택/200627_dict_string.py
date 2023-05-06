def solution(s):
    stack = []
    for alp in s:
        while stack and alp > stack[-1]:
            stack.pop()
        stack.append(alp)

    return ''.join(map(str, stack))


'''
def solution(s):
    stack = []
    s_sorted = sorted([[index*-1, char] for index, char in enumerate(s)], key=lambda x:x[1])
    last_char, last_index = s_sorted.pop()
    print(s_sorted)

def solution(s):
    stack = []
    answer = ''

    while s:
        max_char = max(s)
        max_index = s.index(max_char)
        s = s[max_index + 1 : ]
        answer += max_char

    # answer = ''.join(stack)
    return answer
'''