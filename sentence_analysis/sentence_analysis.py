""""takes a strong from a user and counts
upper case letters, lower case letters, punctuation symbols, and total"""

sentence = input('Please, type in a sentence of your choice: ')

dict_ = {'lower': 0, 'upper': 0, 'punct': 0, 'total': 0}
sentence = sentence.replace(' ','')
for char in sentence:
    if char.islower():
        dict_['lower'] += 1
    elif char.isupper():
        dict_['upper'] += 1
    else:
        dict_['punct'] += 1
dict_['total'] = dict_['upper'] + dict_['lower'] + dict_['punct']
print(f"Lower case letters: {dict_['lower']}.\nUpper case letters: {dict_['upper']}.\n"
      f"Punctuation: {dict_['punct']}\nTotal: {dict_['total']}")