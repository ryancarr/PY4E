hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
if(hours > 40):
    hours_over = hours - 40
    overtime = hours_over * (rate * 1.5)
    pay = 40 * rate + overtime
else:
    pay = hours * rate

print('Pay:', pay)
