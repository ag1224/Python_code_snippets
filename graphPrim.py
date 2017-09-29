import math
import operator

class PriorityQueue:
  def parent(self, i):
    return (i - 1) // 2
  def left(self, i):
    return (2 * i + 1)
  def right(self, i):
    return (2 * i + 2)
  def min_heapify(self, i):
    l = self.left(i)
    r = self.right(i)
    smallest = i
    if l < self.curr_size and self.a[i] > self.a[l]:
      smallest = l
    if r < self.curr_size and self.a[smallest] > self.a[r]:
      smallest = r
    if smallest != i:
      self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
      self.max_heapify(smallest)
  def buildmin_heap(self):
    for i in range(self.curr_size // 2, -1, -1):
      self.min_heapify(i)
  def __init__(self, a):
    self.a = a
    self.curr_size = len(self.a)
    self.buildmin_heap()
    
  def minimum(self):
    return self.a[0]
  def remove_minimum(self):
    self.min_heapify(1)
    self.curr_size = self.curr_size - 1
  def insert(self, k):
    self.a.append(-float("inf"))
    self.curr_size += 1
    self.decrease_key(self.curr_size-1, k)
    
  def decrease_key(self, i, x):
    self.a[i] = x
    while self.a[self.parent(i)] > x:
      self.a[i], self.a[self.parent(i)] = self.a[self.parent(i)], self.a[i]
      i = (i - 1) // 2
  def printq(self):
    print(self.a)

    
class Vertex:
    def __init__(self, v):
        self.name = v
        self.key = float('inf')
        self.p = None

class Edge:
    def __init__(self, u, v, w):
        self.start = u
        self.end = v
        self.weight = w
        
class Graph:
    def __init__(self, directed = False):
        self.outgoing = {}
        self.incoming = {} if directed else self.outgoing
        self.E = []
        self.V = []
        self.keys = []
        
    def is_directed(self):
        return self.incoming is not self.outgoing

    def vertex_count(self):
        return len(self.outgoing)

    def vertices(self):
        return self.outgoing.keys()
    
    def edge_count(self):
        total = sum(len(self.outgoing[v]) for v in self.outgoing)
        return total if self.is_directed() else total // 2
    
    def degree(self, v, outgoing=True):
        adj = self.outgoing if outgoing else self.incoming
        return len(adj[v])

    def insert_vertex(self, v):
        self.outgoing[v] = []
        self.V.append(v)
        self.keys.append(v.key)
        if self.is_directed():
            self.incoming[v] = []

    def insert_edge(self, e):
        self.outgoing[e.start].append(e.end)
        self.incoming[e.end].append(e.start)
        self.E.append(e)

    def key_locator(self, k):
        for v in self.V:
            if v.key == k:
                self.V.remove(v)
                return v
        
    def MST_Prim(self, s):
        s.key = 0
        count = 0
        heap = sorted(self.V, key = operator.attrgetter('weight'))
        tree = []
        while heap:
            u = self.key_locator(heap.minimum())
            count += 1
            if count > 1:
                tree.append((z.name, u.name))
            heap.remove_minimum()
            for v in self.outgoing[u]:
                if v.key in heap:
                    for e in self.E:
                        if e.start == u and e.end == v:
                            wt = e.weight
                            break
                    v.p = u
                    if wt < v.key:
                        for i in len(heap):
                            if heap[i] == v.key:
                                break
                        v.key = wt
                        heap.decrease_key(i, wt)
            z = u
        print(tree)
            
g = Graph()
a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
e = Vertex('E')

e1 = Edge(a, b, 10)
e2 = Edge(a, c, 20)
e3 = Edge(b, c, 30)
e4 = Edge(b, d, 5)
e5 = Edge(c, d, 15)
e6 = Edge(c, e, 6)
e7 = Edge(d, e, 8)
 
g.insert_vertex(a)
g.insert_vertex(b)
g.insert_vertex(c)
g.insert_vertex(d)
g.insert_vertex(e)

g.insert_edge(e1)
g.insert_edge(e2)
g.insert_edge(e3)
g.insert_edge(e4)
g.insert_edge(e5)
g.insert_edge(e6)
g.insert_edge(e7)

#print(g.is_directed())
#g.BFS(c)
#V = [c, a, b, d]
#g.DFS(V)
g.MST_Prim(a)

