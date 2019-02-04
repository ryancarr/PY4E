# Name    : Exercise8-5.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Open a file, extract email addresses
#           Display email addresses on screen followed by total count

# Text files are stored in the data folder one level up
filename = input('Enter a filename: ')
if filename == 'mbox-short.txt':
    filename = '../data/mbox-short.txt'
else:
    print('File cannot be opened:', filename)
    quit()

fh = open(filename, 'r')

count = 0

for line in fh:
    if not line.startswith('From') or line.startswith('From:'):
        continue
    print(line.split()[1])
    count += 1

print('There were', count, 'lines in the file with From as the first word')
