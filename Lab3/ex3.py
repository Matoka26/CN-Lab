from sklearn import datasets, decomposition
import matplotlib.pyplot as plt

if __name__ == "__main__":
    iris = datasets.load_iris()

    n_components = 2
    pca = decomposition.PCA(n_components=n_components)
    x_pca = pca.fit_transform(iris.data)

    plt.scatter(x_pca[:, 0], x_pca[:, 1])
    plt.grid(True)
    plt.show()
