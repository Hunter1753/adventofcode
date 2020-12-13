#plaid brown bags contain 2 dotted indigo bags, 1 dull indigo bag, 2 light brown bags.
def parseRule(textRule):
	outputRule = {}
	textRule = textRule.split(",")
	beginning = textRule[0].split("bags contain")
	name = beginning[0].strip()
	subBags = []
	if "no" in beginning[1]:
		pass
	else:
		textRule = [beginning[1]] + textRule[1:]
		for rule in textRule:
			rule = rule.strip().split(" ")
			count = int(rule[0])
			color = rule[1] + " " + rule[2]
			subBags.append((count, color))
	return (name, subBags)

def findContainingBags(color, inverseRules):
	containingColors = [color]
	if color in inverseRules:
		additionalColors = list(map(lambda c: findContainingBags(c, inverseRules),inverseRules[color]))
		additionalColors = [item for sublist in additionalColors for item in sublist]
		containingColors += additionalColors
	return containingColors

rules = {}
with open("./7/input.txt") as inputFile:
	for line in inputFile:
		rule = parseRule(line)
		rules[rule[0]] = rule[1]

inverseRules = {}
for key in rules:
	for bag in rules[key]:
		bag = bag[1]
		inverseRules.setdefault(bag, []).append(key)

print(len(set(findContainingBags("shiny gold", inverseRules))) - 1)
