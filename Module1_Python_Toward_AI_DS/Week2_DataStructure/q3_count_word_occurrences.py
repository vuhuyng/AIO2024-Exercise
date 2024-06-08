def count_word(file_path):
    counter = {}

    # Your Code Here

    # End Code Here

    return counter

file_path = '/content/P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])
