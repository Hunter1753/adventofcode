import math

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

def validateByr(value):
	try:
		value = int(value)
	except ValueError:
		return False
	if not (1920 <= value <= 2002):
		return False
	return True

def validateIyr(value):
	try:
		value = int(value)
	except ValueError:
		return False
	if not (2010 <= value <= 2020):
		return False
	return True

def validateEyr(value):
	try:
		value = int(value)
	except ValueError:
		return False
	if not (2020 <= value <= 2030):
		return False
	return True

def validateHgt(value):
	height = value[:-2]
	unit = value[-2:]

	if unit not in ["in", "cm"]:
		return False

	try:
		height = int(height)
	except ValueError:
		return False

	if unit == "cm":
		if not (150 <= height <= 193):
			return False
	else:
		if not (59 <= height <= 76):
			return False

	return True

def validateHcl(value):
	if value[0] != "#":
		return False
	if len(value) != 7:
		return False
	try:
		int(value[1:], 16)
	except ValueError:
		return False
	return True

def validateEcl(value):
	if value not in ["amb","blu","brn","gry","grn","hzl","oth"]:
		return False
	return True

def validatePid(value):
	if len(value) != 9:
		return False
	return True

def validateField(key, value):
	switch = {
		"byr": validateByr,
		"iyr": validateIyr,
		"eyr": validateEyr,
		"hgt": validateHgt,
		"hcl": validateHcl,
		"ecl": validateEcl,
		"pid": validatePid,
		"cid": lambda value: True
	}

	return switch[key](value)

def validatePassport(passport):
	for key in passport.keys():
		if validateField(key, passport[key]):
			continue
		else:
			print("[X] passport has wrong field {}: {}".format(key, passport[key]))
			return False
	return True

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
		if validatePassport(passport):
			print("[O] passport with {} is valid".format(passportKeys))
			validPassports += 1
			continue
	else:
		print("[X] passport missing {}, {}".format(necessaryKeys.difference(passportKeys), passport))

print("the number of valid passports is {}".format(validPassports))