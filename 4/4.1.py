def tokenizePassports(inputList):
	tempPassport = {}
	passports = []
	for row in inputList:
		if len(row) > 0:
			items = row.split(" ")
			for item in items:
				item = item.split(":")
				tempPassport[item[0]] = item[1]
		else:
			passports.append(tempPassport)
			tempPassport = {}
	if len(tempPassport) > 0:
		passports.append(tempPassport)
	return passports

inputList = []
with open("./4/input.txt") as inputFile:
	for line in inputFile:
		line = line.replace("\n","")
		inputList.append(line)

passports = tokenizePassports(inputList)

validPassports = 0
necessaryKeys = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}
for passport in passports:
	passportKeys = set(passport.keys())
	if necessaryKeys.issubset(passportKeys):
		print("[O] passport with {} is valid".format(passportKeys))
		validPassports += 1
	else:
		print("[X] passport missing {}, {}".format(necessaryKeys.difference(passportKeys), passport))

print("the number of valid passports is {}".format(validPassports))