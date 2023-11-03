class Graph:
    def __init__(self, file_name):
        self.file_name = file_name
        self.vertex_list = []
        self.edge = []
        self.edge_list = []
        self.con = {}
        self.location = []
        self.s_distance = None
        file = open(self.file_name, 'r')
        lines = file.readlines()
        for line in lines:
            line = line.split(" ")
            n1 = self.add_node(line[0])
            n2 = self.add_node(line[1])
            self.add_edges(n1, n2, int(line[2]))
            self.add_edges(n2, n1, int(line[2]))

    def add_node(self, v):
        if v not in self.vertex_list:
            self.vertex_list.append(v)
        return self.vertex_list.index(v)

    def return_index(self, vertex):
        pos = self.vertex_list.index(vertex)
        return pos

    def node_con(self, node1, node2):
        key = node1
        if key in self.con:
            self.con[key].append(node2)
        else:
            self.con[key] = []
            self.con[key].append(node2)

    def add_edges(self, node1, node2, weight):
        self.edge = []
        node1 = self.vertex_list[node1]
        node2 = self.vertex_list[node2]
        self.node_con(node1, node2)
        self.edge.append(node1)
        self.edge.append(node2)
        self.edge.append(weight)
        if self.edge not in self.edge_list:
            self.edge_list.append(self.edge)