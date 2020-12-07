def rowToMap


forestMap = []
with open("./3/input.txt") as inputFile:
	for line in inputFile:
		forestMap.append(line)

numberOfTrees = 0
column = 0

newmap = map(lambda row:
		rowlist = list(row)
		if rowlist[column] == "#":
			numberOfTrees += 1
			rowlist[column] = "X"
		else:
			rowlist[column] = "O"
		column += 3
		if column > 30:
			column -= 30
		return "".join(rowlist)
	, forestMap)

print(newmap)

print("you encountered {} trees".format(numberOfTrees))