from sklearn import datasets
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
# load iris data
iris = datasets.load_iris()
X = iris.data
y = iris.target

# fit a PCA
pca = PCA(n_components = 2, whiten = True)
pca.fit(X) # train

# project the data in 2D
X_pca = pca.transform(X)

# visualize the data
target_ids = range(len(iris.target_names))
plt.figure(figsize=(6,5))
for i, c, label in zip(target_ids, 'rgbcmykw', iris.target_names):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], c = c, label = label )
plt.legend()
plt.show()

