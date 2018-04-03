# Integer: If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"

num = 200

if type(num) == int:
    if num >= 100:
        print "That's a big number!"
    elif num < 100:
        print "That's a small number!"

# String: If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

string = "This is a string which will continue to haunt your dreams for ever and ever"

if len(string) >= 50:
    print "Long sentence"
else:
    print "Short sentence"

# List: If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

if len(a) >= 10:
    print "Big list!"
else:
    print "Short list"