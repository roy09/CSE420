import re

# define the keywords
KEYWORDS = {"if", "else", "for", "while", "true", "int", "double"}
DATA_TYPE = {"int", "double"}
MATH_OPS = {'+', '-', '*', '/', '%'}
LOGIC_OPS = {'>', '<' '=='}
# define the to be returned structures
keywords = []
identifiers = []
mathOps = []
logicOps = []
numVals = []
others = []

with open("data.txt") as input:
    for line in input:
        temp = re.split(';', line)
        temp = temp[0].split()

        # check it is a keyword
        for item in temp:
            if item in KEYWORDS:
                keywords.append(item)
                continue

        # check if is a math operation
        for item in temp:
            if item in MATH_OPS:
                mathOps.append(item)
                continue


        # check if it is a logical operation
        for item in temp:
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


        others.append(item)

print "Keywords: "
print keywords
print "Identifiers: "
print identifiers
print "Math Operations: "
print mathOps
print "Logic Operations: "
print logicOps
print "Numeric Values: "
print numVals
print "Others: "
print others
