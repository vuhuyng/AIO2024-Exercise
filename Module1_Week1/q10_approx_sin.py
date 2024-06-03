def factorial(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result

def approx_sin(x, n):
    result = 0
    for i in range(n):
        part1 = (-1) ** i
        part2 = x ** (2 * i + 1)
        part3 = factorial(2 * i + 1)
        result += part1 * (part2 / part3)
    return result


assert round(approx_sin(x=1, n=10), 4)==0.8415
print(round(approx_sin(x=3.14, n=10), 4))
