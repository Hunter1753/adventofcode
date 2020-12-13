def uniqueCount(group):
	return len(set(group))

groupList = []
tempGroup = ""
with open("./6/input.txt") as inputFile:
	for line in inputFile:
		line = line.replace("\n","")
		if len(line) > 0:
			tempGroup += line
		else:
			groupList.append(tempGroup)
			tempGroup = ""
	if len(tempGroup) > 0:
		groupList.append(tempGroup)

groupList = list(map(uniqueCount,groupList))

print("{} unique options in groups".format(sum(groupList)))