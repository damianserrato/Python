myInfo = {
    'name': "Santiago",
    'age': "255",
    'country': "Poland",
    'language': "Ruby"
}

def printDict():
    for data in range(len(myInfo)):
        print "My ", myInfo.keys()[data], " is", myInfo.values()[data]

printDict()