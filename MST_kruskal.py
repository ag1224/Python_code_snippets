import random
import operator

class Graph:
    class vertex:
        def __init__(self, i):
            self.rank = None
            self.p = None
            self.number = i+1

    class Edge:
        def __init__(self, u, v):
            self.weight = random.randint(1, 20)
            self.start = u
            self.end = v
            v.p = u

    def __init__(self, n):
        self.V = []
        for i in range(n):
            self.V.append(self.vertex(i))
        self.E = []
        for i in range(n):
            for j in range(i+1, n):
                self.E.append(self.Edge(self.V[i], self.V[j]))
        for i in self.E:
            print(i.weight)
            
    def MAKESET(self, i):
        i.p = i                       #Characteristic of leader
        i.rank = 0

    def UNION(self, x, y):
        self.LINK(self.FINDSET(x), self.FINDSET(y))

    def LINK(self, x, y):
        if x.rank > y.rank:              #Union by Size
            y.p = x
            x.rank = x.rank + y.rank
        else:
            x.p = y
            y.rank = y.rank + x.rank

    def FINDSET(self, x):
        if x != x.p:
            x.p = self.FINDSET(x.p)
        return x.p

    def MST(self):
        final = []
        for v in self.V:
            self.MAKESET(v)
        self.E = sorted(self.E, key = operator.attrgetter('weight'))
        print('Sorted weights:')
        for i in self.E:
            print(i.weight)
        for i in self.E:
            if self.FINDSET(i.start) != self.FINDSET(i.end):
                final.append(i)
                self.UNION(i.start, i.end)
        print('Length of MST:', len(final))
        for i in final:
            print(i.weight, end = ' ')
        print()
        for i in final:
            print('(',i.start.number,',',i.end.number,')', end = ' ')


a = Graph(4)
a.MST()




            
