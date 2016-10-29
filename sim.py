import numpy as np
import pyvisgraph as vg
from os import listdir
from matplotlib import pyplot as plt


def main():
    folder = 'obstacles'

    # load a list of the obstacle files.
    files = listdir(folder)

    # each element of the list of obstacles is a list
    # of vertices representing a figure on the plane.
    #
    #                       vi = (x, y)
    #
    #     obstacle 0        obstacle 1            obstacle n
    # [[v1, v2,..., vn], [v1, v2,..., vn],..., [v1, v2,..., vn]]
    polygons = []
    for f in files:
        # each file on the obtacle course's folder contains
        # the coordinates of an obstacle's vertices in the format:
        # x1, x2, x3,..., xn
        # y1, y2, y3,..., yn
        x, y = np.loadtxt(folder + '/' + f)
        vertices = [vg.Point(x, y) for x, y in zip(x, y)]
        polygons.append(vertices)

    # see https://github.com/TaipanRex/pyvisgraph
    # for visibility graph source code
    #
    # VisGraph builds the visibility graph using Der-Tsai Lee's
    # visibility graph algorithm. Lee's algorithm has
    # a total running time of O(n^2 log n), making it
    # much more efficient than the naive algorithm
    # which checks every possible pair of vertices.
    #
    # LEE'S ALGORITHM PSEUDOCODE:
    #
    # visibility_graph(S <- disjoint polygonal obstacles)
    #     G <- all vertices of S
    #     VG -> empty visibility graph
    #     for each vertex v in G # O(n)
    #         do VG <- visible_vertices(v,S) # O(n log n)
    #     return VG
    g = vg.VisGraph()
    g.build(polygons)

    # the VisGraph shortest_path function computes the shortest path
    # between two points using Dijkstra's algorithm. It adds
    # the start and goal nodes to the visibility graph along
    # with the corresponding edges.
    # This fucntion runs in O(|E| + |V|log|V|)
    start = vg.Point(10000.0, 30000.0)
    goal = vg.Point(70597.0, 15000.0)
    shortest = g.shortest_path(start, goal)

    ################
    # PLOTING CODE #
    ################
    for p in polygons:
        plot_polygon(p)

    for e in g.visgraph.get_edges():
       plot_edge(e)

    plot_path(shortest)

    plt.plot(start.x, start.y, 'mo')
    plt.plot(goal.x, goal.y, 'mo')

    plt.show()


def plot_polygon(vertices):
    last_i = len(vertices) - 1
    for i in range(len(vertices)):
        v = vertices[i]
        if i == last_i:
            w = vertices[0]
        else:
            w = vertices[i + 1]
        plt.plot([v.x, w.x], [v.y, w.y], 'r-')


def plot_edge(edge):
    v = edge.p1
    w = edge.p2
    plt.plot([v.x, w.x], [v.y, w.y], 'b--')


def plot_path(path):
    for i in range(len(path) - 1):
        v = path[i]
        w = path[i + 1]
        plt.plot([v.x, w.x], [v.y, w.y], 'g-', linewidth=2.0)


if __name__ == '__main__':
    main()
