list = "if (a > b)"
list2 = ""
count = 0;

for i in list:
    if i == ")" or i == '(':
        list2 = list2 + " "
    list2 = list2 + i
print list2
