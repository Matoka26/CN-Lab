import numpy as np

n = 3

def f(a: [[float]], b: [float]):
    for k in range(0,n-1):
        for i in range(k+1,n):
            # Calculeaza multiplicatorii Gaussieni
            a[i][k] = -a[i][k] / a[k][k]   # Se suprascriu in triunghiul inferior
            b[i] = b[i] + b[k] * a[i][k]
            # Aplica multiplicatorii
            for j in range(k+1,n):
                a[i][j] = a[i][j] + a[k][j] * a[i][k]

    a = np.triu(a)

def ltris(l: [[float]], b: [float]) -> [float]:
    x = b.copy()
    for i in range(n-1, -1, -1):
        for j in range(0, n-1-i):
            x[i] = x[i] - l[i][n-1-j] * x[j]
        x[i] = x[i] / l[i][i]
    return x


if __name__ == "__main__":
    A = [[2, 4, -2],
         [4, 9, -3],
         [-2, -3, 7]]
    b = np.array([2, 8, 10])
    f(A, b)
    print('A:\n', A)
    print('b:\n', b)
    print('X:\n', ltris(A, b))

    n = 6
    A = np.random.randn(n, n)
    b = np.random.randn(n)
    f(A, b)
    print('A:\n', A)
    print('b:\n', b)
    print('X:\n', ltris(A, b))




