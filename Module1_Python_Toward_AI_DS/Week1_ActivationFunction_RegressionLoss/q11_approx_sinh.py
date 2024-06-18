def factorial(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result


def approx_sinh(x, n):
    result = 0
    for i in range(n):
        part1 = x ** (2 * i + 1)
        part2 = factorial(2 * i + 1)
        result += part1 / part2
    return result


assert round(approx_sinh(x=1, n=10), 2) == 1.18
print(round(approx_sinh(x=3.14, n=10), 2))
