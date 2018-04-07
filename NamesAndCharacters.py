users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def findUsers():
    num = 1
    something = 0
    for i in range(len(users)):
        for idx in range(len(users.values()[i])):
            string = ""
            string += "- " + users.values()[i][idx]['first_name'] + " " + users.values()[i][idx]['last_name']
            print num, string, " - ", len(users.values()[i][idx]['first_name'] + users.values()[i][idx]['last_name'])



findUsers()