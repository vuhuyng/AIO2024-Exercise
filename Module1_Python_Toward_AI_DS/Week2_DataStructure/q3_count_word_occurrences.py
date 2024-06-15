def count_word(file_path):
    counter = {}

    with open(file_path, 'r') as f:
        conten = f.read()
    conten = conten.lower().strip().split()
    for char in conten:
        key = char
        count = 0
        for value_count in conten:
            if key == value_count:
                count += 1
        counter[key] = count
    return counter


file_path = 'Module1_Python_Toward_AI_DS/Week2_DataStructure/P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])
