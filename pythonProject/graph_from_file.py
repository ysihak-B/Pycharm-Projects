import graph


def graph_from_file(filename):
    build_graph = graph.Graph(filename)

    print("\n", build_graph.vertex_list)
    print("\n", build_graph.edge_list)
    print("\n", build_graph.con, "\n")

    for edges in build_graph.edge_list:
        print(edges[0], edges[1], edges[2])


graph_from_file("AI-PYTHON FILES/graph data")