# Name    : Exercise4-7.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Calculates a grade based on a given score
#           Uses function to perform calculation

def computegrade(score):
    if score > 1.0 or score < 0:
        grade = 'Bad score'
    elif score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'

    return grade

try:
    score = float(input('Enter score: '))
except:
    print('Bad score')
    quit()

grade = computegrade(score)
print(grade)
