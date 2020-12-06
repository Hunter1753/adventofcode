def checkPassword(data):
	return (data["password"][data["pos1"] - 1] == data["char"]) != (data["password"][data["pos2"] -1 ] == data["char"])

passwords = []
with open("./2/input.txt") as inputFile:
	for line in inputFile:
		tokens = line.split(" ")
		minMax = tokens[0].split("-")
		data = {
			"pos1": int(minMax[0]),
			"pos2": int(minMax[1]),
			"char": tokens[1][:-1],
			"password": tokens[2][:-1]
		}
		passwords.append(data)

countOfValidPasswords = 0
for password in passwords:
	if checkPassword(password):
		countOfValidPasswords += 1

print("{} passwords are valid of {} total passwords".format(countOfValidPasswords, len(passwords)))