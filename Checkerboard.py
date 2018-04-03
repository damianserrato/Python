#A program that prints a 'checkerboard' pattern to the console

i = 1
j = 1
star1 = ""
star2 = ""

while i < 9:
    star1 += "* "
    i += 1

while j < 9:
    star2 += " *"
    j += 1

for idx in range(1,5):
    print star1
    print star2