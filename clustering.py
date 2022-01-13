import math

from helper import distance


def getClusters(points, centers):
    clusters = [[] for k in centers]

    for point in points:
        min_center = -1
        min_distance = math.inf
        for i, center in enumerate(centers):
            dist = distance(point, center)**2
            if dist < min_distance:
                min_distance = dist
                min_center = i
        clusters[min_center].append(point)
    return clusters


def getClustersCoreset(points, centers):
    clusters = [[] for k in centers]

    for point in points:
        min_center = -1
        min_distance = math.inf
        for i, center in enumerate(centers):
            dist = point["weight"]*distance(point["point"], center)**2
            if dist < min_distance:
                min_distance = dist
                min_center = i
        clusters[min_center].append(point)
    return clusters
