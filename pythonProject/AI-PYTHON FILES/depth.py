import graph

graph = graph.Graph("graph data")
neighbors = graph.con
isvisited = []
visited = []

for each in graph.vertex_list:
    index = graph.return_index(each)
    isvisited.append(False)


def depth_search(vertex):
    v_pos = graph.return_index(vertex)
    if not isvisited[v_pos]:
        isvisited[v_pos] = True
        visited.append(vertex)
    for neighbor in neighbors.get(vertex):
        n_pos = graph.return_index(neighbor)
        if not isvisited[n_pos]:
            isvisited[n_pos] = True
            visited.append(neighbor)
            depth_search(neighbor)


depth_search("Drobeta")
print(visited)


