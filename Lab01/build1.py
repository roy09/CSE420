import re

# define the keywords
KEYWORDS = {"if", "else", "for", "while", "true", "int", "double"}
DATA_TYPE = {"int", "double"}
MATH_OPS = {'+', '-', '*', '/', '%', '='}
LOGIC_OPS = {'>', '<' '=='}
# define the to be returned structures
keywords = []
identifiers = []
mathOps = []
logicOps = []
numVals = []
others = []
openingBrackets = ['{', '(', '[']
closingBrackets = ['}', ')', ']']


flag = False
opening = False

with open("data.txt") as input:
    for line in input:
        temp = re.split(';', line)

        # deal with brackets
        temp2 = ""
        for i in temp[0]:
            if i in closingBrackets:
                temp2 = temp2 + " "
            if i in openingBrackets:
                opening = True

            temp2 = temp2 + i
            if opening:
                temp2 = temp2 + " "
                opening = False
        temp[0] = temp2
        temp = temp[0].split()

        for item in temp:
            if (flag):
                if item[len(item) - 1] == ',':
                    identifiers.append(item[:-1])

                else:
                    identifiers.append(item)
                    flag = False
                continue

            # check it is a keyword
            if item in KEYWORDS:
                keywords.append(item)
                if item in DATA_TYPE:
                    flag = True
                continue

            if item in identifiers:
                continue

            # check if is a math operation
            if item in MATH_OPS:
                mathOps.append(item)
                continue

            # check if it is a logical operation
            if item in LOGIC_OPS:
                logicOps.append(item)
                continue

            # check if it is a numeric value
            if item.isdigit():
                numVals.append(item)
                continue
            try:
                float(item)
                numVals.append(item)
                continue
            except ValueError:
                pass

            # if nothing satisfies, add to others
            others.append(item)
            prev = item

print "Keywords: "
print set(keywords)
print "Identifiers: "
print set(identifiers)
print "Math Operations: "
print set(mathOps);
print "Logic Operations: "
print set(logicOps)
print "Numeric Values: "
print set(numVals)
print "Others: "
print set(others)
