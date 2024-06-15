def levenshtein_distance(token1, token2):
    distances = [[0] * (len(token2) + 1) for i in range(len(token1) + 1)]

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1
    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                distances[t1][t2] = min(a, b, c) + 1

    distance = float(distances[len(token1)][len(token2)])
    return distance


assert levenshtein_distance("hi", "hello") == 4.0
print(levenshtein_distance("hola", "hello"))
