import numpy as np
import matplotlib.pyplot as plt

def draw_fruits(arr, ratio=1):
    n = len(arr)
    rows = int(np.ceil(n / 10))
    cols = n if rows < 2 else 10
    fig, axs = plt.subplots(rows, cols,
                            figsize=(cols * ratio, rows * ratio), squeeze=False)
    for i in range(rows):
        for j in range(cols):
            if i * 10 + j < n:
                axs[i, j].imshow(arr[i * 10 + j], cmap='gray_r')
            axs[i, j].axis('off')
    plt.show()

# transform 3 dimension to 2 dimension array
fruits = np.load('fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100 * 100)

# reduce 1st dimention from 300 to 50 by PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=50)
pca.fit(fruits_2d)
# print(pca.components_.shape)
# draw_fruits(pca.components_.reshape(-1, 100, 100))

# reduce original data dimension from 10000 to 50
# print(fruits_2d.shape)
fruits_pca = pca.transform(fruits_2d)
# print(fruits_pca.shape)

# fruits_inverse = pca.inverse_transform(fruits_pca)
# print(fruits_inverse.shape)
# fruits_reconstruct = fruits_inverse.reshape(-1, 100, 100)
# for start in [0, 100, 200] :
#     draw_fruits(fruits_reconstruct[start:start+100])
#     print("\n")

# print(np.sum(pca.explained_variance_ratio_))
# plt.plot(pca.explained_variance_ratio_)
# plt.show()

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
target = np.array([0]*100 + [1]*100 + [2]*100)
from sklearn.model_selection import cross_validate
# cross check original data
# scores = cross_validate(lr, fruits_2d, target)
# print(np.mean(scores['test_score']))
# print(np.mean(scores['fit_time']))

# cross check PCA data
# scores = cross_validate(lr, fruits_pca, target)
# print(np.mean(scores['test_score']))
# print(np.mean(scores['fit_time']))

# find 50% ratio explained variation
pca = PCA(n_components=0.5)
pca.fit(fruits_2d)
# print(pca.n_components_)

fruits_pca = pca.transform(fruits_2d)
# print(fruits_pca.shape)
scores = cross_validate(lr, fruits_pca, target)
# print(np.mean(scores['test_score']))
# print(np.mean(scores['fit_time']))

# find cluster
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits_pca)
# print(np.unique(km.labels_, return_counts=True))

# for label in range(0, 3) :
#     draw_fruits(fruits[km.labels_ == label])
#     print("\n")

for label in range(0, 3):
    data = fruits_pca[km.labels_ == label]
    plt.scatter(data[:,0], data[:,1])
plt.legend(['apple', 'banana', 'pineapple'])
plt.show()
