numbers = [7, 4, 3, 9, 10, 7, 13, 5, 8]
numbers.append(14)
numbers.insert(0, 12)
numbers.remove(3)
print(numbers)
print(numbers.index(10))
print(50 in numbers)
print(numbers.count(7))

sequence = [34, 54, 64, 98, 39, 27, 48]
sequence2 = sequence.copy()
sequence.pop()
print(sequence)
sequence.sort()
print(sequence)
sequence.reverse()
print(sequence)
print(sequence2)