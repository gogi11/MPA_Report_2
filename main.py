import math
import random


def isPointInRect(p, rect):
    [x, y] = p
    [x1, x2, y1, y2] = rect
    return x1 <= x <= x2 and y1 <= y <= y2


def allSquaresInCircle(center, radius, squareSize):
    nrRows = radius * 2 / squareSize
    x1 = center[0] - radius
    y1 = center[1] - radius

    allSquares = []
    for i in range(0, nrRows):
        for j in range(0, nrRows):
            allSquares.push([
                x1 + i*squareSize, 
                x1 + (i+1)*squareSize,
                y1 + j*squareSize, 
                y1 + (j+1)*squareSize
            ])
    return allSquares

        


def coresetConstruction(points, epsilon=0.2):
    coreset = []

    n = len(points)
    d = 2
    a = 1
    logN = math.log(n)
    z = logN * math.log(a * logN)

    centers = kMeansPlusPlus()
    radius = math.sqrt(cost(points, centers) / (a * logN * n))

    for j in range(0, z):
        radius = radius * (2**j)
        x = epsilon * radius / math.sqrt(d)
        
        for center in centers:
            for square in allSquaresInCircle(center, radius, x):
                allPointsInSquare = []
                for point in points:
                    if isPointInRect(point, square):
                        allPointsInSquare.append(point)
                if len(allPointsInSquare) > 0:
                    # select abritrary point as rep
                    rep = allPointsInSquare[math.floor(random.random() * len(allPointsInSquare))]
                    coreset.append({"point": rep, "weight": len(allPointsInSquare)})
                    for point in allPointsInSquare:
                        points.remove(point)
    return coreset
                

            

        




def kMeansPlusPlus(points, k):
    n = len(points)
    centroids = []
    centroids[0] = points[random.randint(0, n)]
    minDistances = []
    cumulative = []
    sampledIndex = 0

    for i in range(0, n):
        minDistances[i] = math.inf # 999999999

    for i in range(1, k):
        for j in range(0, n):
            x = distance(points[j], centroids[i-1])
            if minDistances[j] > x:
                minDistances[j] = x
        cumulative[0] = minDistances[0] * minDistances[0];

        for j in range (1, n):
            cumulative[j] = cumulative[j- 1] + (minDistances[j] * minDistances[j])
        
        x = random.randrange(0, 1)
        x = x*cumulative[n-1]

        if x <= cumulative[0]:
            sampledIndex = 1
        else:
            for j in range(1, n):
                if x > cumulative[j-1] & x <= cumulative[j]:
                    sampledIndex = j
        centroids[i] = points[sampledIndex]

def distance(pointA, pointB):
    return ((((pointB[0] - pointA[0])**2) + ((pointB[1] - pointA[1])**2))**0.5)

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