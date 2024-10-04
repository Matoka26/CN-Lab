import decimal

min = 2.2250738585072014e-308
nof_iterations = 60
x0 = 0.1


def serie(n: float):
    x = decimal.Decimal(n).quantize(decimal.Decimal('0.00'))
    if x < 0 \
            or x > 1\
            or x == 0.5:
        raise Exception("Invalid number")

    return 2 * x if x < 0.5 else 2 * x - 1


if __name__ == "__main__":
    xk = x0
    for _ in range(nof_iterations):
        xk = serie(xk)
        print(f"{xk:0,.4f}", end=", ")
