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
