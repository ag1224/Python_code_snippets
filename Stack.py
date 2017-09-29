class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def Is_empty(self):
        return len(self._data) == 0

    def push(self, x):
        self._data.append(x)

    def top(self):
        try:
            return self._data[-1]
        except Empty:
            print('Stack is empty!')

    def pop(self):
        try:
            return self._data.pop()
        except Empty:
            print('Stack is empty!')

S = ArrayStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.Is_empty())
print(S.pop())
print(S.Is_empty())
print(S.pop())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)
print(S.pop())
print(S.pop())
print(S.pop())
print(S.top())

