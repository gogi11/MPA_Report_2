import math
import random

from helper import distance


def kMeansPlusPlus(points, k):
    n = len(points)
    centroids = [[0, 0] for _ in range(k)]
    centroids[0] = points[random.randint(0, n)]
    min_distances = [math.inf for _ in range(n)]
    cumulative = [0.0 for _ in range(n)]
    sampled_index = 0

    for i in range(1, k):
        for j in range(0, n):
            x = distance(points[j], centroids[i - 1]) ** 2
            if min_distances[j] > x:
                min_distances[j] = x
        cumulative[0] = min_distances[0]

        for j in range(1, n):
            cumulative[j] = cumulative[j - 1] + (min_distances[j])

        x = random.random() * cumulative[n - 1]

        if x <= cumulative[0]:
            sampled_index = 1
        else:
            for j in range(1, n):
                if cumulative[j - 1] < x <= cumulative[j]:
                    sampled_index = j
        centroids[i] = points[sampled_index]
    return centroids


def kMeansPlusPlusCoreset(coreset, k):
    n = len(coreset)
    centroids = [[0, 0] for _ in range(k)]
    centroids[0] = coreset[random.randint(0, n)]["point"]
    min_distances = [math.inf for _ in range(n)]
    cumulative = [0.0 for _ in range(n)]
    sampled_index = 0

    for i in range(1, k):
        for j in range(0, n):
            x = coreset[j]["weight"] * distance(coreset[j]["point"], centroids[i - 1])**2
            if min_distances[j] > x:
                min_distances[j] = x
        cumulative[0] = min_distances[0]

        for j in range(1, n):
            cumulative[j] = cumulative[j - 1] + (min_distances[j])

        x = random.random() * cumulative[n - 1]

        if x <= cumulative[0]:
            sampled_index = 1
        else:
            for j in range(1, n):
                if cumulative[j - 1] < x <= cumulative[j]:
                    sampled_index = j
        centroids[i] = coreset[sampled_index]["point"]
    return centroids
