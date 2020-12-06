def findMatching(numbers, value):
	for number1 in numbers:
		for number2 in numbers:
			variables = [number1, number2]
			if (len(set(variables)) != len(variables)):
				continue
			if number1 + number2 == value:
				print("{} + {} = {}, {} * {} = {}".format(number1,number2,value,number1,number2,number1*number2))
				return

numbers = []
with open("./1/input.txt") as inputFile:
	for line in inputFile:
		numbers.append(int(line))

findMatching(numbers, 2020)
