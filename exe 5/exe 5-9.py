# Write a Python program to print yesterdays' date.
# Expected Output:

from datetime import date, timedelta
print(date.today() + timedelta(days=-1))