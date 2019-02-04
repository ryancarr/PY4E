# Name    : Exercise8-4.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Open a file, add unique words to list
#           Sort list and display results to user

# Text files are stored in the data folder one level up
filename = input('Enter a filename: ')
if filename == 'romeo.txt':
    filename = '../data/romeo.txt'
else:
    print('File cannot be opened:', filename)
    quit()

fh = open(filename, 'r')

words = []

for line in fh:
    for word in line.strip().split():
        if word not in words:
            words.append(word)
        else: continue

words.sort()
print(words)

fh.close()
