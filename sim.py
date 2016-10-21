import numpy as np
import pyvisgraph as vg
from os import listdir
from scipy.spatial import Delaunay
from matplotlib import pyplot as plt


def main():
    folder = 'obstacles'
    files = listdir(folder)
    # each element of the list of obstacles is a list of vertices
    # (e.g. points) representing a figure on the plane.
    #
    #     obstacle 0        obstacle 1            obstacle n
    # [[v1, v2,..., vn], [v1, v2,..., vn],..., [v1, v2,..., vn]]
    obstacles = []

    for f in files:
        x, y = np.loadtxt(folder + '/' + f)
        vertices = [[x, y] for x, y in zip(x, y)]
        obstacles.append(vertices)

    '''
    start = vg.Point(13485.0, 57876.0)
    goal = vg.Point(12832.0, 42957.0)

    polygons = [[vg.Point(0.0,1.0), vg.Point(3.0,1.0), vg.Point(1.5,4.0)],
                [vg.Point(4.0,4.0), vg.Point(7.0,4.0), vg.Point(5.5,8.0)]]

    start = vg.Point(1.5,0.0)
    goal = vg.Point(4.0, 6.0)

    g = vg.VisGraph()
    g.build(polygons)

    shortest = g.shortest_path(start, goal)

    vis_edges = g.visgraph.get_edges()

    for edge in vis_edges:
        v = edge.p1
        w = edge.p2
        plt.plot([v.x, w.x], [v.y, w.y], 'r')

    '''
    for vertices in obstacles:
        plot_segments(vertices, 'b')

    plt.show()


def triangulate(vertices):
    pass

def plot_path(path):
    pass


def plot_segments(vertices, color):
    last_i = len(vertices) - 1

    for i in range(len(vertices)):
        v = vertices[i]
        if i == last_i:
            w = vertices[0]
        else:
            w = vertices[i + 1]
        plt.plot([v[0], w[0]], [v[1], w[1]], color + '-')


if __name__ == '__main__':
    main()
