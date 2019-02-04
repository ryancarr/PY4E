minimum = None
maximum = None

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break

    try:
        number = int(number)
    except:
        print('Invalid number')
        continue

    if minimum == None or maximum == None:
        minimum = number
        maximum = number
    elif minimum > number:
        minimum = number
    elif maximum < number:
        maximum = number

print(maximum, minimum)
