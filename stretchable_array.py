import ctypes                               # provides low-level arrays
import random

class DynamicArray:
    def __init__(self):
        self._n = 0                         # count actual elements
        self._capacity = 1                  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError()
        return self._A[k]                   # retrieve from array

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return(c * ctypes.py_object)()
    
a = DynamicArray()
n = int(input('Enter the number of elements to store: '))
for i in range(n):
    a.append(random.randint(1, 10))
for j in range(n):
    print(a[j], end = ' ')
print()
print(a[len(a)])
print(a[n//2])
print(len(a))

