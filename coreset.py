import random
from helper import *


def coresetConstruction(points, centroids, epsilon=0.2):
    coreset = []

    n = len(points)
    dimensions = 2
    a = 1
    log_n = math.log(n)
    z = log_n * math.log(a * log_n)

    radius = math.sqrt(cost(points, centroids) / (a * log_n * n))

    for j in range(0, math.ceil(z)):
        radius_to_power = radius * (2 ** j)
        x = epsilon * radius_to_power / math.sqrt(dimensions)

        for centroid in centroids:
            for square in allSquaresInCircle(centroid, radius_to_power, x):
                all_points_in_square = []
                all_indices = []

                for i, point in enumerate(points):
                    if isPointInRect(point, square) and isPointInCircle(point, centroid, radius_to_power):
                        all_indices.append(i)
                        all_points_in_square.append(point)

                if len(all_points_in_square) > 0:
                    # select arbitrary point as representative (rep)
                    rep = all_points_in_square[math.floor(random.random() * len(all_points_in_square))]
                    coreset.append({
                        "point": rep,
                        "weight": len(all_points_in_square),
                        "represents": all_points_in_square
                    })
                    points = deleteIndicesFromNumpyArray(arr=points, indices=all_indices)

    return coreset
