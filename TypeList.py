# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

myList = ['magical unicorns',19,'hello',98.98,'world']
mySum = 0
myString = ""

for count in range(0, len(myList)):
    if type(myList[count]) == int:
        mySum += myList[count]
    elif type(myList[count]) == str:
        myString += myList[count]

myString = "String: " + myString
print myString
mySum = "Sum: " + myString

if mySum > 0 and len(myString) > 1:
    print "The list you entered is of a mixed type"
elif mySum > 0 and len(myString) == 0:
    print "The list you entered is of an integer type"
else:
    print "The list you entered is of a string type"