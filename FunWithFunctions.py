# Odd/Even
def odd_even():
    for i in range(1, 2001):
        if i % 2 != 0:
            print "Number is " + str(i) + ". This is an odd number."
        elif i % 2 == 0:
            print "Number is " + str(i) + ". This is an even number."
odd_even()

#Multiply
a = [2,4,6,8,10]
b = 5

def multiply(a,b):
    for i in range(0, len(a)):
        a[i] *= b
    print a
multiply(a,b)

#Layered Multiples
arr = [a]
by = 3
new_array = [1]