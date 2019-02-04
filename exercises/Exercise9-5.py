# Name    : Exercise9-5.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Open a file, extract email domain and keep running count
#           Store data in dictionary and output result for user

# Text files are stored in the data folder one level up
filename = input('Enter a filename: ')
if filename == 'mbox-short.txt':
    filename = '../data/mbox-short.txt'
else:
    print('File cannot be opened:', filename)
    quit()

fh = open(filename, 'r')

emails = {}

for line in fh:
    # Only use data from lines that start with From and not From:
    if not line.startswith('From') or line.startswith('From:'):
        continue
    email = line.split()[1]
    domain = email.split('@')[1]

    if domain in emails.keys():
        emails[domain] += 1
    else:
        emails[domain] = 1

fh.close()

print(emails)
