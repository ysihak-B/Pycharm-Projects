class Graph:
    def __init__(self, size):
        self.adj_list = []
        self.vertices = []
        for i in range(size):
            self.adj_list.append([0 for i in range(size)])
        self.size = size

    def add_node(self, v):
        if v in self.vertices:
            print("vertex %c already exists", v)
            return
        self.vertices.append(v)

    def add_edge(self, v1, v2):
        if not v1 in self.vertices:
            self.add_node(v1)
        if not v2 in self.vertices:
            self.add_node(v2)
        pos = self.vertices.index(v1)
        pos2 = self.vertices.index(v2)
        self.adj_list[pos][pos2] = v2


g = Graph(5)
print(g.adj_list)
g.add_edge('a', 'b')
g.add_edge('a', 'c')
g.add_edge('b', 'e')
g.add_edge('c', 'd')
g.add_edge('e', 'b')
g.add_edge('d', 'b')
g.add_edge('c', 'b')
print(g.adj_list)
