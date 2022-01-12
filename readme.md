# (k, epsilon)-coreset for the k-means problem


## Installation:
``pip install -r requirements.txt``

## How to use:
1. Calculate `k` centroids with `kMeansPlusPlus(points, k)`
1. Calculate the `(k, epsilon)` coreset of those centroids with `coresetConstruction(blobs, centroids)`
1. Profit?????

## Files:
1. `coreset.py` - contains the coreset function
1. `kMeansPP.py` - contains the k-means function
1. `helper.py` - contains all the other functions,
 which either are not part of the 2 other functions, or save space