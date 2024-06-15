def My_function(integers, number=1):
    result = []
    for el in integers:
        if el == number:
            result.append(True)
        else:
            result.append(False)
    return any(result)


my_list = [1, 3, 9, 4]
assert My_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(My_function(my_list, 2))
