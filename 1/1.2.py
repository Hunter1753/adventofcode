def findMatching(numbers, value):
	for number1 in numbers:
		for number2 in numbers:
			for number3 in numbers:
				variables = [number1, number2, number3]
				if (len(set(variables)) != len(variables)):
					continue
				if number1 + number2 + number3 == value:
					print("{} * {} * {} = {}".format(number1,number2,number3,number1*number2*number3))
					return

numbers = []
with open("./1/input.txt") as inputFile:
	for line in inputFile:
		numbers.append(int(line))

findMatching(numbers, 2020)
