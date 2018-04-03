# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
newList = []

for count in range(0, len(word_list)):
    for c in word_list[count]:
        if c == "o":
            newList.append(word_list[count])
print newList