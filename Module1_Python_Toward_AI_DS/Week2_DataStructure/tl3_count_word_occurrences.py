def word_count(file_path):
    result = dict()
    with open(file_path, 'r') as f:
        conten = f.read()
    conten = conten.lower().strip().split()
    for char in conten:
        key = char
        count = 0
        for value_count in conten:
            if key == value_count:
                count += 1
        result[key] = count
    return dict(sorted(result.items()))


file_path = 'Module1_Python_Toward_AI_DS/Week2_DataStructure/P1_data.txt'
print(word_count(file_path))
