adapters = []
with open("./10/input.txt") as inputFile:
	for line in inputFile:
		adapter = int(line.replace("\n",""))
		adapters.append(adapter)

adapters.sort()
differences = {}

lastJoltage = 0
for adapter in adapters:
	difference = adapter - lastJoltage
	differences.setdefault(difference, 0)
	differences[difference] += 1
	lastJoltage = adapter

#your device has 3 higher than the last adapter
differences[3] += 1

print(differences)

print("The product of {} and {} is {}".format(differences[1], differences[3], differences[1] * differences[3]))