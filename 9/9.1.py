import collections
from itertools import combinations

def checkIsSum(value, values):
	toCheck = combinations(values, 2)
	toCheck = [sum(x) for x in toCheck]
	return value in toCheck


numbers = []
with open("./9/input.txt") as inputFile:
	for line in inputFile:
		number = int(line.replace("\n",""))
		numbers.append(number)

last25Numbers = collections.deque(numbers[:25],maxlen=25)

for number in numbers[25:]:
	if checkIsSum(number, last25Numbers):
		last25Numbers.append(number)
	else:
		break

print("{} is not matching any sum of the last 25 numbers.".format(number))