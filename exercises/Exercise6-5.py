str = 'X-DSPAM-Confidence: 0.8475 '
position = str.find(':')
number = float(str[position + 1:])

print(number)
