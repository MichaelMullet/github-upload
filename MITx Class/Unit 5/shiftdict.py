import string
symbols = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
dictionary = {}
shift = 3
for i in range(26):
    dictionary[symbols[i]] = symbols[i + shift]
    dictionary[symbols[i].upper()] = symbols[i + shift].upper()
return dictionary

print(dictionary)