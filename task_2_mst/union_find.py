# UnionFind manages group of objects
# aka as Disjoint Set Data Structure.
class UnionFind:
    def __init__(self, vertices):
        self.count = len(vertices)
        self.size = {}
        self.parent = {}
        self.make_set(vertices)

    # Initially, each node is his own
    # representative (head or root)
    def make_set(self, nodes):
        for node in nodes:
            self.parent[node] = node
            self.size[node] = 1    

    # Returns the representative (which might be the element) 
    # of the group or the element itself
    def find(self, element):
        pathCompression = element
        while self.parent[element] != element:
            element = self.parent[element]

        while self.parent[element] != element:
             tmp = self.parent[pathCompression]
             pathCompression = tmp

        return element

    # Groups element a and b together.
    # The smaller group is added 
    # to the larger group 
    #
    def union(self, a,b):
        root_a = self.find(a)
        root_b = self.find(b)
        # Elements already belong in the same
        # group
        if root_a == root_b:
            return
        
        # unify the smaller group. 
        # this is known as union by size, 
        # and reduces the time complexity
        if self.size[root_a] < self.size[root_b]:
             self.parent[root_a] = root_b 
             self.size[root_b] += self.size[root_a] 
        else:
             self.parent[root_b] = root_a 
             self.size[root_a] += self.size[root_b]

        
def main():
    vertices = ['A','B','C']
    uf = UnionFind(vertices=vertices)
    print(uf.parent)
    edges = [('A','B'),('A','C'),('C','B')]

    e = 0
    i = 0
    result = []
    while (e < len(vertices) - 1 and i < len(edges)):
        edge = edges[i]
        x = uf.find(edge[0])
        y = uf.find(edge[1])
        # Components are not connected
        if x != y:
            uf.union(edge[0],edge[1])
            print(uf.parent)
        
            result.append(edge)
            e = e + 1
        
        i += 1
    print(result)


if __name__ == '__main__':
    main()