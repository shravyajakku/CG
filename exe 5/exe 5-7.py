# Write a Python program to convert a string to datetime.

from datetime import datetime

myString = 'Oct 12 2002 12:45 PM'

result = datetime.strptime(myString, '%b %d %Y %I:%M %p')

print(result)