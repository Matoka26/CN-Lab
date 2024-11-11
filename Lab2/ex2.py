import matplotlib.pyplot as plt
import numpy as np
import pickle
import networkx

graphs_path = "./graphs.pickle"

if __name__ == "__main__":
    with open(graphs_path, 'rb') as f:
        matrices = pickle.load(f)

    for i, mat in enumerate(matrices):
        graph = networkx.convert_matrix.from_numpy_array(mat)

        networkx.draw(graph, with_labels=True)
        plt.show()

        eigs = np.linalg.eig(matrices[i])
        eig_vals = np.unique(np.round(eigs.eigenvalues, 3)) # ty sir skpha for this one

        print(f'Eigen values for graph {i}: {eigs}')

        max_clique = networkx.algorithms.approximation.clique.max_clique(graph)
        print(f'Max clique for graph {i}: {max_clique}')

        print(f'Is complete? {len(eig_vals) == 2}')
        print(f'Is bipartite? {np.allclose(-1 * max(eigs.eigenvalues), min(eigs.eigenvalues))}')