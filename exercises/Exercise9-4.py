# Name    : Exercise9-4.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Open a file, extract email address and keep running count
#           Store data in dictionary output maximum count to user

# Text files are stored in the data folder one level up
filename = input('Enter a filename: ')
if filename == 'mbox-short.txt':
    filename = '../data/mbox-short.txt'
elif filename == 'mbox.txt':
    filename = '../data/mbox.txt'
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

    if email in emails.keys():
        emails[email] += 1
    else:
        emails[email] = 1

fh.close()

maximum = ['',0]

for email in emails:
    if emails[email] > maximum[1]:
        maximum[0] = email
        maximum[1] = emails[email]

print(maximum[0], maximum[1])
