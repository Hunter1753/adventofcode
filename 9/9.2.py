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

invalidNumber = number

for i in range(0, len(numbers)):
	for j in range(i+1, len(numbers)):
		numbersToSum = numbers[i:j+1]
		contiguosSum = sum(numbersToSum)
		if contiguosSum == invalidNumber:
			numbersToSum.sort()
			sumOfSmallestAndLargest = numbersToSum[0] + numbersToSum[len(numbersToSum)-1]
			print("The sum of the smallest [{}] and largest [{}] in the list of contiguos numbers that add up to {} is {}".format(numbersToSum[0], numbersToSum[len(numbersToSum)-1],invalidNumber, sumOfSmallestAndLargest))
			exit(0)
		elif contiguosSum > invalidNumber:
			break
		else:
			continue