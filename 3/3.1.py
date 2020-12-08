forestMap = []
with open("./3/input.txt") as inputFile:
	for line in inputFile:
		forestMap.append(line)

column = 0
numberOfTrees = 0

newmap = []
for row in forestMap:
	rowlist = list(row)
	if rowlist[column] == "#":
		numberOfTrees += 1
		rowlist[column] = "X"
	else:
		rowlist[column] = "O"
	column += 3
	if column > 30:
		column -= 31
	newmap.append("".join(rowlist))

print(newmap)

print("you encountered {} trees".format(numberOfTrees))