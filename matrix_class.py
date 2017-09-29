import random

class Matrix:
    def __init__(self, m, n):
        self._rows = m
        self._columns = n
        self._a = []
        for i in range(m):
            for j in range(n):
                self._a.append(random.randint(1, 10))

    def dim(self):
        return self._rows, self._columns

    def print_matrix(self):
        print(self._a)

    def __getitem__(self, j):
        return self._a[j]

    def __setitem__(self, k, val):
        self._a[k] = val
    
    def __add__(self, m):
        if self.dim() != m.dim():
            raise TypeError('Dimension mismatch!')
        s = Matrix(*self.dim())
        k = 0
        for i in range(self._rows):
            for j in range(self._columns):
                s[j + k] = self[j + k] + m[j + k]
            k += self._columns
        return s

    def __mul__(self, m):
        if self._columns != m._rows:
            raise TypeError('Can''t be multiplied!')
        


m1 = Matrix(2, 3)
m2 = Matrix(2, 3)
m1.print_matrix()
m2.print_matrix()
(m1 + m2).print_matrix()

