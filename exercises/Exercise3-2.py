# Name    : Exercise3-2.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Calculates pay based on user input hours and rate.
#           Capable of handling overtime at time and a half rate
#           Gracefully quits if bad data is input

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

if(hours > 40):
    hours_over = hours - 40
    overtime = hours_over * (rate * 1.5)
    pay = 40 * rate + overtime
else:
    pay = hours * rate

print('Pay:', pay)
