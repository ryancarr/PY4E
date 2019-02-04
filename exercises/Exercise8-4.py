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
