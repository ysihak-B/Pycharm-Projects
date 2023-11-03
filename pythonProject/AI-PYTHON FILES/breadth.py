import graph

graph = graph.Graph("graph data")
neighbors = graph.con
isvisited = []
isexplored = []
visited = []
parents = {}
for each in graph.vertex_list:
    index = graph.return_index(each)
    isvisited.append(False)

for each in graph.vertex_list:
    index = graph.return_index(each)
    isexplored.append(False)


def parent_child(vertex, child):
    key = vertex
    if key in parents:
        parents[key].append(child)
    else:
        parents[key] = []
        parents[key].append(child)


def breadth_search(vertex):
    v_pos = graph.return_index(vertex)
    if not isvisited[v_pos]:
        isvisited[v_pos] = True
        visited.append(vertex)
    if not isexplored[v_pos]:
        for neighbor in neighbors.get(vertex):
            n_pos = graph.return_index(neighbor)
            if not isvisited[n_pos]:
                visited.append(neighbor)
                isvisited[n_pos] = True
                parent_child(vertex, neighbor)
    isexplored[v_pos] = True
    for i in range(len(isvisited)):
        if isvisited[i] and not isexplored[i]:
            vertex = graph.vertex_list[i]
            breadth_search(vertex)


breadth_search("Sibiu")
print(visited)