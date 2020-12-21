from itertools import product
import copy

initialRows = []
with open("./11/input.txt") as inputFile:
	for line in inputFile:
		row = list(line.replace("\n",""))
		initialRows.append(row)

def getSeat(x,y, rows):
	if x < 0 or y < 0 or x >= len(rows[0]) or y >= len(rows):
		return 0
	return 0 if rows[y][x] in ["L", "."] else 1

def getNewState(x, y, rows):
	a = [-1,0,1]
	spacesToCheck = list(product(a, repeat=2))
	spacesToCheck.remove((0, 0))

	spacesToCheck = [[sum(x) for x in zip((x,y),offset)] for offset in spacesToCheck ]

	occupiedSeats = sum([getSeat(*pos, rows) for pos in spacesToCheck])

	if rows[y][x] == "L":
		if occupiedSeats == 0:
			return "#"
		else:
			return "L"
	else:
		if occupiedSeats >= 4:
			return "L"
		else:
			return "#"

rows = initialRows

rounds = 0
while True:
	rounds += 1
	newRows = copy.deepcopy(rows)
	numberOfChanges = 0
	for y in range(0,len(rows)):
		for x in range(0,len(row)):
			seat = rows[y][x]
			if seat in ["L","#"]:
				newState = getNewState(x,y, rows)
				if newState != seat:
					numberOfChanges += 1
				newRows[y][x] = newState

	if numberOfChanges == 0:
		break
	rows = newRows

total = sum([seat in ["#","L"] for row in rows for seat in row])
occupied = sum([seat == "#" for row in rows for seat in row])

print("settled after {} rounds with {} of {} seats occupied".format(rounds, occupied, total))