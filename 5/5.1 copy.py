seats = []
with open("./5/input.txt") as inputFile:
	for line in inputFile:
		line = line.replace("\n","").replace("F","0").replace("B","1").replace("L","0").replace("R","1")
		row = int(line[:-3], 2)
		column = int(line[-3:], 2)
		seat = (row * 8) + column
		seats.append(seat)

seats.sort()
seats = set(seats)

allSeats = set(range(89,990))

print(seats.symmetric_difference(allSeats))