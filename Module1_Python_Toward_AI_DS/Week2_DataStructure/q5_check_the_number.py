def check_the_number(n):
    list_of_numbers = []
    for _ in range(1, 5):
        if n in list_of_numbers:
            results = "True"
        if n not in list_of_numbers:
            results = "False"
    return results


N = 7
assert check_the_number(N) == "False"

N = 2
results = check_the_number(N)
print(results)
