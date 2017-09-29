import math

class PriorityQueue:
  def parent(self, i):
    return (i - 1) // 2
  def left(self, i):
    return (2 * i + 1)
  def right(self, i):
    return (2 * i + 2)
  def max_heapify(self, i):
    l = self.left(i)
    r = self.right(i)
    largest = i
    if l < self.curr_size and self.a[i] < self.a[l]:
      largest = l
    if r < self.curr_size and self.a[largest] < self.a[r]:
      largest = r
    if largest != i:
      self.a[i], self.a[largest] = self.a[largest], self.a[i]
      self.max_heapify(largest)
  def buildmax_heap(self):
    for i in range(self.curr_size // 2, -1, -1):
      self.max_heapify(i)
  def __init__(self, a):
    self.a = a
    self.curr_size = len(self.a)
    self.buildmax_heap()
  def maximum(self):
    return self.a[0]
  def remove_maximum(self):
    self.max_heapify(1)
    self.curr_size = self.curr_size - 1
  def insert(self, k):
    self.a.append(-float("inf"))
    self.curr_size += 1
    self.increase_key(self.curr_size-1, k)
    
  def increase_key(self, i, x):
    self.a[i] = x
    while self.a[self.parent(i)] < x:
      self.a[i], self.a[self.parent(i)] = self.a[self.parent(i)], self.a[i]
      i = (i - 1) // 2
  def printq(self):
    print(self.a)
 
    
m1 = PriorityQueue([1, 5, -9, 65, 35])
m2 = PriorityQueue([0, 54, -57, 3, 10])
m1.printq()
m2.printq()

print(m1.maximum())


