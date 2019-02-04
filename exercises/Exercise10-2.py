# Name    : Exercise10-2.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Open a file, extract hours and keep running count
#           Store data in dictionary and sort then display to user

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

hours = {}

for line in fh:
    # Only use data from lines that start with From and not From:
    if not line.startswith('From') or line.startswith('From:'):
        continue
    time = line.split()[5]
    hour = time.split(':')[0]

    hours[hour] = hours.get(hour,0) + 1

fh.close()

times = hours.items()

times.sort()

for time in times:
    print(time[0], time[1])
