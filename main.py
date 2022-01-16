from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from sklearn.datasets import *

from clustering import getClusters, getClustersCoreset
from coreset import coresetConstruction
from kMeansPP import kMeansPlusPlus, kMeansPlusPlusCoreset
import pandas as pd


def generateData(sampleSize):
    blobs = make_blobs(n_samples=sampleSize, random_state=16, n_features=4)[0]
    moons = make_moons(n_samples=sampleSize, random_state=16, noise=0.1)[0]/10
    for i in range(1, 10):
        moons += make_moons(n_samples=sampleSize, random_state=i, noise=0.1)[0]/10

    # ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude'], [price]
    # around 1020 cities, i.e. k = 1020?
    california_data = fetch_california_housing(return_X_y=True)
    real_data_1 = []
    for i in range(len(california_data[0])):
        real_data_1.append([california_data[0][i][6], california_data[0][i][7]])

    ed_earnings = pd.read_csv('./ed_earnings.csv')
    real_data_2 = []

    max_age = ed_earnings["Age"].max()
    max_income = ed_earnings["Income"].max()
    for i in range(ed_earnings.shape[0]):
        real_data_2.append([ed_earnings["Age"][i] / max_age, ed_earnings["Income"][i] / max_income])

    return [blobs, moons, real_data_2]


def main(dataset, k=3):
    start_time = datetime.now()
    centroids = kMeansPlusPlus(points=dataset, k=k)
    print("k-means++ took " + str(datetime.now() - start_time))

    start_time = datetime.now()
    coreset, squares = coresetConstruction(points=dataset, centroids=centroids)
    print("Coreset Construction took " + str(datetime.now() - start_time))

    coreset_centroids = kMeansPlusPlusCoreset(coreset=coreset, k=k)

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#777']
    i = 0

    fig, ax = plt.subplots()

    for cluster in getClusters(dataset, centroids):
        ax.plot([g[0] for g in cluster], [g[1] for g in cluster], 'o', color=colors[i % len(colors)])
        i += 1

    # for cluster in getClustersCoreset(coreset, coreset_centroids):
    #     point_x = []
    #     point_y = []
    #     for g in cluster:
    #         # print(g)
    #         point_x.extend([q[0] for q in g["represents"]])
    #         point_y.extend([q[1] for q in g["represents"]])
    #     ax.plot(point_x, point_y, 'o', color=colors[i % len(colors)])
    #     i += 1
        # plt.plot([g["point"][0] for g in cluster], [g["point"][1] for g in cluster], 'o', color=colors[i])
        # i += 1

    # ax.plot([g[0] for g in centroids], [g[1] for g in centroids], 'o', color=colors[i% len(colors)])
    # i += 1

    # ax.plot([g[0] for g in coreset_centroids], [g[1] for g in coreset_centroids], 'o', color=colors[i])
    # i += 1

    # for square in squares[0:6]:
    #     for s in square:
    #         rect = patches.Rectangle((s[0], s[2]), s[1] - s[0], s[3] - s[2], linewidth=1, edgecolor='k',
    #                                  facecolor='none')
    #         ax.add_patch(rect)

    # print(squares[-1])

    plt.show()


if __name__ == '__main__':
    dataset = generateData(1000)[0]
    main(dataset, 3)
