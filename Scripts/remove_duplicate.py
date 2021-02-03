numbers = [2, 6, 16, 8, 31, 41, 24, 6, 8, 45, 21]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)