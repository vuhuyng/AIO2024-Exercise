def levenshteinDistanceDP(str1, str2):
    distances = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]

    for t1 in range(len(str1) + 1):
        distances[t1][0] = t1
    for t2 in range(len(str2) + 1):
        distances[0][t2] = t2

    for t1 in range(1, len(str1) + 1):
        for t2 in range(1, len(str2) + 1):
            if str1[t1 - 1] == str2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                distances[t1][t2] = min(a, b, c) + 1

    return distances[len(str1)][len(str2)]


distance = levenshteinDistanceDP("yu", "you")
print(distance)
