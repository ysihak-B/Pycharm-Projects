from a_star import *
from dijkstra import *

bn = {}
for each in vertex_list:
    bn[each] = 0


def helper(short_path):
    for i in range(len(short_path)):
        if i == 0 or i == len(short_path) - 1:
            continue
        else:
            vertex = vertex_list[i]
            bn[vertex] = bn[vertex] + 1
    path.clear()


def between_ness():
    for i in range(len(vertex_list)):
        for j in range(len(vertex_list)):
            if j > i:
                a_star(vertex_list[i], vertex_list[j])
                # dijkstra(vertex_list[i], vertex_list[j])
                get_path(vertex_list[i], vertex_list[j])
                print(path)
                helper(path)
                print(bn)


between_ness()
print(bn)
