import numpy as np
import pyvisgraph as vg
from matplotlib import pyplot as plt
from os import listdir


def main():
    folder = 'obstacles'
    files = listdir(folder)
    polygons = []

    for f in files:
        x, y = np.loadtxt(folder + '/' + f)
        polygon = [vg.Point(x, y) for x, y in zip(x, y)]
        polygons.append(polygon)

    start = vg.Point(13485.0, 57876.0)
    goal = vg.Point(12832.0, 42957.0)

    g = vg.VisGraph()
    g.build(polygons)

    shortest = g.shortest_path(start, goal)

    print g.visgraph.get_edges()

    for polygon in polygons:
        plot_polygon(polygon, 'b')

    plt.show()


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
