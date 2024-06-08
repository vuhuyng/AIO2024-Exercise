import math

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

def approx_cos(x, n):
    result = 0
    for i in range(n):
        part1 = (-1) ** i
        part2 = x ** (2 * i)
        part3 = factorial(2 * i)
        result += part1 * (part2 / part3)
    return result

def approx_sinh(x, n):
    result = 0
    for i in range(n):
        part1 = x ** (2 * i + 1)
        part2 = factorial(2 * i + 1)
        result += part1 / part2
    return result

def approx_cosh(x, n):
    result = 0
    for i in range(n):
        part1 = x ** (2 * i)
        part2 = factorial(2 * i)
        result += (part1 / part2)
    return result


if __name__ == "__main__":
    x = float(input('Enter x (radian (0,2pi]): '))
    n = int(input('Enter n (int): '))

    if x > 0 and x <= 2 * math.pi:
        print(f'appox sin x:{x}, n:{n} = {approx_sin(x, n)}')
        print(f'appox cos x:{x}, n:{n} = {approx_cos(x, n)}')
        print(f'appox sinh x:{x}, n:{n} = {approx_sinh(x, n)}')
        print(f'appox cosh x:{x}, n:{n} = {approx_cosh(x, n)}')



    
    
