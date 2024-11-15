import numpy as np

# np.random.seed(0)

if __name__ == "__main__":
    m = 10
    n = 8
    r = 4
    c = 3

    # a)
    A = np.random.random((m, r))
    print(f'A Rank = {np.linalg.matrix_rank(A)}')

    # b)
    for _ in range(n - r):
        new_col = np.zeros(m)
        for _ in range(c):
            new_col = np.add(new_col,
                                A[:, np.random.choice(A.shape[1], size=1, replace=False)].flatten()
                                * np.random.random()
                             )

        new_col = [[x] for x in new_col]
        A = np.append(A, new_col, axis=1)

    print(f'B Rank = {np.linalg.matrix_rank(A)}')

    # c)
    mean = 0
    std_dev = 0.02
    noise = np.random.normal(mean, std_dev, A.shape)
    A += noise
    print(f'C Rank = {np.linalg.matrix_rank(A)}')

    # d)
    # Se observa doar fluctuatii neglijabile intre unele din valorile singulare
    # Putem deduce ca pentru matricea neafectata de zgomot avem un rang mai mic
    U, S, V = np.linalg.svd(A)
    print(S)