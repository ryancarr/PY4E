# Name    : Exercise6-5.py
# Author  : Ryan Carr
# Date    : 02/03/19
# Purpose : Slice float value from a string and display it on screen

str = 'X-DSPAM-Confidence: 0.8475 '
position = str.find(':')
number = float(str[position + 1:])

print(number)
