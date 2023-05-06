'''
AR_200619_최대 용량이 정해진 FIFO 큐 클래스

리뷰 내용
1. early return문 사용 시 else문 사용 자제(indentation depth를 짧게하여 코드 가독성 향상) 
2. exception raise 부분 구현할 것
3. snake_case 활용
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
        try:
            if self.qsize() <= 0:
                return False
                raise Exception('Empty')
            
            if self.stack2.size() == 0:
                for _ in range(self.stack1.size()):
                    self.stack2.push(self.stack1.pop())
                    
            return self.stack2.pop()
        except Exception as e:
            print('Exception raise!', e)


n, max_size = map(int, input().strip().split(' '))
test_que = MyQueue(max_size)

for _ in range(n):
    comand = None
    input_num = None
    input_string = input()

    if ' ' in input_string:
        command, input_num = input_string.strip().split(' ')
    else:
        command = input_string

    if command == 'PUSH':
        push_num = int(input_num)
        print(test_que.push(push_num))
    elif command == 'POP':
        print(test_que.pop())
    elif command == 'SIZE':
        print(test_que.qsize())
