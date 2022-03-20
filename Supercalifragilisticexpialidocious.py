word = 'Supercalifragilisticexpialidocious'
print('Supercalifragilisticexpialidocious is {} characters long.'.format(len(word)))
print('I will skip every other letter and create a new word:')
new_word = ''
for i, char in enumerate(word):
  if i % 2 == 0:
    new_word = new_word + str(char)

print(new_word)

print('Now break the word into two parts: ')
half = int(len(word)/2)
print(half)
print(word[0:half])
print(word[half:len(word)+1])

count = len(word)
new_word = ''
while count > 0:
  new_word = new_word + word[count-1].lower()
  count -= 1

print('Backwards: ')
print(new_word.title())
