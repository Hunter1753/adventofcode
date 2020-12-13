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

def countContainedBags(bag, rules, depth = 0):
	color = bag[1]
	containedBags = rules[color]
	countOfBags = [1]
	if len(containedBags) > 0:
		countOfBags += list(map(lambda b: countContainedBags(b, rules, depth+1), containedBags))
		print(('-'* depth) + "{}x{}".format(bag[0], countOfBags))
	return bag[0] * sum(countOfBags)

rules = {}
with open("./7/input.txt") as inputFile:
	for line in inputFile:
		rule = parseRule(line)
		rules[rule[0]] = rule[1]

print(countContainedBags((1,"shiny gold"), rules)-1)
