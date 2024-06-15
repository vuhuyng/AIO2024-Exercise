def count_chars(string):
    result = dict()
    for char in string:
        key = char
        count = 0
        for value in string:
            if value == key:
                count += 1
            result[char] = count

    return dict(sorted(result.items()))


string = 'Happiness'
print(count_chars(string))

string = 'smiles'
print(count_chars(string))
