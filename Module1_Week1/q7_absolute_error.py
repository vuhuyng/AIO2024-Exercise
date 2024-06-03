def calc_ae(y, y_hat):
    return abs(y - y_hat)


y = 1
y_hat =6
assert calc_ae(y, y_hat) == 5
y = 2
y_hat = 9
print(calc_ae(y, y_hat))