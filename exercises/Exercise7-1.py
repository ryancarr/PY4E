# Text files are stored in the data folder one level up
filename = '../data/mbox-short.txt'

fh = open(filename,'r')
for line in fh:
    print(line.strip().upper())

fh.close()
