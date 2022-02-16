#3
name = ('Shaun', 'Ron', 'Michael')
seat_numbers = (101, 102, 103)
result = {}
for i in range(len(seat_numbers)):
    result[name[i]] = seat_numbers[i]
print(result)
