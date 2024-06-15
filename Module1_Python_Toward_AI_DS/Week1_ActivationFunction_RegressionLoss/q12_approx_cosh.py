def factorial(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result


def approx_cosh(x, n):
    result = 0
    for i in range(n):
        part1 = x ** (2 * i)
        part2 = factorial(2 * i)
        result += (part1 / part2)
    return result


import math

assert math.isclose(approx_cosh(x=1, n=10), 1.54, rel_tol=1e-9, abs_tol=0.0)
print(round(approx_cosh(x=3.14, n=10), 2))
