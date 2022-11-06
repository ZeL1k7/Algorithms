import copy
from queue import Queue
import numpy as np

graph = [[0, 0, 0, 0, 1],
         [0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [1, 0, 1, 0, 0]]
used = [False for _ in range(len(graph))]
time_in = [0 for _ in range(len(graph))]
time_out = [0 for _ in range(len(graph))]
time = 0


def dfs(vertex):
    global time
    used[vertex] = True
    time_in[vertex] = time
    time += 1
    for v in range(len(graph[vertex])):
        if graph[vertex][v] == 1 and not used[v]:
            dfs(v)
    time_out[vertex] = time
    time += 1


def bfs(vertex):

    q = Queue()
    q.put(vertex)
    used[vertex] = True
    while not q.empty():
        v = q.get()
        for neighboors in range(len(graph[v])):
            if graph[v][neighboors] == 1 and not used[neighboors]:
                used[neighboors] = True
                q.put(neighboors)


def topological_sort():
    v = 0
    dfs(v)
    return np.argsort(time_out)[::-1]


component = []


def connected_components():

    global component

    def dfs_modified(vertex):
        component.append(vertex)
        used[vertex] = True
        for v in range(len(graph[vertex])):
            if graph[vertex][v] == 1 and not used[v]:
                dfs_modified(v)

    components = []
    for v in range(len(used)):
        if not used[v]:
            component = []
            dfs_modified(v)
            components.append(component)
    return components


weighted_positive_graph = \
        [[0, 0, 3, 0, 5],
         [9, 0, 0, 0, 1],
         [0, 13, 0, 0, 1],
         [0, 0, 4, 0, 7],
         [1, 0, 11, 2, 0]]
used_weighted = [False for _ in range(len(weighted_positive_graph))]


def dijkstra(start_vertex):
    '''
    Can be used only with positive weights
    :param start_vertex:
    :return: min distances to all vertexes
    '''
    d = [float('inf') for _ in range(len(weighted_positive_graph))]
    d[start_vertex] = 0
    for i in range(len(weighted_positive_graph)):
        v = min([d[j] if not used_weighted[j] else float('inf') for j in range(len(d))])
        used_weighted[d.index(v)] = True
        for neighboors in range(len(weighted_positive_graph[d.index(v)])):
            if weighted_positive_graph[d.index(v)][neighboors] != 0:
                d[neighboors] = min(d[neighboors], v + weighted_positive_graph[d.index(v)][neighboors])

    return d
