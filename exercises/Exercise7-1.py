# Name    : Exercise7-1.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Open a file, convert all text to uppercase
#           and print result to screen

# Text files are stored in the data folder one level up
filename = '../data/mbox-short.txt'

fh = open(filename,'r')
for line in fh:
    print(line.strip().upper())

fh.close()
