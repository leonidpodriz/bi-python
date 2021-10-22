"""
Play the 7-boom game:
print all numbers between 1 and 100;
if a number is divisible by 7 or contains the digit 7,
print “BOOM” instead of the number.
"""

# Solution 1
for number in range(1, 101):
    if number % 7 == 0 or number - 7 :
        print('BOOM')
    else:
        print(number)
