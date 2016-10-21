import numpy as np
import pyvisgraph as vg
from os import listdir
from scipy.spatial import Delaunay
from matplotlib import pyplot as plt


def main():
    folder = 'obstacles'
    files = listdir(folder)
    polygons = []

    for f in files:
        x, y = np.loadtxt(folder + '/' + f)
        polygon = [vg.Point(x, y) for x, y in zip(x, y)]
        polygons.append(polygon)

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
    for polygon in polygons:
        plot_polygon(polygon, 'b')

    plt.show()


def triangulate(vertices):


def plot_path(path):
    pass


def plot_polygon(polygon, color):
    last_i = len(polygon) - 1

    for i in range(len(polygon)):
        v = polygon[i]
        if i == last_i:
            w = polygon[0]
        else:
            w = polygon[i + 1]
        plt.plot([v.x, w.x], [v.y, w.y], color + '-')


if __name__ == '__main__':
    main()
