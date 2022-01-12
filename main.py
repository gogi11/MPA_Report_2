from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from coreset import coresetConstruction
from kMeansPP import kMeansPlusPlus


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

    plt.plot([g[0] for g in blobs], [g[1] for g in blobs], 'bo')
    plt.plot([g["point"][0] for g in coreset], [g["point"][1] for g in coreset], 'ro')
    plt.plot([g[0] for g in centroids], [g[1] for g in centroids], 'yo')
    plt.show()


if __name__ == '__main__':
    main()
