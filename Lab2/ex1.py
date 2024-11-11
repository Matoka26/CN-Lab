import numpy as np

# np.random.seed(0)


def power_method(mat: np.ndarray, max_iterations=100, tolerance=1e-6) -> (float, np.ndarray):
    err = 1
    it = 0

    y = np.random.rand(len(mat))
    y = np.divide(y, np.linalg.norm(y))

    while err > tolerance:
        if it > max_iterations:
            break

        acc = np.dot(mat, y)
        acc = np.divide(acc, np.linalg.norm(acc))

        y = acc
        error = np.linalg.norm(acc - y)
        it += 1

    eig_val = np.dot(y, np.dot(mat, y)) / np.dot(y, y)
    return eig_val, y


if __name__ == "__main__":
    n = 6
    matrix = np.random.randint(10, size=(n, n))

    np_eig_res = np.linalg.eig(matrix)
    pow_met_res = power_method(matrix, 100)

    print(f'NP eigen values: {np_eig_res[0]}')
    print(f'My eigen value: {pow_met_res[0]}')

    print(f'NP eigen vectors: {np_eig_res[1]}')
    print(f'My eigen vector: {pow_met_res[1]}')
