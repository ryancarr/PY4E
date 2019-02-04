# Name    : Exercise4-6.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Calculates pay based on hours worked and pay rate
#           Uses function to calculate pay

def computepay(hours, rate):
    if(hours > 40):
        hours_over = hours - 40
        overtime = hours_over * (rate * 1.5)
        pay = 40 * rate + overtime
    else:
        pay = hours * rate

    return pay

try:
    hours = float(input('Enter hours: '))
except:
    print('Error, please enter numeric input')
    quit()

try:
    rate = float(input('Enter rate: '))
except:
    print('Error, please enter numeric input')
    quit()

pay = computepay(hours, rate)

print('Pay:', pay)
