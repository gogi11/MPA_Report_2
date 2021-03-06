import math
import random

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


def isPointInCircle(point, center, radius):
    return distance(point, center) <= radius


def generateRandomPointInSquare(square):
    return [
        square[0] + (square[1] - square[0]) * random.random(),
        square[2] + (square[3] - square[2]) * random.random()
    ]


def allSquaresInCircle(center, radius, square_size):
    nr_rows = math.ceil(radius * 2 / square_size)
    x1 = center[0] - radius
    y1 = center[1] - radius

    all_squares = []
    for i in range(0, nr_rows):
        for j in range(0, nr_rows):
            all_squares.append([
                x1 + i * square_size,
                x1 + (i + 1) * square_size,
                y1 + j * square_size,
                y1 + (j + 1) * square_size
            ])
    return all_squares


def deleteIndicesFromNumpyArray(arr, indices):
    i = 0
    for index in indices:
        arr = np.delete(arr, index - i, axis=0)
        i += 1
    return arr
