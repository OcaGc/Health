letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
clean_string = ''
for letter in letters:
    if not letter.isupper():
        clean_string += letter
letters = clean_string
print(letters)