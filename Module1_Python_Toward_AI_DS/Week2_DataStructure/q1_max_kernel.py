def max_kernel(num_list, k):
    result = []
    start = 0
    end = k
    max_value = -99999999999999999999999999999999999999999
    for _ in num_list:
        if end > len(num_list):
            return result
        for i in range(start, end):
            if max_value < num_list[i]:
                max_value = num_list[i]
        result.append(max_value)
        start += 1
        end += 1
    return result


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
