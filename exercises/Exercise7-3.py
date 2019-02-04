# Text files are stored in the data folder one level up
filename = input('Enter a filename: ')
if filename == 'mbox-short.txt':
    filename = '../data/mbox-short.txt'
elif filename == 'mbox.txt':
    filename = '../data/mbox.txt'
elif filename == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    quit()
else:
    print('File cannot be opened:', filename)
    quit()

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
