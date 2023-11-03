import graph

graph = graph.Graph("AI-PYTHON FILES/observations")
neighbors = graph.con


def degree(vertex):
    num_connected_nodes = len(neighbors.get(vertex))
    num_of_vertices = len(graph.vertex_list)
    degree_centrality = num_connected_nodes / (num_of_vertices - 1)
    return degree_centrality


print(degree("Oradea"))
