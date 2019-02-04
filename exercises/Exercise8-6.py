# Name    : Exercise8-5.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Read numbers into a list, use built-in min and max
#           methods to calculate minimum and maximum values

numbers = []

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break

    try:
        number = int(number)
    except:
        print('Invalid number')
        continue

    numbers.append(number)

minimum = min(numbers)
maximum = max(numbers)

print('Maximum:', maximum)
print('Minimum:', minimum)
