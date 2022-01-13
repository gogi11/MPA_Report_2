from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

from clustering import getClusters, getClustersCoreset
from coreset import coresetConstruction
from kMeansPP import kMeansPlusPlus, kMeansPlusPlusCoreset


def main():
    start_time = datetime.now()
    blobs = make_blobs(n_samples=10000)[0]
    print("Blobs Generation took " + str(datetime.now() - start_time))

    start_time = datetime.now()
    centroids = kMeansPlusPlus(points=blobs, k=3)
    print("k-means++ took " + str(datetime.now() - start_time))

    start_time = datetime.now()
    coreset = coresetConstruction(points=blobs, centroids=centroids)
    print("Coreset Construction took " + str(datetime.now() - start_time))

    coreset_centroids = kMeansPlusPlusCoreset(coreset=coreset, k=3)

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#777']
    i = 0

    print(len(centroids))

    for cluster in getClusters(blobs, centroids):
        plt.plot([g[0] for g in cluster], [g[1] for g in cluster], colors[i] + 'o')
        i += 1

    for cluster in getClustersCoreset(coreset, coreset_centroids):
        plt.plot([g["point"][0] for g in cluster], [g["point"][1] for g in cluster], colors[i] + 'o')
        i += 1

    plt.plot([g[0] for g in centroids], [g[1] for g in centroids], colors[i] + 'o')
    i += 1

    plt.plot([g[0] for g in coreset_centroids], [g[1] for g in coreset_centroids], 'o', color=colors[i])
    i += 1

    plt.show()


if __name__ == '__main__':
    main()
