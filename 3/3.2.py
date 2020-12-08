forestMap = []
with open("./3/input.txt") as inputFile:
	for line in inputFile:
		forestMap.append(line)


def countNumberOfTrees(right, down):
	column = 0
	numberOfTrees = 0
	newMap = forestMap[0::down]
	for row in newMap:
		if row[column] == "#":
			numberOfTrees += 1
		
		column += right
		if column > 30:
			column -= 31
	return [numberOfTrees, right, down]

numberOfTrees = []
numberOfTrees.append(countNumberOfTrees(1,1))
numberOfTrees.append(countNumberOfTrees(3,1))
numberOfTrees.append(countNumberOfTrees(5,1))
numberOfTrees.append(countNumberOfTrees(7,1))
numberOfTrees.append(countNumberOfTrees(1,2))

product = 1
for number in numberOfTrees:
	product *= number[0]
	print("you encountered {} trees on slope {}, {}".format(number[0], number[1], number[2]))

print("the product of all trees on the slopes is {}".format(product))