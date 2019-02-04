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
