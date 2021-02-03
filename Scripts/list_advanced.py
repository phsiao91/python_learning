names = ['Ray', 'Kobe', 'Loki', 'Nicole']
names[3] = 'Nycole'
print(names[1:])
print(names[2])
print(names[2:4])
print(names[0])
print(names)

numbers = [2, 6, 8, 6, 4, 2, 11, 38, 10, 33]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

sequence = [2, 5, 56, 55, 77, 43, 7, 84, 78, 41, 32]
highest = sequence[0]
for best in sequence:
    if best > highest:
        highest = best
print(highest)
