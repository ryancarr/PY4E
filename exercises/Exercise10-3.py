# Name    : Exercise10-3.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Open a file, count letters and display frequency to user

# Text files are stored in the data folder one level up
filename = input('Enter a filename: ')
if filename == 'romeo.txt':
    filename = '../data/romeo.txt'
else:
    print('File cannot be opened:', filename)
    quit()

fh = open(filename, 'r')

letters = {}

for line in fh:
    for letter in line.lower():
        if not letter.isalpha():
            continue
        else:
            letters[letter] = letters.get(letter, 0) + 1

frequency = []

for k,v in letters.items():
    frequency.append((v, k))

frequency.sort(reverse=True)

for letter in frequency:
    print(letter[1], letter[0])
