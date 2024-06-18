def character_count(word):
    character_statistic = {}
    for w in word:
        key = w
        value = 0
        for count in word:
            if key == count:
                value += 1
        character_statistic[key] = value
    return character_statistic


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))
