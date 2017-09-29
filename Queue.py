import random

class Empty(Exception):
    pass

class ArrayQueue:
    MAX_CAPACITY = 10
    def __init__(self):
        self.size = 0
        self.data = [None] * ArrayQueue.MAX_CAPACITY
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty!')
        return self.data[self.front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is Empty!')
        answer = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        if 0 < self.size < len(self.data) // 4:
            self.resize(len(self.data) // 2)
        return answer

    def enqueue(self, x):
        if self.size == len(self.data):
            self.resize(2 * self.data)
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = x
        self.size += 1

    def resize(self, cap):
        old = self.data
        self.data = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self.front = 0


Q = ArrayQueue()
Q.enqueue(5)
Q.enqueue(3)
print(len(Q))
print(Q.dequeue())
print(Q.is_empty())
print(Q.dequeue())
print(Q.is_empty())
#print(Q.dequeue())
Q.enqueue(7)
Q.enqueue(9)
print(Q.first())
print(len(Q))
print(Q.dequeue())
print(Q.dequeue())
print(len(Q))
Q.enqueue(1)
Q.enqueue(random.randint(1, 10))
Q.enqueue(random.randint(1, 10))
Q.enqueue(random.randint(1, 10))
Q.enqueue(random.randint(1, 10))
Q.enqueue(random.randint(1, 10))
Q.enqueue(random.randint(1, 10))
Q.enqueue(random.randint(1, 10))
Q.enqueue(random.randint(1, 10))
Q.enqueue(random.randint(1, 10))
Q.enqueue(0)
print(Q.dequeue())
