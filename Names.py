students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names():
    for i in range(len(students)):
        famousPeeps = ""
        for data in range(len(students[i])):
            famousPeeps += " " + students[i].values()[data]
        print famousPeeps

names()
