import math


def calc_sig(x):
    return 1 / (1 + math.e ** (-x))


expected_value = 0.95
calculated_value = calc_sig(3)
tolerance = 0.01

assert abs(calculated_value - expected_value) < tolerance
print(round(calc_sig(2), 2))
