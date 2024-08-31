# 서로소
class DisjointSet:
    def __init__(self, vertex):
        self.p = [0] * (len(vertex) + 1)
        self.rank = [0] * (len(vertex) + 1)
    
    #인덱스가 vertex 숫자, 값이 parent vertex가 된다.
    def make_set(self, x):
        self.p[x] = x
    
    #최적화
    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)
        
        if px != py:
            if self.rank[px] > self.rank[py]:
                p[py] = px
            elif self.rank[px] < self.rank[py]:
                p[px] = py
            else:
                p[py] = px
                self.rank[px] += 1

def mst_kruska(vertices, edges):
    mst = []
    n = len(vertices)
    ds = DisjointSet(vertices)
    
    for i in range(n+1):
        ds.make_set(i)
        
    edges.sort(key = lambda x: x[2])
    
    for edge in edges:
        start, end, w = edge
        if ds.find_set(start) != ds.find_set(end):
            ds.union(start, end)
            mst.append(edge)
    return mst