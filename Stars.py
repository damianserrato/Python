#Stars

x = ["String",5,"Badapple",9,8,"Tan","Tut"]

def draw_stars():
    for count in range(0, len(x)):
        j = 0
        star = ""
        if type(x[count]) == str:
            print x[count][0].lower()
        elif type(x[count]) == int:
            while j < x[count]:
                star += "*"
                j = j + 1
        print star

draw_stars()