import graph

graph = graph.Graph("graph data")
neighbors = graph.con
vertex_list = graph.vertex_list
visited = []
shortest_distance = {}
unvisited = []
parent = {}
path = []


def get_path(vertex, final):
    key = final
    path.append(key)
    while key != vertex:
        key = parent[key]
        path.append(key)

    path.reverse()


def remove_shortest_vertex():
    pos = 0
    vertex = unvisited[0]
    short = shortest_distance[vertex]
    for key in unvisited:
        if shortest_distance[key] < short:
            vertex = key
            short = shortest_distance[vertex]
            pos = unvisited.index(vertex)
    unvisited.pop(pos)
    return vertex


def get_weight(node1, node2):
    for edge in graph.edge_list:
        if edge[0] == node1 and edge[1] == node2:
            return edge[2]
        elif edge[0] == node1 and edge[1] == node2:
            return edge[2]


def initialize(vertex):
    for node in vertex_list:
        if node == vertex:
            shortest_distance[vertex] = 0
        else:
            shortest_distance[node] = float('inf')


def dijkstra(vertex, final):
    initialize(vertex)
    unvisited.append(vertex)
    while vertex != final:
        for neighbor in neighbors.get(vertex):
            if neighbor not in visited:
                unvisited.append(neighbor)
                weight = get_weight(neighbor, vertex)
                short_distance = shortest_distance[vertex] + weight
                if short_distance < shortest_distance[neighbor]:
                    shortest_distance[neighbor] = short_distance
                    parent[neighbor] = vertex
        if vertex not in visited:
            visited.append(vertex)
        vertex = remove_shortest_vertex()
    visited.append(vertex)


dijkstra("Oradea", "Rimnicu_Vilcea")
get_path("Oradea", "Rimnicu_Vilcea")
print(visited)
print(parent)
print(path)

