grade = ""

for i in range(1, 11):
    import random
    num = random.randint(60, 100)
    if num <= 100 and num >= 90:
        grade = "A"
    elif num < 90 and num >= 80:
        grade = "B"
    elif num < 80 and num >= 70:
        grade = "C"
    elif num < 70 and num >= 60:
        grade = "D"
    print "Score: " , num, "; Your grade is " , grade

print "End of the program. Bye!"






#     Scores and Grades
# Score: 87; Your grade is B
# Score: 67; Your grade is D
# Score: 95; Your grade is A
# Score: 100; Your grade is A
# Score: 75; Your grade is C
# Score: 90; Your grade is A
# Score: 89; Your grade is B
# Score: 72; Your grade is C
# Score: 60; Your grade is D
# Score: 98; Your grade is A
# End of the program. Bye!