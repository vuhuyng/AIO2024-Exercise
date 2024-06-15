def window_maximum(num_list, k):
    result = []
    start = 0
    end = k
    max = -9999999999999999999999999
    for _ in num_list:
        if end > len(num_list):
            return result
        for i in range(start, end):
            if num_list[i] > max:
                max = num_list[i]
        result.append(max)
        start += 1
        end += 1
    return result


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(window_maximum(num_list, k))
