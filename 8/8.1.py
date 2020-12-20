instructions = []
with open("./8/input.txt") as inputFile:
	for line in inputFile:
		instruction = line.replace("\n","").split(" ")
		instructions.append(instruction)

visitedInstructions = set()
pc = 0
acc = 0
while(True):
	if pc in visitedInstructions:
		break
	else:
		visitedInstructions.add(pc)
	instruction = instructions[pc][0]
	value = int(instructions[pc][1])

	if instruction == "acc":
		acc += value
		pc += 1
	elif instruction == "jmp":
		pc += value
	else:
		pc += 1

print("The value of the accumulator is {} and the program repeated itself on line {}".format(acc, pc))