my_dict = {
    "Aero": "45663466",
    "Michael": "70234532",
    "Jay": "54456567"
}
new_dict = {}
def myfunction():
    li = []
    for i in my_dict:
        li.append((i, my_dict[i]))
    print li
myfunction()