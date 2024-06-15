def my_function(n):
    result = -(10*100)
    for e in n:
        if e > result:
            result = e
    return result


my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001

my_list = [1, 9, 9, 0]
print(my_function(my_list))
