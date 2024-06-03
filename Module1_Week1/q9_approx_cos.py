def factorial(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result

def approx_cos(x, n):
    result = 0
    for i in range(n):
        part1 = (-1) ** i
        part2 = x ** (2 * i)
        part3 = factorial(2 * i)
        result += part1 * (part2 / part3)
    return result

assert round(approx_cos(x=1, n=10), 2)==0.54
print(round(approx_cos(x=3.14, n=10), 2))

        
    
