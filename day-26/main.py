from tarfile import PAX_NAME_FIELDS


import pandas
nato_datafram = pandas.read_csv('nato_phonetic_alphabet.csv')
input = input('enter a word')
nato_dict = {row.letter:row.code for (index, row) in nato_datafram.iterrows()}


result = {valuue for (key, valuue) in nato_dict.items() if key in input}
print(result)

result2 = [nato_dict[n] for n in input]
print(result2)