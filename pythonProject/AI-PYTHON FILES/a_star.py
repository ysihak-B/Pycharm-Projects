from cmath import sin, cos
from math import atan2
import numpy as np
from numpy import radians
import graph
# radius of the earth
R = 6371

graph = graph.Graph("graph data")
neighbors = graph.con
vertex_list = graph.vertex_list
visited = []
location = {}
shortest_distance = {}
shortest_f = {}
unvisited = []
parent = {}
path = []


def lat_lon(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.split(" ")
        key = line[0]
        lat = line[1]
        lon = line[2]
        location[key] = (float(lat), float(lon))


def heuristic(location1, location2):
    lat1 = radians(location1[0])
    lat2 = radians(location2[0])
    lon1 = radians(location1[1])
    lon2 = radians(location2[1])
    lat_dif = lat2 - lat1
    lon_dif = lon2 - lon1
    a = sin(lat_dif / 2) ** 2 + cos(lat1) * cos(lat2) * sin(lon_dif / 2) ** 2
    c = 2 * atan2(np.sqrt(a), np.sqrt(1 - a))
    heuristic_distance = R * c
    return heuristic_distance


def remove_shortest_vertex():
    pos = 0
    vertex = unvisited[0]
    short = shortest_f[vertex]
    for key in unvisited:
        if shortest_f[key] < short:
            vertex = key
            short = shortest_f[vertex]
            pos = unvisited.index(vertex)
    unvisited.pop(pos)
    return vertex


def get_path(vertex, final):
    key = final
    path.append(key)
    while key != vertex:
        key = parent[key]
        path.append(key)

    path.reverse()


def get_weight(node1, node2):
    for edge in graph.edge_list:
        if edge[0] == node1 and edge[1] == node2:
            return edge[2]
        elif edge[0] == node1 and edge[1] == node2:
            return edge[2]


def initialize(vertex, h):
    for node in vertex_list:
        if node == vertex:
            shortest_distance[vertex] = 0
            shortest_f[vertex] = 0 + h
        else:
            shortest_f[node] = float('inf')
            shortest_distance[node] = float('inf')


def a_star(vertex, final):
    lat_lon("location")
    location1 = location[vertex]
    location2 = location[final]
    h = heuristic(location1, location2)
    initialize(vertex, h)
    while vertex != final:
        for neighbor in neighbors.get(vertex):
            if neighbor not in visited and neighbor not in unvisited:
                unvisited.append(neighbor)
                g = get_weight(vertex, neighbor) + shortest_distance[vertex]
                location1 = location[neighbor]
                h = heuristic(location1, location2)
                f = g + h
                if f < shortest_f[neighbor]:
                    shortest_f[neighbor] = f
                    parent[neighbor] = vertex
                if g < shortest_distance[neighbor]:
                    shortest_distance[neighbor] = g

        if vertex not in visited:
            visited.append(vertex)
        vertex = remove_shortest_vertex()
    visited.append(vertex)


a_star("Oradea", "Rimnicu_Vilcea")
get_path("Oradea", "Rimnicu_Vilcea")
print(visited)
print(parent)
print(path)
