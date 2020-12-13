def setIntersectionCount(group):
	return len(set.intersection(*group))

groupList = []
tempGroup = []
with open("./6/input.txt") as inputFile:
	for line in inputFile:
		line = line.replace("\n","")
		if len(line) > 0:
			tempGroup.append(set(line))
		else:
			groupList.append(tempGroup)
			tempGroup = []
	if len(tempGroup) > 0:
		groupList.append(tempGroup)

groupList = list(map(setIntersectionCount,groupList))

print("{} common options in groups".format(sum(groupList)))