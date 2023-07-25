phrase = str(input("Please, write any sentence: ")).strip()

print('How many times does the letter "A" appear:', phrase.lower().count('a'))
print('In which position does the letter "A" appear first:', (phrase.lower().find('a') + 1))
print('In which position does the letter "A" appear lastly:', (phrase.lower().rfind('a') + 1))
