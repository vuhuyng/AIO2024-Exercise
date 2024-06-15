def my_function(n):
    result = 10**100
    for e in n:
        if e < result:
            result = e
    return result


my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100

my_list = [1, 2, 3, -1]
print(my_function(my_list))
