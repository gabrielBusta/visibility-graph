import numpy as np
import pyvisgraph as vg
from os import listdir
from matplotlib import pyplot as plt


def main():
    folder = 'obstacles'
    # load a list of the obstacle file names
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

    start = vg.Point(10000.0, 30000.0)
    goal = vg.Point(70597.0, 15000.0)

    g = vg.VisGraph()
    g.build(polygons)
    shortest = g.shortest_path(start, goal)
    print(shortest)
    for p in polygons:
        plot_polygon(p)

    for e in g.visgraph.get_edges():
        plot_edge(e)

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

        plt.text(v.x, v.y, str(v.x) + ',' + str(v.y), fontsize=10)
        plt.text(w.x, w.y, str(w.x) + ',' + str(w.y), fontsize=10)
        plt.plot([v.x, w.x], [v.y, w.y], 'r-')


def plot_edge(edge):
    v = edge.p1
    w = edge.p2
    plt.plot([v.x, w.x], [v.y, w.y], 'b--')


if __name__ == '__main__':
    main()
