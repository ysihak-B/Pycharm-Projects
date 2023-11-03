class Node:
    def __init__(self, name, edge_list):
        self.name= name
        self.edge_list = edge_list

class Edge :
    def __init__(self, node_a,node_b, weight):
        self.node_a = node_a
        self.node_b = node_b
        self.weight = weight

class Graph:
    def __init__(self, ver, edge):
        self.ver = ver
        self.edge = edge