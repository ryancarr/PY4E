# Name    : Exercise7-2.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Open a file, calculate average spam confidence
#           Display result to user

# Text files are stored in the data folder one level up
filename = input('Enter a filename: ')
if filename == 'mbox-short.txt':
    filename = '../data/mbox-short.txt'
elif filename == 'mbox.txt':
    filename = '../data/mbox.txt'

fh = open(filename, 'r')

count = 0
total = 0.0

for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'): continue

    position = line.find(':')
    number = float(line[position + 1:])
    total += number
    count += 1

average = total / count

print('Average spam confidence:', average)

fh.close()
