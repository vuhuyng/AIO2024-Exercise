def mean_difference_n_root_error(y, y_hat, n, p):
    return abs((y_hat ** (1 / n)) - (y ** (1 / n))) ** p


if __name__ == '__main__':
    y = float(input('Enter y: '))
    y_hat = float(input('Enter y_hat: '))
    n = int(input('Enter n:'))
    p = int(input('Enter p:'))

    print(mean_difference_n_root_error(y, y_hat, n, p))
