import numpy as np
import pyvisgraph as vg
from os import listdir
from scipy.spatial import Delaunay
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
    obstacles = []
    for f in files:
        # each file on the obtacle course's folder contains
        # the coordinates of an obstacle's vertices in the format:
        # x1, x2, x3,..., xn
        # y1, y2, y3,..., yn
        x, y = np.loadtxt(folder + '/' + f)
        vertices = list(zip(x, y))
        obstacles.append(vertices)

    # the polygons list contains a list of triangles
    # representing the obstacles on the plane
    # polygons = []
    # for vertices in obstacles:
        # triagulate the obstacle using it's vertices
        # triangles = triangulate(vertices)
        # triangulate returns numpy arrays. Threfore, we need to
        # convert these arrays into vg.Points before we can use
        # the visibilty graph algorithm in pyvisgraph
        # for triangle in triangles:
            # polygons.append(convert_to_vg_points(triangle))

    # start = vg.Point(13485.0, 57876.0)
    # goal = vg.Point(12832.0, 42957.0)

    polygons = [[vg.Point(0.0,1.0), vg.Point(3.0,1.0), vg.Point(1.5,4.0), vg.Point(0.0, 4.0)],
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

    for vertices in polygons:
        plot_segments(vertices, 'b')

    plt.show()


def triangulate(vertices):
    triangulation = Delaunay(vertices)
    triangles = []
    for simplex in triangulation.simplices:
        triangles.append(indexes_to_points(simplex, triangulation.points))
    return triangles


def indexes_to_points(simplex, points):
    return [points[simplex[0]], points[simplex[1]], points[simplex[2]]]


def convert_to_vg_points(triangle):
    vg_triangle = []
    for vertex in triangle:
        vg_triangle.append(vg.Point(vertex[0], vertex[1]))
    return vg_triangle


def plot_segments(vertices, color):
    last_i = len(vertices) - 1

    for i in range(len(vertices)):
        v = vertices[i]
        if i == last_i:
            w = vertices[0]
        else:
            w = vertices[i + 1]
        plt.plot([v.x, w.x], [v.y, w.y], color + '-')


if __name__ == '__main__':
    main()
