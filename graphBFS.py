class Vertex:
    def __init__(self, v):
        self.element = v
        self.color = 'WHITE'
        self.d = -1
        self.f = -1
        self.p = None
        
class Graph:
    def __init__(self, directed = False):
        self.outgoing = {}
        self.incoming = {} if directed else self.outgoing
        self.time = 0
        self.T = []
        
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
        if self.is_directed():
            self.incoming[v] = []

    def insert_edge(self, u, v):
        self.outgoing[u].append(v)
        self.incoming[v].append(u)

    def BFS(self, s):
        s.d = 0
        q = []
        q.append(s)
        while q:
            u = q.pop(0)
            print(u.element)
            for v in self.outgoing[u]:
                if v.color is 'WHITE':
                    v.color = 'GRAY'
                    v.d = u.d + 1
                    v.p = u
                    q.append(v)
            u.color = 'BLACK'

    def DFS(self, V):
        for v in V:
            if v.color == 'WHITE':
                print(v.element)
                self.DFS_VISIT(v)

    def DFS_VISIT(self, u):
        self.time = self.time + 1
        u.d = self.time
        u.color = 'GRAY'
        for v in self.outgoing[u]:
            if v.color == 'WHITE':
                print(v.element)
                v.p = u
                self.DFS_VISIT(v)
        u.color = 'BLACK'
        self.time = self.time + 1
        u.f = self.time
        self.T.append(u.element)

    def T_sort(self, V):
        self.DFS(V)
        print(self.T.reverse())
        
g = Graph(True)
a = Vertex(0)
b = Vertex(1)
c = Vertex(2)
d = Vertex(3)
 
g.insert_vertex(a)
g.insert_vertex(b)
g.insert_vertex(c)
g.insert_vertex(d)
g.insert_edge(a, b)
g.insert_edge(a, c)
g.insert_edge(b, c)
g.insert_edge(c, a)
g.insert_edge(c, d)
g.insert_edge(d, d)
print(g.is_directed())
#g.BFS(c)
V = [c, a, b, d]
g.T_sort(V)

