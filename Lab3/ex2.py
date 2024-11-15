import matplotlib.pyplot as plt
from scipy import misc
import numpy as np

if __name__ == "__main__":
    A = misc.face(gray=True)
    m, n = A.shape
    # k = np.random.randint(low=0, high=min(m, n)-1)
    ks = [10, 20, 40]

    U, S, V = np.linalg.svd(A)

    for k in ks:
        Ak = np.matmul(np.matmul(U[:, 1:k], np.diag(S[1:k])), V[1:k, :])
        plt.imshow(Ak, cmap=plt.cm.gray)
        plt.show()
