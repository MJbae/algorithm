'''
200617_week1_최대 용량이 정해진 FIFO 큐 클래스

과제 목표
1. 최대 용량이 정해진 FIFO 큐 클래스 구현
2. 표준 입력으로 들어온 명령어로 큐 조작

핵심아이디어
push 기능의 경우 stack1에 append하여 구현하였습니다.
pop의 경우 stack2에서 pop하여 구현하였으나 stack2가 빈 경우에는 stack1의 모든 요소를 stack2로 append하였습니다.

배운점
1. 파이썬 객체 활용
2. 스택 자료형 2개로 큐 구현 알고리즘(참고 https://tdm1223.tistory.com/44)
  * 2시간 고민 후 스택 2개로 큐 구현할 수 있는 방법이 떠오르지 않아 위의 블로그를 참고함
3. 표준 입력 활용

시간복잡도 = O(N), N = 입력되는 명령의 수(n)
'''

class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)


class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return self.stack1.size() + self.stack2.size()

    def push(self, item):
        if self.stack1.size() >= self.max_size:
            return False
        else:
            self.stack1.push(item)
            return True

    def pop(self):
        if self.qsize() <= 0:
            return False
        else:
            if self.stack2.size() == 0:
                for _ in range(self.stack1.size()):
                    self.stack2.push(self.stack1.pop())

        return self.stack2.pop()


n, max_size = map(int, input().strip().split(' '))
testQue = MyQueue(max_size)

for _ in range(n):
    comand = None
    inputNum = None
    inputString = input()

    if ' ' in inputString:
        command, inputNum = inputString.strip().split(' ')
    else:
        command = inputString

    if command == 'PUSH':
        pushNum = int(inputNum)
        print(testQue.push(pushNum))
    elif command == 'POP':
        print(testQue.pop())
    elif command == 'SIZE':
        print(testQue.qsize())