# Name    : Exercise3-3.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Calculates grade based on a given score
#           Quits if bad data is input

try:
    grade = float(input('Enter score: '))
except:
    print('Bad score')
    quit()

if grade > 1.0 or grade < 0:
    print('Bad score')
    quit()

if grade >= 0.9:
    print('A')
elif grade >= 0.8:
    print('B')
elif grade >= 0.7:
    print('C')
elif grade >= 0.6:
    print('D')
else:
    print('F')
