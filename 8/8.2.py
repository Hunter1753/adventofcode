import copy

instructions = []
with open("./8/input.txt") as inputFile:
	for line in inputFile:
		instruction = line.replace("\n","").split(" ")
		instructions.append(instruction)

for instructionToChange in range(0,len(instructions)):
	newInstructions = copy.deepcopy(instructions)
	if instructions[instructionToChange][0] == "jmp":
		newInstructions[instructionToChange][0] = "nop"
	elif instructions[instructionToChange][0] == "nop":
		newInstructions[instructionToChange][0] = "jmp"
	else:
		continue

	visitedInstructions = set()
	loop = True
	pc = 0
	acc = 0
	while(True):
		if pc == len(newInstructions):
			#program terminated successfully
			loop = False
			break
		if pc in visitedInstructions:
			break
		else:
			visitedInstructions.add(pc)
		instruction = newInstructions[pc][0]
		value = int(newInstructions[pc][1])

		if instruction == "acc":
			acc += value
			pc += 1
		elif instruction == "jmp":
			pc += value
		else:
			pc += 1

	if loop:
		continue
	else:
		print("The value of the accumulator is {} and the program has to be changed on line {}".format(acc, instructionToChange))
		break

if loop:
	print("no instruction change fixed the problem")