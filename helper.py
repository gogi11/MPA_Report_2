import math

import numpy as np


def distance(p1, p2):
    return (((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)) ** 0.5


def cost(cluster, centers):
    total = 0
    for point in cluster:
        dist = math.inf
        for center in centers:
            dist = min(distance(point, center) ** 2, dist)
        total += dist
    return total


def costCoreset(coreset, centers):
    total = 0
    for point in coreset:
        dist = math.inf
        for center in centers:
            dist = min(point["weight"] * distance(point["point"], center) ** 2, dist)
        total += dist
    return total


def isPointInRect(point, rect):
    return rect[0] <= point[0] <= rect[1] and rect[2] <= point[1] <= rect[3]


def allSquaresInCircle(center, radius, squareSize):
    nr_rows = radius * 2 / squareSize
    x1 = center[0] - radius
    y1 = center[1] - radius

    all_squares = []
    for i in range(0, math.ceil(nr_rows)):
        for j in range(0, math.ceil(nr_rows)):
            all_squares.append([
                x1 + i * squareSize,
                x1 + (i + 1) * squareSize,
                y1 + j * squareSize,
                y1 + (j + 1) * squareSize
            ])
    return all_squares


def deleteIndicesFromNumpyArray(arr, indices):
    i = 0
    for index in indices:
        arr = np.delete(arr, index - i, axis=0)
        i += 1
    return arr

