adapters = [0]
with open("./10/input.txt") as inputFile:
	for line in inputFile:
		adapter = int(line.replace("\n",""))
		adapters.append(adapter)

adapters.sort()
adapters.append(adapters[-1]+3)

possibilities = [0]*len(adapters)
possibilities[-1] = 1

def getPossibleWays(index):
	#we have seen this already
	if possibilities[index] != 0:
		return possibilities[index]
	
	sumOfFollowing = 0
	for i in range(index+1, index+4):
		if i >= len(adapters):
			break
		if adapters[index] - adapters[i] <= 3:
			sumOfFollowing += getPossibleWays(i)

	possibilities[index] = sumOfFollowing
	return sumOfFollowing

possibleWays = getPossibleWays(0)

print("The number of possible ways is {}".format(possibleWays))