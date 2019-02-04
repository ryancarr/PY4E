# Name    : Exercise5-1.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Ask user for multiple numbers then output total,
#           count and average

total = 0
count = 0

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break

    try:
        number = int(number)
    except:
        print('Invalid number')
        continue

    total += number
    count += 1

average = float(total) / count
print(total, count, average)
